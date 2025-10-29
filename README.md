# ml_project
Este projeto é referente a recuperação da disciplina de Machine Learning, com o objetivo de construir uma aplicação web interativa usando Streamlit para analisar o dataset de Câncer de Mama (Wisconsin).

# Projeto de Machine Learning Aplicado à Saúde

## Link do Projeto

Link da Aplicação (Streamlit Cloud): `https://mlproject-rec.streamlit.app/`

---

## 1. Visão Geral

O objetivo é aplicar técnicas de aprendizagem supervisionada e não supervisionada para extrair insights do dataset de câncer de mama.

* **Dataset:** Breast Cancer Wisconsin (Diagnostic)
* **Técnicas:**
    * Análise Exploratória de Dados (EDA)
    * **Aprendizagem Supervisionada:** Classificação (com `RandomForestClassifier`)
    * **Aprendizagem Não Supervisionada:** Clusterização (com `KMeans`) e Redução de Dimensionalidade (com `PCA`)

### Fonte dos Dados

Para este projeto, o dataset foi carregado diretamente da biblioteca **Scikit-learn**, que o disponibiliza para fins educacionais.

* **Acesso no Código:** `from sklearn.datasets import load_breast_cancer`
* **Documentação (Sklearn):** [https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html)

A fonte original e acadêmica deste conjunto de dados é o **UCI Machine Learning Repository**.

* **Fonte Original (UCI):** [https://archive.ics.uci.edu/dataset/17/breast-cancer-wisconsin-diagnostic](https://archive.ics.uci.edu/dataset/17/breast-cancer-wisconsin-diagnostic)

---

## 2. Estrutura da Aplicação

A aplicação é dividida em quatro seções principais:

1.  **Introdução:** Apresenta o problema, o dataset e os objetivos do projeto.
2.  **Análise Exploratória (EDA):** Mostra estatísticas descritivas, a distribuição das classes (Maligno vs. Benigno) e a correlação entre as características.
3.  **Modelo Supervisionado:**
    * Treina um modelo `Random Forest` para prever o diagnóstico.
    * Permite ao usuário ajustar hiperparâmetros (como número de árvores e profundidade).
    * Exibe métricas de performance (Acurácia, Relatório de Classificação) e uma Matriz de Confusão.
    * Mostra a importância das características (`feature importances`).
4.  **Modelo Não Supervisionado:**
    * Utiliza `K-Means` para agrupar os dados sem conhecer o diagnóstico.
    * Utiliza `PCA` para reduzir as 30 características para 2 componentes principais, permitindo a visualização.
    * Compara os clusters encontrados pelo K-Means com os diagnósticos reais.

## 3. Conclusões e Aprendizados

   * Conclusões: Consegui treinar um modelo supervisionado (Random Forest) com uma acurácia alta.
     Mais importante, descobrimos quais características, como `worst concave points`, são as mais preditivas.
     E o modelo não supervisionado (K-Means) confirmou que os tumores malignos e benignos são, de fato, estruturalmente diferentes nos dados, a ponto de um algoritmo "cego" conseguir separá-los.

   * Aprendizados: Este projeto foi uma excelente prática do ciclo completo de ciência de dados: desde a carga e análise exploratória (EDA), passando pelo pré-processamento (como o StandardScaler), até o treinamento, avaliação (com Matriz de Confusão) e interpretação de      dois tipos diferentes de modelos. Utilizar o Streamlit também se mostrou incrível para criar uma interface interativa e profissional, permitindo que outras pessoas pudessem interagir com os modelos.
