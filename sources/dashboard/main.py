import streamlit as st
import sys
import os
from pathlib import Path

# Adiciona os diretórios dos módulos ao path
sys.path.append(str(Path(__file__).parent.parent))

# Configuração da página
st.set_page_config(
    page_title="FarmTech - Dashboard Integrado",
    page_icon="🌾",
    layout="wide"
)

# Título principal
st.title("🌾 FarmTech - Sistema Integrado de Gestão para Agronegócio")

# Sidebar com navegação
st.sidebar.title("Navegação")
page = st.sidebar.radio(
    "Selecione o módulo:",
    ["Visão Geral", "Dados Meteorológicos", "IoT e Automação", 
     "Análise de Dados", "Visão Computacional", "Configurações"]
)

# Conteúdo principal baseado na seleção
if page == "Visão Geral":
    st.header("Visão Geral do Sistema")
    st.write("""
    Bem-vindo ao sistema integrado FarmTech. Este dashboard combina todas as funcionalidades
    desenvolvidas nas fases anteriores em uma interface unificada.
    """)
    
    # Cards com métricas principais
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Temperatura Atual", value="25°C", delta="2°C")
    with col2:
        st.metric(label="Umidade do Solo", value="65%", delta="-5%")
    with col3:
        st.metric(label="Status da Irrigação", value="Ativo", delta="")

elif page == "Dados Meteorológicos":
    st.header("Dados Meteorológicos")
    st.write("Módulo em desenvolvimento...")

elif page == "IoT e Automação":
    st.header("IoT e Automação")
    st.write("Módulo em desenvolvimento...")

elif page == "Análise de Dados":
    st.header("Análise de Dados")
    st.write("Módulo em desenvolvimento...")

elif page == "Visão Computacional":
    st.header("Visão Computacional")
    st.write("Módulo em desenvolvimento...")

elif page == "Configurações":
    st.header("Configurações")
    st.write("Módulo em desenvolvimento...")

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido por Grupo 12 - FIAP") 