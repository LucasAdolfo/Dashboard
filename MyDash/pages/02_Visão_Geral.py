import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Visão Geral do Dataset")

# ===========================
# LEITURA DO CSV (ANTES DE TUDO)
# ===========================
try:
    df = pd.read_csv("dados.csv")
except FileNotFoundError:
    st.error('Arquivo "dados.csv" não encontrado. Coloque o arquivo na mesma pasta do app ou ajuste o caminho.')
    st.stop()
except Exception as e:
    st.error(f"Erro ao ler 'dados.csv': {e}")
    st.stop()

# ===========================
# VALIDAR COLUNAS
# ===========================
required_cols = {"artist_name", "track_name", "album_name", "track_popularity"}
missing = required_cols - set(df.columns)

if missing:
    st.error(f"Colunas faltando no arquivo: {', '.join(sorted(missing))}")
    st.write("Colunas disponíveis:", list(df.columns))
    st.stop()

# ===========================
# MÉTRICAS
# ===========================
col1, col2, col3 = st.columns(3)

col1.metric("🎤 Artistas Únicos", int(df["artist_name"].nunique()))
col2.metric("🎵 Músicas", int(df["track_name"].nunique()))
col3.metric("📅 Álbuns", int(df["album_name"].nunique()))

# ===========================
# GRÁFICO
# ===========================
st.subheader("Popularidade Média por Artista (Top 20)")

mean_pop = (
    df.groupby("artist_name", as_index=False)["track_popularity"]
      .mean()
      .sort_values(by="track_popularity", ascending=False)
      .head(20)
)

fig = px.bar(
    mean_pop,
    x="track_popularity",
    y="artist_name",
    orientation="h",
    labels={"track_popularity": "Popularidade", "artist_name": "Artista"},
)

fig.update_layout(
    yaxis={"categoryorder": "total ascending"},
    margin=dict(l=100, r=20, t=30, b=30)
)

st.plotly_chart(fig, use_container_width=True)
