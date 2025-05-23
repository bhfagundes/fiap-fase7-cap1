import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import requests
import json
import logging
from typing import Dict, List, Optional
import boto3
from botocore.exceptions import ClientError

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuração da página
st.set_page_config(
    page_title="FarmTech Dashboard",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tema personalizado
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Funções de utilidade
@st.cache_data
def load_data() -> pd.DataFrame:
    """Carrega dados do S3 com cache."""
    try:
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket='farmtech-data', Key='crop_data.csv')
        return pd.read_csv(response['Body'])
    except ClientError as e:
        logger.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()

@st.cache_resource
def load_model():
    """Carrega modelo de ML com cache."""
    try:
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket='farmtech-models', Key='crop_model.pkl')
        return joblib.load(response['Body'])
    except ClientError as e:
        logger.error(f"Erro ao carregar modelo: {e}")
        return None

def get_weather_data() -> Dict:
    """Obtém dados meteorológicos da API."""
    try:
        response = requests.get('https://api.weather.com/data')
        return response.json()
    except Exception as e:
        logger.error(f"Erro ao obter dados meteorológicos: {e}")
        return {}

def analyze_crop_data(df: pd.DataFrame) -> tuple:
    """Realiza análise avançada dos dados."""
    stats = df.describe()
    corr = df.corr()
    fig = px.scatter_matrix(df)
    return stats, corr, fig

# Sidebar
with st.sidebar:
    st.title("🌾 FarmTech")
    st.image("assets/logo.png", width=100)
    
    # Navegação
    page = st.radio(
        "Navegação",
        ["Dashboard", "Análise", "IoT", "Configurações"]
    )
    
    # Filtros
    st.subheader("Filtros")
    date_range = st.date_input(
        "Período",
        value=(datetime.now() - timedelta(days=30), datetime.now())
    )
    
    crop_type = st.multiselect(
        "Tipo de Cultura",
        ["Soja", "Milho", "Café", "Cana"]
    )

# Página principal
if page == "Dashboard":
    st.title("Dashboard Principal")
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Área Total",
            "1.234 ha",
            "+5%"
        )
    
    with col2:
        st.metric(
            "Produção",
            "45.678 ton",
            "+3%"
        )
    
    with col3:
        st.metric(
            "Eficiência",
            "92%",
            "+2%"
        )
    
    with col4:
        st.metric(
            "Custos",
            "R$ 123.456",
            "-1%"
        )
    
    # Gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Produção por Cultura")
        fig = px.bar(
            x=["Soja", "Milho", "Café", "Cana"],
            y=[1000, 800, 600, 400],
            title="Produção (ton)"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Tendência de Produção")
        fig = px.line(
            x=pd.date_range(start="2023-01-01", periods=12, freq="M"),
            y=np.random.normal(1000, 100, 12),
            title="Produção Mensal"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Mapa
    st.subheader("Localização das Fazendas")
    map_data = pd.DataFrame({
        "lat": [-23.5505, -23.5506, -23.5507],
        "lon": [-46.6333, -46.6334, -46.6335],
        "name": ["Fazenda 1", "Fazenda 2", "Fazenda 3"]
    })
    st.map(map_data)

elif page == "Análise":
    st.title("Análise Avançada")
    
    # Carregar dados
    df = load_data()
    
    if not df.empty:
        # Análise estatística
        st.subheader("Estatísticas Descritivas")
        st.dataframe(df.describe())
        
        # Correlações
        st.subheader("Correlações")
        fig = px.imshow(df.corr())
        st.plotly_chart(fig, use_container_width=True)
        
        # Análise de séries temporais
        st.subheader("Análise Temporal")
        fig = px.line(df, x='date', y='production')
        st.plotly_chart(fig, use_container_width=True)

elif page == "IoT":
    st.title("Monitoramento IoT")
    
    # Dados dos sensores
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Temperatura")
        fig = px.line(
            x=pd.date_range(start="2023-01-01", periods=24, freq="H"),
            y=np.random.normal(25, 2, 24),
            title="Temperatura (°C)"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Umidade")
        fig = px.line(
            x=pd.date_range(start="2023-01-01", periods=24, freq="H"),
            y=np.random.normal(60, 5, 24),
            title="Umidade (%)"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Status dos dispositivos
    st.subheader("Status dos Dispositivos")
    devices = pd.DataFrame({
        "Dispositivo": ["Sensor 1", "Sensor 2", "Sensor 3"],
        "Status": ["Online", "Online", "Offline"],
        "Última Atualização": ["2 min atrás", "5 min atrás", "1 hora atrás"]
    })
    st.dataframe(devices)

else:  # Configurações
    st.title("Configurações")
    
    # Configurações do usuário
    st.subheader("Perfil")
    st.text_input("Nome")
    st.text_input("Email")
    st.selectbox("Idioma", ["Português", "English", "Español"])
    
    # Notificações
    st.subheader("Notificações")
    st.checkbox("Alertas de Produção")
    st.checkbox("Alertas de IoT")
    st.checkbox("Relatórios Diários")
    
    # Integrações
    st.subheader("Integrações")
    st.text_input("API Key Weather")
    st.text_input("API Key Market")
    
    if st.button("Salvar Configurações"):
        st.success("Configurações salvas com sucesso!")

# Footer
st.markdown("---")
st.markdown("FarmTech Dashboard v1.0 | Desenvolvido com ❤️") 