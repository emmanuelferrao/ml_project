import streamlit as st
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

# Importa os módulos de cada página
import page_intro
import page_eda
import page_supervised
import page_unsupervised

# --- Configuração da Página ---
# Deve ser o primeiro comando Streamlit
st.set_page_config(
    page_title="ML na Saúde: Análise de Câncer de Mama",
    page_icon="🩺",
    layout="wide"
)

# --- Carregamento e Preparação dos Dados ---
# @st.cache_data garante que os dados sejam carregados apenas uma vez.
@st.cache_data
def carregar_dados():
    """Carrega, mapeia e escala o dataset de Câncer de Mama."""
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['diagnostico'] = data.target
    df['diagnostico'] = df['diagnostico'].map({0: 'Maligno', 1: 'Benigno'})
    
    # Prepara dados para modelos
    X = df[data.feature_names]
    y = df['diagnostico']
    
    # Escala os dados (importante para PCA e K-Means)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return df, data.feature_names, X, y, X_scaled

# Carrega os dados na inicialização
df, feature_names, X, y, X_scaled = carregar_dados()


# --- Barra Lateral (Navegação) ---
st.sidebar.title("Navegação 🧭")
st.sidebar.markdown("Atividade de Recuperação - Machine Learning")

# Dicionário para mapear nomes de página para funções de renderização
paginas = {
    "Introdução": page_intro,
    "Análise Exploratória (EDA)": page_eda,
    "Modelo Supervisionado (Classificação)": page_supervised,
    "Modelo Não Supervisionado (Clusterização)": page_unsupervised
}

# Cria o seletor de página
pagina_selecionada = st.sidebar.radio("Selecione uma seção:", paginas.keys())

st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido por: ~Emmanuel Ferrão")


# --- Renderização da Página ---
# Chama a função 'render_page' do módulo selecionado
if pagina_selecionada == "Introdução":
    page_intro.render_page(df, X)
    
elif pagina_selecionada == "Análise Exploratória (EDA)":
    page_eda.render_page(df, feature_names)

elif pagina_selecionada == "Modelo Supervisionado (Classificação)":
    page_supervised.render_page(X_scaled, y, feature_names)

elif pagina_selecionada == "Modelo Não Supervisionado (Clusterização)":
    page_unsupervised.render_page(X_scaled, y)