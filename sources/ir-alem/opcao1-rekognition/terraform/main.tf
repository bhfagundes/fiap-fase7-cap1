terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Módulo para configuração do Rekognition
module "rekognition" {
  source = "./modules/rekognition"

  project_name     = var.project_name
  environment      = var.environment
  collection_name  = var.collection_name
  min_confidence   = var.min_confidence
  max_labels       = var.max_labels
}

# Módulo para configuração do S3
module "s3" {
  source = "./modules/s3"

  project_name    = var.project_name
  environment     = var.environment
  bucket_name     = var.bucket_name
  enable_versioning = true
}

# Módulo para configuração do Lambda
module "lambda" {
  source = "./modules/lambda"

  project_name    = var.project_name
  environment     = var.environment
  function_name   = var.function_name
  runtime         = "python3.9"
  handler         = "lambda_function.lambda_handler"
  timeout         = 30
  memory_size     = 256
  s3_bucket_id    = module.s3.bucket_id
}

# Módulo para configuração do API Gateway
module "api_gateway" {
  source = "./modules/api_gateway"

  project_name    = var.project_name
  environment     = var.environment
  api_name        = var.api_name
  lambda_arn      = module.lambda.function_arn
  lambda_name     = module.lambda.function_name
} 