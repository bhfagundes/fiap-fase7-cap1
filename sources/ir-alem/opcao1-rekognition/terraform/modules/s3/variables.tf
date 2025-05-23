variable "project_name" {
  description = "Nome do projeto"
  type        = string
}

variable "bucket_name" {
  description = "Nome do bucket S3"
  type        = string
}

variable "lambda_arn" {
  description = "ARN da função Lambda"
  type        = string
} 