#DESCRIÇÃO DO PROJETO 1 - Projeto de análise de dados de livros e reviews de clientes
#O código fornecido é um script em Python que utiliza a biblioteca Streamlit para criar uma aplicação web interativa que exibe informações sobre livros e suas avaliações. A aplicação lê dados de dois arquivos CSV: um contendo avaliações de clientes e outro com uma lista dos 100 livros mais populares.
#Primeiramente, o script importa as bibliotecas necessárias: streamlit para a interface web e pandas para manipulação de dados. Em seguida, configura a página para um layout amplo usando st.set_page_config(layout="wide")
#Os dados são carregados a partir dos arquivos CSV usando pd.read_csv(). O arquivo "customer reviews.csv" contém as avaliações dos clientes, enquanto "Top-100 Trending Books.csv" contém informações sobre os livros mais populares. A lista de títulos de livros únicos é extraída e apresentada em um menu de seleção na barra lateral da aplicação usando st.sidebar.selectbox().
#Com base no livro selecionado pelo usuário, o script filtra os dados para obter informações detalhadas sobre o livro e suas avaliações. As informações do livro, como título, gênero, preço, avaliação e ano de publicação, são extraídas e exibidas na interface principal da aplicação usando st.title(), st.subheader() e st.columns() para organizar os dados em três colunas.
#Finalmente, o script exibe as avaliações dos clientes para o livro selecionado. Para cada avaliação, uma mensagem de chat é criada usando st.chat_message(), onde o nome do cliente e o conteúdo da avaliação são exibidos.
#Este código cria uma interface de usuário interativa e informativa que permite aos usuários explorar informações sobre livros populares e ler avaliações de outros clientes de forma organizada e visualmente agradável.

import streamlit as st
import pandas as pd 

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer reviews.csv")  
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Books", books)

df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)
col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

st.divider()

for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])

