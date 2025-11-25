import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Musical", layout="wide")

st.title("🎵 Dashboard Musical — Spotify: Análise dados")

st.markdown("""
 Bem-vindo ao dashboard!  
 Use o menu lateral para navegar entre as páginas.
 """)
try:
    df_preview = pd.read_csv("https://raw.githubusercontent.com/LucasAdolfo/Dashboard/refs/heads/main/MyDash/dados.csv")
    rows, cols = df_preview.shape

    st.markdown(f"""
    Bem-vindo(a) ao **Spotify Dashboard Musical**!

    Este aplicativo foi desenvolvido para explorar e visualizar os principais dados sobre o app de músicas chamado Spotify. Através de dados detalhados, buscamos responder a perguntas cruciais como:

    * **Quantos minutos tem a música e qual sua popularidade?**
    * **Quais as músicas mais populares?**
    * **Quais mais populares e que possuem mais seguidores?**
    * **Quais os anos com mais lançamentos de álbuns?**
    * **Quais os gêneros musicais mais frequentes e populares?**
   

    Nosso objetivo é fornecer uma ferramenta clara e intuitiva para explorar e entender os dados musicais do Spotify.

    ---

    ### Como Navegar:

    Utilize o menu de navegação na **barra lateral (esquerda)** para explorar as diferentes seções do aplicativo:

    * **📊 Dashboard Musical:** Explore as principais métricas e visualizações relacionadas às músicas do Spotify.
    * **📈 Tendências & Análises:** Mergulhe em análises detalhadas sobre tendências musicais e outros insights relevantes.
    * **🎤 Artistas:** Descubra informações sobre os artistas mais populares e seus seguidores.
    * **💿 Álbuns:** Analise os lançamentos de álbuns ao longo do tempo e sua popularidade.
    ---
        
    O seu conjunto de dados tem as seguintes dimensões:
    - **Linhas:** {rows} 📊
    - **Colunas:** {cols} 📈

    Agradecemos a sua visita e esperamos que encontre informações valiosas aqui!
    """)
except Exception as e:
    st.error(f"Não foi possível ler 'dados.csv': {e}")

st.header("Visão Geral dos Dados Principais")


df = pd.read_csv("dados.csv")

st.dataframe(df)




