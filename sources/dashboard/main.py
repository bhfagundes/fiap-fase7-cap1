import streamlit as st
import sys
import os
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import json
from datetime import datetime, timedelta
import cv2
import numpy as np
from PIL import Image
import io

# Adiciona os diretórios dos módulos ao path
sys.path.append(str(Path(__file__).parent.parent))

# Configuração da página
st.set_page_config(
    page_title="FarmTech - Dashboard Integrado",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Funções auxiliares
def load_data():
    """Carrega dados de exemplo para demonstração"""
    dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
    data = {
        'data': dates,
        'temperatura': np.random.normal(25, 5, len(dates)),
        'umidade': np.random.normal(65, 10, len(dates)),
        'precipitacao': np.random.exponential(5, len(dates))
    }
    return pd.DataFrame(data)

def create_metric_card(title, value, delta=None, delta_color="normal"):
    """Cria um card de métrica estilizado"""
    st.metric(
        label=title,
        value=value,
        delta=delta,
        delta_color=delta_color
    )

def plot_temperature(df):
    """Plota gráfico de temperatura"""
    fig = px.line(df, x='data', y='temperatura',
                  title='Temperatura ao Longo do Tempo',
                  labels={'data': 'Data', 'temperatura': 'Temperatura (°C)'})
    fig.update_layout(height=400)
    return fig

def plot_humidity(df):
    """Plota gráfico de umidade"""
    fig = px.line(df, x='data', y='umidade',
                  title='Umidade ao Longo do Tempo',
                  labels={'data': 'Data', 'umidade': 'Umidade (%)'})
    fig.update_layout(height=400)
    return fig

def plot_precipitation(df):
    """Plota gráfico de precipitação"""
    fig = px.bar(df, x='data', y='precipitacao',
                 title='Precipitação ao Longo do Tempo',
                 labels={'data': 'Data', 'precipitacao': 'Precipitação (mm)'})
    fig.update_layout(height=400)
    return fig

# Título principal
st.title("🌾 FarmTech - Sistema Integrado de Gestão para Agronegócio")

# Sidebar com navegação
st.sidebar.title("Navegação")
page = st.sidebar.radio(
    "Selecione o módulo:",
    ["Visão Geral", "Dados Meteorológicos", "IoT e Automação", 
     "Análise de Dados", "Visão Computacional", "Configurações"]
)

# Carrega dados de exemplo
df = load_data()

# Conteúdo principal baseado na seleção
if page == "Visão Geral":
    st.header("Visão Geral do Sistema")
    st.write("""
    Bem-vindo ao sistema integrado FarmTech. Este dashboard combina todas as funcionalidades
    desenvolvidas nas fases anteriores em uma interface unificada.
    """)
    
    # Cards com métricas principais
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        create_metric_card("Temperatura Atual", "25°C", "2°C", "normal")
    with col2:
        create_metric_card("Umidade do Solo", "65%", "-5%", "inverse")
    with col3:
        create_metric_card("Status da Irrigação", "Ativo", "", "normal")
    with col4:
        create_metric_card("Previsão de Rendimento", "+15%", "15%", "normal")
    
    # Gráficos principais
    st.subheader("Tendências Recentes")
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(plot_temperature(df), use_container_width=True)
    with col2:
        st.plotly_chart(plot_humidity(df), use_container_width=True)
    
    # Alertas e Notificações
    st.subheader("Alertas e Notificações")
    alerts = [
        {"tipo": "⚠️ Alerta", "mensagem": "Umidade do solo abaixo do ideal", "tempo": "5 min atrás"},
        {"tipo": "ℹ️ Info", "mensagem": "Sistema de irrigação ativado", "tempo": "15 min atrás"},
        {"tipo": "✅ Sucesso", "mensagem": "Backup concluído com sucesso", "tempo": "1 hora atrás"}
    ]
    
    for alert in alerts:
        st.info(f"{alert['tipo']} - {alert['mensagem']} ({alert['tempo']})")

elif page == "Dados Meteorológicos":
    st.header("Dados Meteorológicos")
    
    # Filtros
    col1, col2 = st.columns(2)
    with col1:
        data_inicio = st.date_input("Data Inicial", datetime.now() - timedelta(days=30))
    with col2:
        data_fim = st.date_input("Data Final", datetime.now())
    
    # Gráficos
    st.plotly_chart(plot_temperature(df), use_container_width=True)
    st.plotly_chart(plot_humidity(df), use_container_width=True)
    st.plotly_chart(plot_precipitation(df), use_container_width=True)
    
    # Tabela de dados
    st.subheader("Dados Detalhados")
    st.dataframe(df)

elif page == "IoT e Automação":
    st.header("IoT e Automação")
    
    # Status dos sensores
    st.subheader("Status dos Sensores")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Sensor de Temperatura", "Online", "Ativo")
    with col2:
        st.metric("Sensor de Umidade", "Online", "Ativo")
    with col3:
        st.metric("Sensor de pH", "Online", "Ativo")
    
    # Controle de irrigação
    st.subheader("Controle de Irrigação")
    if st.button("Ativar Irrigação"):
        st.success("Sistema de irrigação ativado!")
    if st.button("Desativar Irrigação"):
        st.warning("Sistema de irrigação desativado!")
    
    # Configurações
    st.subheader("Configurações")
    umidade_min = st.slider("Umidade Mínima (%)", 0, 100, 30)
    umidade_max = st.slider("Umidade Máxima (%)", 0, 100, 70)
    intervalo = st.slider("Intervalo de Verificação (min)", 1, 60, 15)

elif page == "Análise de Dados":
    st.header("Análise de Dados")
    
    # Previsão de rendimento
    st.subheader("Previsão de Rendimento")
    col1, col2 = st.columns(2)
    with col1:
        cultura = st.selectbox("Cultura", ["Arroz", "Dendezeiro"])
        area = st.number_input("Área (hectares)", 1, 1000, 100)
    with col2:
        temperatura = st.number_input("Temperatura Média (°C)", 0, 50, 25)
        umidade = st.number_input("Umidade Média (%)", 0, 100, 65)
    
    if st.button("Calcular Previsão"):
        st.success(f"Previsão de rendimento: {np.random.normal(100, 10):.1f} toneladas")

elif page == "Visão Computacional":
    st.header("Visão Computacional")
    
    # Upload de imagem
    uploaded_file = st.file_uploader("Escolha uma imagem", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Imagem carregada', use_column_width=True)
        
        if st.button("Analisar Imagem"):
            st.success("Análise concluída!")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Classificação:")
                st.write("- Banana: 95% de confiança")
                st.write("- Estágio: Maduro")
            with col2:
                st.write("Recomendações:")
                st.write("- Pronto para colheita")
                st.write("- Bom estado de conservação")

elif page == "Configurações":
    st.header("Configurações")
    
    # Configurações gerais
    st.subheader("Configurações Gerais")
    api_key = st.text_input("API Key", type="password")
    ambiente = st.selectbox("Ambiente", ["Desenvolvimento", "Produção"])
    
    # Configurações de notificação
    st.subheader("Configurações de Notificação")
    email = st.text_input("Email para notificações")
    notificacoes = st.multiselect(
        "Tipos de notificação",
        ["Alertas de umidade", "Status de irrigação", "Previsão de rendimento"]
    )
    
    # Salvar configurações
    if st.button("Salvar Configurações"):
        st.success("Configurações salvas com sucesso!")

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido por Grupo 12 - FIAP") 