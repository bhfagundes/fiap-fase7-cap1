variable "project_name" {
  description = "Nome do projeto"
  type        = string
}

variable "function_name" {
  description = "Nome da função Lambda"
  type        = string
}

variable "function_zip" {
  description = "Caminho para o arquivo ZIP da função"
  type        = string
}

variable "collection_name" {
  description = "Nome da coleção do Rekognition"
  type        = string
}

variable "min_confidence" {
  description = "Confiança mínima para detecção"
  type        = number
}

variable "max_labels" {
  description = "Número máximo de labels"
  type        = number
} 