import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#CSV
@st.cache_data
def le_dados():
    return pd.read_csv("https://raw.githubusercontent.com/LucasAdolfo/Dashboard/refs/heads/main/MyDash/dados.csv")
df = le_dados();

df["genre"] = df["artist_genres"].astype(str).str.split(",").str[0]

st.title("🎧 Análise por Gênero Musical")

generos = df["genre"].value_counts().head(15)

st.subheader("Frequência de Gêneros")

plt.figure(figsize=(8,5))
plt.bar(generos.index, generos.values, color="purple")
plt.xticks(rotation=45)
plt.ylabel("Quantidade")
st.pyplot(plt)

st.subheader("Popularidade por Gênero")
media = df.groupby("genre")["track_popularity"].mean().sort_values(ascending=False)

st.bar_chart(media.head(15))

