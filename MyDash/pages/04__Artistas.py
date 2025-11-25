import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎤 Análise de Artistas")


# LEITURA DO CSV
@st.cache_data
def le_dados():
    return pd.read_csv("https://raw.githubusercontent.com/LucasAdolfo/Dashboard/refs/heads/main/MyDash/dados.csv")

try:
    df = le_dados();
except FileNotFoundError:
    st.error('Arquivo "dados.csv" não encontrado. Coloque o arquivo na mesma pasta do app.')
    st.stop()
except Exception as e:
    st.error(f"Erro ao carregar CSV: {e}")
    st.stop()


# VALIDAR COLUNAS NECESSÁRIAS

required_cols = {
    "artist_name", 
    "artist_followers", 
    "artist_popularity"
}

missing = required_cols - set(df.columns)

if missing:
    st.error(
        "As seguintes colunas obrigatórias estão faltando no dataset: "
        + ", ".join(sorted(missing))
    )
    st.write("Colunas disponíveis:", list(df.columns))
    st.stop()


# FILTROS

artistas = df["artist_name"].dropna().unique()
select_art = st.sidebar.multiselect("Selecione artistas", artistas)

if len(select_art) > 0:
    df = df[df["artist_name"].isin(select_art)]

# Evitar erro se filtro zerar o DataFrame
if df.empty:
    st.warning("Nenhum dado disponível após aplicar os filtros.")
    st.stop()


# GRÁFICO: Seguidores x Popularidade

st.subheader("Popularidade do Artista x Seguidores")

fig = px.scatter(
    df,
    x="artist_followers",
    y="artist_popularity",
    color="artist_name",
    hover_name="artist_name",
    size="artist_popularity",
    title="Popularidade do Artista x Seguidores",
)

st.plotly_chart(fig, use_container_width=True)


# RANKING DE POPULARIDADE

st.subheader("Ranking de Artistas por Popularidade Média")

rank = (
    df.groupby("artist_name")["artist_popularity"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(rank.head(20))




