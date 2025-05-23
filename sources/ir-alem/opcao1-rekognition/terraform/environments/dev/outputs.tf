output "api_endpoint" {
  description = "Endpoint da API"
  value       = module.api_gateway.api_endpoint
}

output "bucket_name" {
  description = "Nome do bucket S3"
  value       = module.s3.bucket_name
}

output "collection_id" {
  description = "ID da coleção do Rekognition"
  value       = module.rekognition.collection_id
}

output "function_name" {
  description = "Nome da função Lambda"
  value       = module.lambda.function_name
} 