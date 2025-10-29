import streamlit as st
import plotly.express as px

def render_page(df, feature_names):
    """Renderiza a página de Análise Exploratória de Dados."""
    
    st.title("🔬 Análise Exploratória de Dados (EDA)")
    
    st.subheader("Estatísticas Descritivas")
    st.write(df.describe())
    
    # Gráfico 1: Distribuição do Diagnóstico
    st.subheader("Distribuição do Diagnóstico (Alvo)")
    fig_dist = px.histogram(df, x='diagnostico', color='diagnostico',
                            title="Contagem de Diagnósticos (Benigno vs. Maligno)",
                            color_discrete_map={'Maligno': '#FF6347', 'Benigno': '#4682B4'})
    st.plotly_chart(fig_dist, use_container_width=True)
    
    # Gráfico 2: Mapa de Calor de Correlação
    st.subheader("Mapa de Calor de Correlação")
    st.markdown("Analisando a correlação entre as principais características ('mean')")
    mean_cols = [col for col in df.columns if 'mean' in col]
    corr = df[mean_cols].corr()
    
    fig_corr = px.imshow(corr, text_auto=True, aspect="auto", 
                         color_continuous_scale='RdBu_r',
                         title="Correlação entre Características 'Mean'")
    st.plotly_chart(fig_corr, use_container_width=True)
    
    # Gráfico 3: Scatter plot interativo
    st.subheader("Distribuição de Características por Diagnóstico")
    feature_1 = st.selectbox("Selecione a Característica 1 (Eixo X):", feature_names, index=0)
    feature_2 = st.selectbox("Selecione a Característica 2 (Eixo Y):", feature_names, index=1)
    
    fig_scatter = px.scatter(df, x=feature_1, y=feature_2, color='diagnostico',
                             title=f"{feature_1} vs. {feature_2} por Diagnóstico",
                             color_discrete_map={'Maligno': '#FF6347', 'Benigno': '#4682B4'})
    st.plotly_chart(fig_scatter, use_container_width=True)