provider "aws" {
  region = var.aws_region
}

module "rekognition" {
  source = "../../modules/rekognition"

  project_name    = var.project_name
  collection_name = var.collection_name
}

module "s3" {
  source = "../../modules/s3"

  project_name = var.project_name
  bucket_name  = var.bucket_name
  lambda_arn   = module.lambda.function_arn
}

module "lambda" {
  source = "../../modules/lambda"

  project_name    = var.project_name
  function_name   = var.function_name
  function_zip    = var.function_zip
  collection_name = var.collection_name
  min_confidence  = var.min_confidence
  max_labels      = var.max_labels
}

module "api_gateway" {
  source = "../../modules/api_gateway"

  project_name        = var.project_name
  api_name           = var.api_name
  environment        = var.environment
  lambda_invoke_arn  = module.lambda.invoke_arn
  lambda_function_name = var.function_name
  lambda_arn         = module.lambda.function_arn
} 