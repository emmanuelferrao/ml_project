import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def render_page(X_scaled, y, feature_names):
    """Renderiza a página de Aprendizagem Supervisionada."""
    
    st.title("🎯 Aprendizagem Supervisionada: Random Forest")
    st.markdown("""
    Nesta seção, treinamos um modelo de **Random Forest** para classificar tumores como malignos ou benignos. 
    """)

    # --- Hiperparâmetros na barra lateral ---
    st.sidebar.subheader("Parâmetros do Random Forest")
    n_estimators = st.sidebar.slider("Número de Árvores (n_estimators)", 50, 500, 100, 50)
    max_depth = st.sidebar.slider("Profundidade Máxima (max_depth)", 2, 20, 10, 2)
    test_size = st.sidebar.slider("Proporção dos Dados de Teste", 0.1, 0.5, 0.3, 0.05)
    
    # --- Treinamento e Avaliação ---
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=test_size, random_state=42)
    
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    # --- Exibição dos Resultados ---
    st.subheader("Resultados do Modelo")
    st.markdown(f"**Acurácia no conjunto de teste:** `{accuracy:.4f}`")
    
    st.text("Relatório de Classificação:")
    st.text(classification_report(y_test, y_pred))
    
    # Matriz de Confusão
    st.subheader("Matriz de Confusão")
    cm = confusion_matrix(y_test, y_pred, labels=['Maligno', 'Benigno'])
    fig_cm = px.imshow(cm, text_auto=True, aspect="auto",
                       labels=dict(x="Diagnóstico Previsto", y="Diagnóstico Real"),
                       x=['Maligno', 'Benigno'],
                       y=['Maligno', 'Benigno'],
                       color_continuous_scale='Blues')
    st.plotly_chart(fig_cm, use_container_width=True)

    # Importância das Features
    st.subheader("Importância das Características (Feature Importances)")
    importances = pd.DataFrame({
        'feature': feature_names,
        'importance': model.feature_importances_
    }).sort_values(by='importance', ascending=False)
    
    fig_imp = px.bar(importances.head(15), x='importance', y='feature', orientation='h',
                     title="Top 15 Características Mais Importantes")
    st.plotly_chart(fig_imp, use_container_width=True)