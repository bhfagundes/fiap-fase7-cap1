variable "project_name" {
  description = "Nome do projeto"
  type        = string
}

variable "api_name" {
  description = "Nome da API"
  type        = string
}

variable "environment" {
  description = "Ambiente (dev, prod, etc)"
  type        = string
}

variable "lambda_invoke_arn" {
  description = "ARN de invocação da função Lambda"
  type        = string
}

variable "lambda_function_name" {
  description = "Nome da função Lambda"
  type        = string
}

variable "lambda_arn" {
  description = "ARN da função Lambda"
  type        = string
} 