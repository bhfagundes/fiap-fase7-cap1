# Integração de IA na Infraestrutura AWS - AWS Rekognition

## Objetivo
Implementar um sistema de reconhecimento de imagens usando AWS Rekognition para análise de culturas e monitoramento de plantações.

## Arquitetura
O sistema utiliza os seguintes componentes AWS:
- AWS Rekognition para análise de imagens
- S3 para armazenamento de imagens
- Lambda para processamento
- API Gateway para exposição de endpoints
- CloudWatch para monitoramento

## Implementação

### 1. Configuração do AWS Rekognition
- Criação de coleção para armazenar imagens de referência
- Configuração de labels personalizados para culturas
- Definição de thresholds para detecção

### 2. Pipeline de Processamento
1. Upload de imagens para S3
2. Trigger de Lambda
3. Análise com Rekognition
4. Armazenamento de resultados
5. Notificações via SNS

### 3. Integração com Sistema Existente
- Conexão com dashboard
- Visualização de resultados
- Alertas automáticos

## Documentação Técnica

### Prints de Configuração
- [Configuração Rekognition](docs/rekognition-setup.png)
- [Criação de Coleção](docs/collection-creation.png)
- [Configuração de Labels](docs/labels-config.png)

### Código Fonte
- [Lambda Function](lambda_function.py)
- [API Gateway](api_gateway.yaml)
- [Terraform](main.tf)

## Vídeo Demonstrativo
[Link do vídeo](https://youtube.com/watch?v=...)

## Justificativa
A implementação do AWS Rekognition permite:
- Análise automática de saúde das plantações
- Detecção precoce de doenças
- Monitoramento em larga escala
- Redução de custos com inspeção manual 