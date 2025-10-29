import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def render_page(X_scaled, y):
    """Renderiza a página de Aprendizagem Não Supervisionada."""
    
    st.title("🔍 Aprendizagem Não Supervisionada: K-Means + PCA")
    st.markdown("""
    Aqui, usamos **K-Means** para agrupar os dados sem saber o diagnóstico. 
    Usamos **PCA (Análise de Componentes Principais)** para reduzir as 30 características 
    para apenas 2, permitindo a visualização em um gráfico 2D.
    """)

    # --- Hiperparâmetros na barra lateral ---
    st.sidebar.subheader("Parâmetros do K-Means")
    n_clusters = st.sidebar.slider("Número de Clusters (k)", 2, 10, 2, 1)

    # --- Modelagem (PCA e K-Means) ---
    # PCA para redução
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    pca_df = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
    
    # K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X_scaled)
    
    # Adiciona resultados ao DataFrame
    pca_df['cluster'] = clusters
    pca_df['diagnostico_real'] = y
    
    # --- Visualização dos Resultados ---
    st.subheader("Visualização dos Clusters vs. Diagnóstico Real")
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico 1: Clusters encontrados
        fig_kmeans = px.scatter(pca_df, x='PC1', y='PC2', color='cluster',
                                title=f"Clusters Encontrados pelo K-Means (k={n_clusters})",
                                color_continuous_scale='viridis')
        st.plotly_chart(fig_kmeans, use_container_width=True)
        st.markdown("**Interpretação:** Grupos que o K-Means criou.")

    with col2:
        # Gráfico 2: Diagnósticos reais
        fig_real = px.scatter(pca_df, x='PC1', y='PC2', color='diagnostico_real',
                              title="Diagnósticos Reais (para Comparação)",
                              color_discrete_map={'Maligno': '#FF6347', 'Benigno': '#4682B4'})
        st.plotly_chart(fig_real, use_container_width=True)
        st.markdown("**Interpretação:** Classes reais (Maligno/Benigno).")
    
    st.subheader("Conclusão da Clusterização")
    st.markdown(f"""
    Ao comparar os gráficos, vemos que o K-Means (com k={n_clusters}) 
    conseguiu (ou não) encontrar uma estrutura nos dados que se assemelha aos diagnósticos reais.
    """)