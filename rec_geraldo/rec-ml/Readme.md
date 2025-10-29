# 🩺 Projeto de Machine Learning Aplicado à Saúde

Este projeto é referente a recuperação da disciplina de Machine Learning, com o objetivo de construir uma aplicação web interativa usando Streamlit para analisar o dataset de Câncer de Mama (Wisconsin).

## 🚀 Links do Projeto

* **Link da Aplicação (Streamlit Cloud):** `[INSIRA AQUI O LINK DO SEU APP PUBLICADO]`
* **Link do Vídeo (YouTube/Drive):** `[INSIRA AQUI O LINK DA SUA APRESENTAÇÃO]`

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

## 3. Como Executar Localmente

Para executar este projeto em sua máquina local, siga os passos:

1.  **Clone o repositório:**
    ```bash
    git clone [URL-DO-SEU-REPOSITORIO-GITHUB]
    cd [NOME-DA-PASTA-DO-PROJETO]
    ```

2.  **Crie um ambiente virtual (Recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação Streamlit:**
    ```bash
    streamlit run app.py
    ```

## 4. Conclusões e Aprendizados

*(Esta é a parte mais importante para sua avaliação!)*

* **[ESCREVA AQUI O QUE VOCÊ APRENDEU]**
* (Ex: O modelo supervisionado atingiu uma acurácia de X%, sendo as features Y e Z as mais importantes...)
* (Ex: O K-Means com k=2 conseguiu criar grupos muito similares aos diagnósticos reais, mostrando que...)
* (Ex: A maior dificuldade foi...)