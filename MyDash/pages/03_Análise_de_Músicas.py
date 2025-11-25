import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data
def le_dados():
    return pd.read_csv("https://raw.githubusercontent.com/LucasAdolfo/Dashboard/refs/heads/main/MyDash/dados.csv")

st.title("🎼 Análise de Músicas")

try:
    df = le_dados();
except FileNotFoundError:
    st.error('Arquivo "dados.csv" não encontrado. Coloque o arquivo na mesma pasta do app ou ajuste o caminho.')
    st.stop()
except Exception as e:
    st.error(f"Erro ao ler 'dados.csv': {e}")
    st.stop()

# Filtro
pop_min = st.sidebar.slider("Popularidade mínima", 0, 100, 50)
df_filt = df[df["track_popularity"] >= pop_min]

# Gráfico — Duração x Popularidade
st.subheader("⏱️ Duração x Popularidade")

fig1 = px.scatter(
    df_filt,
    x="track_duration_min",
    y="track_popularity",
    title="Duração x Popularidade",
    labels={"track_duration_min": "Duração (min)", "track_popularity": "Popularidade"},
    hover_data=["track_name", "artist_name"]  
)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico — Top 10 músicas
st.subheader("🏆 Top 10 Músicas Mais Populares")

top10 = df.sort_values("track_popularity", ascending=False).head(10)

fig2 = px.bar(
    top10,
    x="track_popularity",
    y="track_name",
    orientation="h",
    labels={"track_popularity": "Popularidade", "track_name": "Música"},
    hover_data=["artist_name"]  
)
fig2.update_layout(yaxis={'categoryorder':'total ascending'})  
st.plotly_chart(fig2, use_container_width=True)




