import streamlit as st

def render_page(df, X):
    """Renderiza a página de introdução."""
    
    st.title("🩺 Análise de Machine Learning Aplicada à Saúde")
    st.header("Dataset: Câncer de Mama (Wisconsin)")
    
    st.markdown("""
    Bem-vindo a esta aplicação interativa! O objetivo deste projeto é demonstrar a aplicação de técnicas de 
    Machine Learning (Aprendizagem Supervisionada e Não Supervisionada) em um conjunto de dados real da área da saúde.

    O dataset utilizado é o **Breast Cancer Wisconsin (Diagnostic)**, disponível publicamente. 
    Ele contém características computadas a partir de imagens digitalizadas de biópsias de massa mamária.
    
    **O desafio é:**
    1.  **Classificar** tumores como **'Maligno'** ou **'Benigno'** (Supervisionado).
    2.  **Agrupar** os tumores com base em suas características, sem saber o diagnóstico (Não Supervisionado).
    
    Use o menu na barra lateral para navegar pelas diferentes seções do projeto.
    """)
    
    st.subheader("Visualização dos Dados")
    st.dataframe(df.head())
    
    st.subheader("Descrição das Features (Características)")
    st.markdown(f"""
    O dataset possui {X.shape[1]} características numéricas. Alguns exemplos:
    - `mean radius` (raio médio)
    - `mean texture` (textura média)
    - `mean perimeter` (perímetro médio)
    - `mean area` (área média)
    - ... e suas variações (erro padrão e 'pior' valor).
    """)