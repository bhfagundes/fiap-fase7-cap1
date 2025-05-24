# Configuração do CloudWatch para o FarmTech Dashboard

Este diretório contém as configurações do Amazon CloudWatch para monitoramento, alertas e logs do FarmTech Dashboard.

## Estrutura de Arquivos

- `dashboard.json`: Configuração do dashboard principal do CloudWatch
- `alarms.json`: Configuração dos alertas do CloudWatch
- `logs.json`: Configuração dos grupos de logs e streams
- `insights.json`: Configuração das queries e dashboards do CloudWatch Insights
- `events.json`: Configuração dos eventos e regras do CloudWatch Events
- `synthetics.json`: Configuração dos testes sintéticos do CloudWatch
- `contributor-insights.json`: Configuração do CloudWatch Contributor Insights
- `anomaly-detection.json`: Configuração do CloudWatch Anomaly Detection
- `service-quotas.json`: Configuração do CloudWatch Service Quotas
- `composite-alarms.json`: Configuração do CloudWatch Composite Alarms
- `metric-math.json`: Configuração do CloudWatch Metric Math
- `metric-streams.json`: Configuração do CloudWatch Metric Streams

## Dashboard Principal

O dashboard principal (`dashboard.json`) inclui os seguintes widgets:

1. **EKS Cluster Nodes**
   - Monitoramento de nós do cluster
   - Contagem de nós falhos
   - Utilização de recursos

2. **Aurora Performance**
   - Utilização de CPU
   - Memória disponível
   - Conexões ativas

3. **Lambda Performance**
   - Número de invocações
   - Taxa de erros
   - Duração das execuções

4. **CloudFront Performance**
   - Número de requisições
   - Taxa de erros
   - Latência

5. **IoT Performance**
   - Clientes conectados
   - Mensagens publicadas
   - Status dos dispositivos

6. **SQS Queue Status**
   - Tamanho da fila
   - Idade das mensagens
   - Taxa de processamento

7. **SageMaker Performance**
   - Latência do modelo
   - Número de invocações
   - Utilização de recursos

8. **Cost Overview**
   - Custos totais
   - Custos por serviço
   - Tendências de custo

## Alertas

Os alertas configurados (`alarms.json`) incluem:

1. **EKS**
   - Alta utilização de CPU (>80%)
   - Nós falhos
   - Problemas de autoscaling

2. **Aurora**
   - Alto número de conexões (>100)
   - Baixa memória disponível
   - Alta latência

3. **Lambda**
   - Erros de execução
   - Alta duração
   - Falhas de invocação

4. **CloudFront**
   - Alta taxa de erros (>1%)
   - Problemas de cache
   - Erros de distribuição

5. **IoT**
   - Dispositivos desconectados
   - Falhas de comunicação
   - Problemas de autenticação

6. **SQS**
   - Fila muito grande (>1000 mensagens)
   - Mensagens antigas
   - Erros de processamento

7. **SageMaker**
   - Alta latência (>100ms)
   - Erros de predição
   - Problemas de modelo

8. **Custos**
   - Custo diário alto (>$100)
   - Picos de utilização
   - Tendências de aumento

## Logs

A configuração de logs (`logs.json`) inclui:

1. **Grupos de Logs**
   - `/farmtech/eks`
   - `/farmtech/aurora`
   - `/farmtech/lambda`
   - `/farmtech/cloudfront`
   - `/farmtech/iot`
   - `/farmtech/sqs`
   - `/farmtech/sagemaker`
   - `/farmtech/application`

2. **Filtros de Métricas**
   - Contagem de erros
   - Contagem de avisos
   - Erros do Lambda
   - Desconexões IoT

3. **Streams de Log**
   - Dashboard
   - API
   - Worker

## CloudWatch Insights

As queries do CloudWatch Insights (`insights.json`) incluem:

1. **Análise de Erros**
   - Erros por componente
   - Erros por tipo
   - Tendências de erros

2. **Análise de Performance**
   - Performance por endpoint
   - Latência de requisições
   - Utilização de recursos

3. **Status IoT**
   - Status dos dispositivos
   - Problemas de conexão
   - Métricas de comunicação

4. **Queries de Banco**
   - Performance de queries
   - Queries problemáticas
   - Padrões de acesso

5. **Atividade de Usuários**
   - Ações por usuário
   - Recursos acessados
   - Padrões de uso

6. **Saúde do Sistema**
   - Status dos componentes
   - Problemas de saúde
   - Métricas de sistema

7. **Eventos de Segurança**
   - Tipos de eventos
   - Fontes de eventos
   - Padrões de segurança

8. **Utilização de Recursos**
   - Uso por recurso
   - Picos de utilização
   - Tendências de uso

## Dashboards do Insights

1. **ErrorAnalysisDashboard**
   - Análise de erros
   - Análise de performance

2. **IoTDashboard**
   - Status dos dispositivos
   - Saúde do sistema

3. **PerformanceDashboard**
   - Análise de performance
   - Queries de banco
   - Utilização de recursos

4. **SecurityDashboard**
   - Eventos de segurança
   - Atividade de usuários

## Eventos

A configuração de eventos (`events.json`) inclui:

1. **Regras Agendadas**
   - Backup diário do banco de dados
   - Manutenção semanal do sistema
   - Relatório mensal
   - Varredura de segurança diária
   - Teste de performance semanal

2. **Regras Baseadas em Eventos**
   - Processamento de dados IoT
   - Notificação de erros
   - Alerta de custos

3. **Event Bus Personalizado**
   - Eventos específicos do FarmTech
   - Integração com sistemas externos
   - Roteamento de eventos

4. **Arquivos de Eventos**
   - Retenção de 365 dias
   - Eventos do bus personalizado
   - Histórico de eventos

## Testes Sintéticos

A configuração de testes sintéticos (`synthetics.json`) inclui:

1. **Testes do Dashboard**
   - Disponibilidade do dashboard (a cada 5 minutos)
   - Carregamento de páginas
   - Verificação de elementos
   - Testes de navegação

2. **Testes da API**
   - Saúde da API (a cada 1 minuto)
   - Endpoints críticos
   - Respostas HTTP
   - Validação de dados

3. **Testes IoT**
   - Conexão IoT (a cada 1 minuto)
   - Publicação de mensagens
   - Recebimento de dados
   - Validação de payload

4. **Testes de Banco**
   - Conexão com banco (a cada 5 minutos)
   - Queries básicas
   - Performance
   - Integridade

5. **Testes de ML**
   - Modelo de ML (a cada 15 minutos)
   - Predições
   - Latência
   - Precisão

6. **Grupos de Testes**
   - Grupo do Dashboard
   - Grupo do Backend
   - Agrupamento lógico
   - Execução coordenada

## Contributor Insights

A configuração do Contributor Insights (`contributor-insights.json`) inclui:

1. **Regras de Contribuidores**
   - API (requisições por usuário)
   - IoT (mensagens por dispositivo)
   - Banco de dados (queries por usuário)
   - ML (predições por usuário)
   - Erros (erros por usuário)
   - Performance (latência por usuário)
   - Segurança (eventos por usuário)
   - Custos (gastos por usuário)

2. **Insights por Área**
   - API (requisições, erros, performance)
   - IoT (dispositivos, erros)
   - Banco de dados (queries, performance)
   - ML (predições, performance)
   - Segurança (eventos, erros)
   - Custos (gastos)

3. **Análises**
   - Padrões de uso
   - Problemas recorrentes
   - Performance por usuário
   - Custos por usuário
   - Segurança por usuário

4. **Métricas**
   - Contagem de eventos
   - Média de duração
   - Soma de valores
   - Distribuição de uso

## Anomaly Detection

A configuração do Anomaly Detection (`anomaly-detection.json`) inclui:

1. **Detectores de Anomalias**
   - API (latência anômala)
   - IoT (conexões anômalas)
   - Banco de dados (performance anômala)
   - ML (latência anômala)
   - Custos (gastos anômalos)
   - Erros (taxa anômala)
   - Sistema (uso de memória anômalo)
   - Rede (tráfego anômalo)

2. **Configuração Global**
   - Período de treinamento: 7 dias
   - Período de avaliação: 1 dia
   - Sensibilidade: 0.8
   - Sazonalidade: Diária
   - Agregação: Média
   - Dados ausentes: Breaking

3. **Métricas Monitoradas**
   - Latência da API
   - Conexões IoT
   - CPU do banco
   - Latência do ML
   - Custos
   - Taxa de erros
   - Uso de memória
   - Tráfego de rede

4. **Alertas**
   - Notificações SNS
   - Ações de recuperação
   - Thresholds dinâmicos
   - Períodos de avaliação

## Service Quotas

A configuração do Service Quotas (`service-quotas.json`) inclui:

1. **Quotas Monitoradas**
   - Lambda (execuções concorrentes)
   - RDS (instâncias por conta)
   - IoT (número máximo de things)
   - SageMaker (número máximo de endpoints)
   - CloudFront (número máximo de distribuições)
   - S3 (número máximo de buckets)
   - DynamoDB (número máximo de tabelas)
   - API Gateway (número máximo de APIs)

2. **Configuração de Alertas**
   - Períodos de avaliação: 2
   - Período: 300 segundos
   - Estatística: Máximo
   - Tratamento de dados ausentes: Breaching

3. **Solicitações de Aumento**
   - Solicitação automática habilitada
   - Template de solicitação
   - Razão padrão
   - Valor desejado dinâmico

4. **Thresholds**
   - Lambda: 80%
   - RDS: 75%
   - IoT: 80%
   - SageMaker: 70%
   - CloudFront: 75%
   - S3: 80%
   - DynamoDB: 75%
   - API Gateway: 80%

## Composite Alarms

A configuração do Composite Alarms (`composite-alarms.json`) inclui:

1. **Alertas Compostos**
   - Alta carga do sistema (CPU, memória, rede)
   - Degradação da API (latência, erros, disponibilidade)
   - Problemas no banco de dados (CPU, conexões, latência)
   - Problemas IoT (conexão, mensagens, latência)
   - Problemas de ML (latência, erros, precisão)
   - Problemas de segurança (WAF, acesso, grupos)
   - Problemas de custo (diário, recursos, anomalias)
   - Problemas de disponibilidade (health check, endpoints, região)

2. **Configuração Global**
   - Ações habilitadas
   - Períodos de avaliação: 2
   - Datapoints para alarme: 2
   - Threshold: 1
   - Operador de comparação: GreaterThanThreshold
   - Tratamento de dados ausentes: Breaching

3. **Ações Automáticas**
   - Recuperação de instâncias
   - Reinicialização de serviços
   - Investigação de segurança
   - Análise de custos
   - Failover de DNS

4. **Notificações**
   - Alertas gerais
   - Alertas de segurança
   - Alertas de custo
   - Ações de recuperação

## Metric Math

A configuração do Metric Math (`metric-math.json`) inclui:

1. **Expressões Matemáticas**
   - Taxa de sucesso da API
   - Eficiência do sistema
   - Confiabilidade IoT
   - Performance do ML
   - Eficiência de custos
   - Eficiência do banco de dados
   - Eficiência da rede
   - Saúde geral do sistema

2. **Configuração Global**
   - Período: 300 segundos
   - Períodos de avaliação: 2
   - Datapoints para alarme: 2
   - Threshold: 80
   - Operador de comparação: LessThanThreshold
   - Tratamento de dados ausentes: Missing

3. **Métricas Base**
   - API (erros, requisições)
   - Sistema (CPU, memória, disco)
   - IoT (conexões, mensagens)
   - ML (precisão, latência)
   - Custos (real, estimado)
   - Banco (CPU, conexões, armazenamento)
   - Rede (pacotes de erro, total)

4. **Cálculos**
   - Porcentagens
   - Médias
   - Somas
   - Combinações
   - Normalizações

## Metric Streams

A configuração do Metric Streams (`metric-streams.json`) inclui:

1. **Streams de Métricas**
   - API (requisições, erros, latência)
   - Sistema (CPU, memória, disco)
   - IoT (clientes, mensagens, erros)
   - ML (latência, precisão, predições)
   - Banco de dados (CPU, conexões, armazenamento)
   - Rede (pacotes, erros, latência)
   - Custos (real, estimado, recursos)
   - Segurança (bloqueios, acesso, mudanças)

2. **Configuração Global**
   - Formato de saída: JSON
   - Stream de entrega: Kinesis Firehose
   - Role IAM: farmtech-metric-stream-role
   - Filtros de inclusão: FarmTech/*
   - Filtros de exclusão: Nenhum

3. **Configurações de Estatísticas**
   - Média
   - Soma
   - Mínimo
   - Máximo
   - Aplicado a todas as métricas

4. **Destinos**
   - Kinesis Firehose
   - S3
   - Redshift
   - OpenSearch
   - Athena

## Como Usar

1. **Visualização do Dashboard**
   ```bash
   aws cloudwatch get-dashboard --dashboard-name FarmTechDashboard
   ```

2. **Configuração de Alertas**
   ```bash
   aws cloudwatch put-metric-alarm --cli-input-json file://alarms.json
   ```

3. **Configuração de Logs**
   ```bash
   aws logs create-log-group --log-group-name /farmtech/application
   aws logs create-log-stream --log-group-name /farmtech/application --log-stream-name dashboard-1
   ```

4. **Execução de Queries**
   ```bash
   aws logs start-query --log-group-name /farmtech/application --query-string "fields @timestamp, @message | filter @message like /ERROR/"
   ```

5. **Configuração de Eventos**
   ```bash
   aws events put-rule --cli-input-json file://events.json
   aws events put-targets --rule farmtech-daily-backup --targets file://targets.json
   ```

6. **Configuração de Testes Sintéticos**
   ```bash
   aws synthetics create-canary --cli-input-json file://synthetics.json
   aws synthetics create-group --cli-input-json file://synthetics.json
   ```

7. **Configuração de Contributor Insights**
   ```bash
   aws cloudwatch put-insight-rule --cli-input-json file://contributor-insights.json
   ```

8. **Configuração de Anomaly Detection**
   ```bash
   aws cloudwatch put-anomaly-detector --cli-input-json file://anomaly-detection.json
   ```

9. **Configuração de Service Quotas**
   ```bash
   aws service-quotas put-service-quota --cli-input-json file://service-quotas.json
   ```

10. **Configuração de Composite Alarms**
    ```bash
    aws cloudwatch put-composite-alarm --cli-input-json file://composite-alarms.json
    ```

11. **Configuração de Metric Math**
    ```bash
    aws cloudwatch put-metric-math --cli-input-json file://metric-math.json
    ```

12. **Configuração de Metric Streams**
    ```bash
    aws cloudwatch put-metric-stream --cli-input-json file://metric-streams.json
    ```

## Manutenção

1. **Atualização de Alertas**
   - Revisar thresholds mensalmente
   - Ajustar períodos de avaliação
   - Atualizar ações de alerta

2. **Limpeza de Logs**
   - Manter retenção de 30 dias
   - Arquivar logs importantes
   - Monitorar custos de armazenamento

3. **Otimização de Queries**
   - Revisar performance
   - Ajustar filtros
   - Otimizar parse patterns

4. **Atualização de Dashboards**
   - Adicionar novas métricas
   - Remover métricas obsoletas
   - Ajustar layouts

5. **Gerenciamento de Eventos**
   - Revisar regras periodicamente
   - Ajustar agendamentos
   - Monitorar falhas de eventos

6. **Manutenção de Testes**
   - Atualizar scripts
   - Ajustar thresholds
   - Revisar cobertura

7. **Análise de Contribuidores**
   - Revisar regras
   - Ajustar agregações
   - Atualizar insights

8. **Análise de Anomalias**
   - Ajustar sensibilidade
   - Revisar thresholds
   - Atualizar períodos
   - Calibrar detectores

9. **Gerenciamento de Quotas**
   - Monitorar utilização
   - Ajustar thresholds
   - Revisar solicitações
   - Otimizar recursos

10. **Gerenciamento de Alertas Compostos**
    - Revisar regras
    - Ajustar thresholds
    - Atualizar ações
    - Otimizar notificações

11. **Gerenciamento de Métricas**
    - Revisar expressões
    - Ajustar períodos
    - Otimizar cálculos
    - Calibrar thresholds

12. **Gerenciamento de Streams**
    - Monitorar throughput
    - Ajustar filtros
    - Otimizar formato
    - Verificar destinos

## Próximos Passos

1. **Melhorias Planejadas**
   - Adicionar mais métricas personalizadas
   - Implementar dashboards específicos por módulo
   - Criar alertas baseados em ML
   - Expandir cobertura de eventos
   - Adicionar mais testes sintéticos
   - Expandir análise de contribuidores
   - Refinar detecção de anomalias
   - Implementar ML para detecção
   - Expandir métricas monitoradas
   - Otimizar quotas
   - Implementar previsão de uso
   - Expandir monitoramento
   - Refinar alertas compostos
   - Implementar ações automáticas
   - Expandir cobertura de alertas
   - Refinar métricas compostas
   - Implementar previsões
   - Expandir cálculos
   - Expandir streams
   - Otimizar formato
   - Adicionar destinos

2. **Integrações**
   - Conectar com sistemas de ticket
   - Integrar com ferramentas de análise
   - Automatizar respostas a alertas
   - Adicionar mais destinos de eventos
   - Integrar com ferramentas de teste
   - Conectar com sistemas de BI
   - Integrar com sistemas de ML
   - Conectar com ferramentas de análise
   - Integrar com sistemas de orçamento
   - Conectar com ferramentas de planejamento
   - Integrar com sistemas de incidentes
   - Conectar com ferramentas de automação
   - Integrar com sistemas de BI
   - Conectar com ferramentas de análise
   - Integrar com data lakes
   - Conectar com ferramentas de análise

3. **Documentação**
   - Atualizar thresholds
   - Documentar novos alertas
   - Criar guias de troubleshooting
   - Documentar fluxos de eventos
   - Documentar casos de teste
   - Documentar padrões de uso
   - Documentar padrões anômalos
   - Documentar procedimentos de resposta
   - Documentar limites de serviço
   - Documentar procedimentos de aumento
   - Documentar regras de alerta
   - Documentar fórmulas
   - Documentar interpretações
   - Documentar streams
   - Documentar destinos 