#EXPLICAÇÃO DO PROJETO 1 - Projeto de análise de dados de livros e resenhas de clientes:
#O código fornecido é um script em Python que utiliza a biblioteca Streamlit para criar uma interface web interativa para exibir informações sobre livros e suas avaliações. Vamos detalhar cada parte do código:
#Primeiramente, as bibliotecas streamlit e pandas são importadas. A função st.set_page_config(layout="wide") é usada para configurar o layout da página para ser mais largo, proporcionando uma melhor visualização dos dados.
#Os dados são carregados a partir de dois arquivos CSV: "customer reviews.csv" e "Top-100 Trending Books.csv". O primeiro contém avaliações de clientes, enquanto o segundo contém informações sobre os 100 livros mais populares. Esses dados são lidos em dataframes df_reviews e df_top100_books, respectivamente.
#A lista de títulos de livros únicos é extraída do dataframe df_top100_books e apresentada em um menu de seleção na barra lateral usando st.sidebar.selectbox. O usuário pode selecionar um livro a partir dessa lista.
#Com base no livro selecionado, o dataframe df_top100_books é filtrado para obter as informações específicas desse livro, armazenadas em df_book. Da mesma forma, df_reviews é filtrado para obter as avaliações relacionadas ao livro selecionado, armazenadas em df_reviews_f.
#As informações do livro, como título, gênero, preço, classificação e ano de publicação, são extraídas do dataframe df_book e exibidas na interface usando st.title e st.subheader para o título e gênero, respectivamente. Três colunas são criadas usando st.columns(3) para exibir o preço, a classificação e o ano de publicação do livro.
#Uma linha divisória é adicionada com st.divider() para separar as informações do livro das avaliações dos clientes.
#Finalmente, um loop percorre as avaliações filtradas em df_reviews_f. Para cada avaliação, uma mensagem de chat é criada usando st.chat_message, onde o nome do avaliador (row[4]) é exibido como remetente. O título da avaliação (row[2]) é exibido em negrito, seguido pelo texto da avaliação (row[5]).
#Este script cria uma interface interativa e informativa para os usuários explorarem livros populares e lerem avaliações de outros clientes.

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