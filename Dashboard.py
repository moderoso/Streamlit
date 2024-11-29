# Importação das bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
#from utils import webscraping,graf_marcado_max_min,atualiza_dados

# Configuração da página
st.set_page_config(page_title= 'Dashboard - Preço do Petróleo', layout='wide', page_icon= ':fuelpump:,📊 ')

# Título da página
st.title('Dashboard - Variação do Preço do Petróleo :fuelpump:')

# Botão para atualizar os dados da aplicação
#atualiza_dados()

# Webscraping dos dados de petróleo
#url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?serid=38590&module=M'
#coluna = 'Preco'
#dados = webscraping(url,coluna)

# Construção dos dataframes 
@st.cache_data
def get_dolar_data ():
df_dolar = pd.read_csv('dolar.csv', encoding = "ISO-8859-1", sep=";")
df_dolar.head()

if st.checkbox('Show dataframe'):
	st.write(df_dolar)


st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames.
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
)



try:
    df = get_dolar_data ()
    ano = st.multiselect(
        "Selecione Ano", list(df.index), ["2024", "2023"]
    )
    if not anos:
        st.error("Selecione um ano.")

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Region:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )