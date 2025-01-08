#CONTINUANDO A EXPLICAÇÃO DO PROJETO 1 - Projeto de análise de dados de livros e resenhas de clientes:
#O código fornecido é um script em Python que utiliza as bibliotecas Streamlit, Pandas e Plotly para criar uma interface web interativa que exibe informações sobre livros e permite a visualização de gráficos. Vamos detalhar cada parte do código:
#Primeiramente, as bibliotecas streamlit, pandas e plotly.express são importadas. A função st.set_page_config(layout="wide") é usada para configurar o layout da página para ser mais largo, proporcionando uma melhor visualização dos dados.
#Os dados são carregados a partir de dois arquivos CSV: "customer reviews.csv" e "Top-100 Trending Books.csv". O primeiro contém avaliações de clientes, enquanto o segundo contém informações sobre os 100 livros mais populares. Esses dados são lidos em dataframes df_reviews e df_top100_books, respectivamente.
#Os valores máximo e mínimo dos preços dos livros são extraídos do dataframe df_top100_books e armazenados nas variáveis price_max e price_min. Um controle deslizante (slider) é adicionado na barra lateral usando st.sidebar.slider, permitindo que o usuário selecione um intervalo de preços. O valor máximo do slider é definido como price_max.
#O dataframe df_top100_books é filtrado para incluir apenas os livros cujo preço é menor ou igual ao valor selecionado no slider. O dataframe resultante é armazenado em df_books e exibido na interface.
#Dois gráficos são criados usando a biblioteca Plotly Express (px). O primeiro gráfico (fig) é um gráfico de barras que mostra a contagem de publicações por ano, enquanto o segundo gráfico (fig2) é um histograma que mostra a distribuição dos preços dos livros.
#Duas colunas são criadas usando st.columns(2), e os gráficos são exibidos nessas colunas usando col1.plotly_chart(fig) e col2.plotly_chart(fig2).
#Este script cria uma interface interativa que permite aos usuários explorar os livros populares com base no preço e visualizar gráficos que mostram a distribuição dos anos de publicação e dos preços dos livros.

import streamlit as st   #importação da biblioteca streamlit
import pandas as pd      #importação da biblioteca pandas
import plotly.express as px      #importação da biblioteca plotly

st.set_page_config(layout="wide")     #configuração de largura de tela

df_reviews = pd.read_csv("datasets/customer reviews.csv")  #extração de tabela exel 
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max) #slider
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books

fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
