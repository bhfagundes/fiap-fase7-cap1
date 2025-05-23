variable "aws_region" {
  description = "Região AWS onde os recursos serão criados"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Nome do projeto"
  type        = string
  default     = "farmtech-rekognition"
}

variable "environment" {
  description = "Ambiente (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "collection_name" {
  description = "Nome da coleção do Rekognition"
  type        = string
  default     = "farmtech-crops"
}

variable "min_confidence" {
  description = "Confiança mínima para detecção"
  type        = number
  default     = 80
}

variable "max_labels" {
  description = "Número máximo de labels por imagem"
  type        = number
  default     = 10
}

variable "bucket_name" {
  description = "Nome do bucket S3"
  type        = string
  default     = "farmtech-images"
}

variable "function_name" {
  description = "Nome da função Lambda"
  type        = string
  default     = "farmtech-rekognition-processor"
}

variable "api_name" {
  description = "Nome da API Gateway"
  type        = string
  default     = "farmtech-rekognition-api"
} 