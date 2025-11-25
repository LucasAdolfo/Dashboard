import streamlit as st
import pandas as pd
import plotly.express as px
import os  
st.set_page_config(layout="wide")  


st.title("💿 Análise de Álbuns")

@st.cache_data
def le_dados():
    return pd.read_csv("https://raw.githubusercontent.com/LucasAdolfo/Dashboard/refs/heads/main/MyDash/dados.csv")
# LEITURA DO CSV
try:
    df = le_dados();
except FileNotFoundError:
    st.error('Arquivo "dados.csv" não encontrado. Coloque o arquivo na mesma pasta do app.')
    st.stop()
except Exception as e:
    st.error(f"Erro ao carregar CSV: {e}")
    st.stop()

# ===========================
# VALIDAR COLUNAS NECESSÁRIAS
# ===========================
required_cols = {"album_release_date", "album_name"}
missing = required_cols - set(df.columns)

if missing:
    st.error(
        "As seguintes colunas necessárias estão faltando no dataset: "
        + ", ".join(sorted(missing))
    )
    st.write("Colunas disponíveis:", list(df.columns))
    st.stop()

# ===========================
# TRATAMENTO DA COLUNA DE ANO
# ===========================
def extrair_ano(valor):
    try:
        return int(str(valor)[:4])
    except:
        return None

df["ano"] = df["album_release_date"].apply(extrair_ano)
df = df.dropna(subset=["ano"])
df["ano"] = df["ano"].astype(int)

# ===========================
# SLIDER DE ANOS
# ===========================
min_ano = int(df["ano"].min())
max_ano = int(df["ano"].max())

anos = st.sidebar.slider(
    "Selecione o intervalo de anos",
    min_ano,
    max_ano,
    (min_ano, max_ano)
)

df2 = df[(df["ano"] >= anos[0]) & (df["ano"] <= anos[1])]

if df2.empty:
    st.warning("Nenhum álbum encontrado nesse intervalo de anos.")
    st.stop()

# ===========================
# GRÁFICO INTERATIVO (COM HOVER)
# ===========================
st.subheader("📅 Lançamentos ao longo do tempo")

lan = (
    df2.groupby("ano")["album_name"]
    .nunique()
    .reset_index(name="quantidade")
)

fig = px.line(
    lan,
    x="ano",
    y="quantidade",
    markers=True,
    title="Número de Álbuns Lançados por Ano",
    labels={"ano": "Ano", "quantidade": "Quantidade de Álbuns"},
)

fig.update_traces(
    hovertemplate="<b>Ano:</b> %{x}<br><b>Álbuns:</b> %{y}<extra></extra>"
)

fig.update_layout(
    hovermode="x unified",
    xaxis=dict(dtick=1, showgrid=True),
    yaxis=dict(showgrid=True),
)


st.plotly_chart(fig, use_container_width=True)
