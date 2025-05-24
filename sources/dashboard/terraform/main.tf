# Configuração do provider AWS
provider "aws" {
  region = var.aws_region
}

# VPC e Subnets
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  version = "3.14.0"

  name = "farmtech-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["${var.aws_region}a", "${var.aws_region}b", "${var.aws_region}c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = false
  one_nat_gateway_per_az = true

  tags = {
    Environment = "production"
    Project     = "FarmTech"
  }
}

# EKS Cluster
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "18.26.6"

  cluster_name    = "farmtech-cluster"
  cluster_version = "1.24"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  eks_managed_node_groups = {
    general = {
      desired_size = 2
      min_size     = 1
      max_size     = 5

      instance_types = ["t3.medium"]
      capacity_type  = "ON_DEMAND"
    }
  }

  tags = {
    Environment = "production"
    Project     = "FarmTech"
  }
}

# Aurora Serverless
module "aurora" {
  source  = "terraform-aws-modules/rds-aurora/aws"
  version = "7.6.0"

  name           = "farmtech-aurora"
  engine         = "aurora-postgresql"
  engine_version = "13.6"
  instance_class = "db.serverless"
  serverlessv2_scaling_configuration = {
    min_capacity = 0.5
    max_capacity = 1.0
  }

  vpc_id                 = module.vpc.vpc_id
  db_subnet_group_name   = module.vpc.database_subnet_group_name
  create_security_group  = true
  allowed_cidr_blocks    = module.vpc.private_subnets_cidr_blocks

  tags = {
    Environment = "production"
    Project     = "FarmTech"
  }
}

# CloudFront Distribution
resource "aws_cloudfront_distribution" "main" {
  enabled             = true
  is_ipv6_enabled    = true
  default_root_object = "index.html"

  origin {
    domain_name = aws_s3_bucket.static.bucket_regional_domain_name
    origin_id   = "S3-${aws_s3_bucket.static.bucket}"

    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.main.cloudfront_access_identity_path
    }
  }

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD", "OPTIONS"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-${aws_s3_bucket.static.bucket}"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 3600
    max_ttl                = 86400
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }

  tags = {
    Environment = "production"
    Project     = "FarmTech"
  }
}

# S3 Bucket for Static Content
resource "aws_s3_bucket" "static" {
  bucket = "farmtech-static-content"

  tags = {
    Environment = "production"
    Project     = "FarmTech"
  }
}

# CloudFront Origin Access Identity
resource "aws_cloudfront_origin_access_identity" "main" {
  comment = "FarmTech CloudFront OAI"
}

# IoT Core
resource "aws_iot_thing_type" "sensor" {
  name = "farmtech-sensor"
}

resource "aws_iot_thing" "sensor" {
  name       = "farmtech-sensor-1"
  thing_type = aws_iot_thing_type.sensor.name

  attributes = {
    Type = "DHT11"
  }
}

# Lambda Functions
resource "aws_lambda_function" "data_processor" {
  filename         = "lambda/data_processor.zip"
  function_name    = "farmtech-data-processor"
  role            = aws_iam_role.lambda_exec.arn
  handler         = "index.handler"
  runtime         = "python3.9"
  timeout         = 30
  memory_size     = 256

  environment {
    variables = {
      DB_HOST     = module.aurora.cluster_endpoint
      DB_NAME     = "farmtech"
      DB_USER     = "admin"
      DB_PASSWORD = var.db_password
    }
  }

  tags = {
    Environment = "production"
    Project     = "FarmTech"
  }
}

# IAM Role for Lambda
resource "aws_iam_role" "lambda_exec" {
  name = "farmtech-lambda-exec"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# SNS Topic
resource "aws_sns_topic" "alerts" {
  name = "farmtech-alerts"
}

# SQS Queue
resource "aws_sqs_queue" "data_queue" {
  name                      = "farmtech-data-queue"
  delay_seconds             = 0
  max_message_size          = 262144
  message_retention_seconds = 345600
  receive_wait_time_seconds = 0
  visibility_timeout_seconds = 30

  tags = {
    Environment = "production"
    Project     = "FarmTech"
  }
}

# CloudWatch Log Group
resource "aws_cloudwatch_log_group" "main" {
  name              = "/farmtech/main"
  retention_in_days = 30

  tags = {
    Environment = "production"
    Project     = "FarmTech"
  }
}

# Variables
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}

# Outputs
output "cluster_endpoint" {
  description = "EKS cluster endpoint"
  value       = module.eks.cluster_endpoint
}

output "aurora_endpoint" {
  description = "Aurora cluster endpoint"
  value       = module.aurora.cluster_endpoint
}

output "cloudfront_domain" {
  description = "CloudFront distribution domain"
  value       = aws_cloudfront_distribution.main.domain_name
} 