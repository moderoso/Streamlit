# Importação das bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

from utils import atualiza_dados

# Configuração da página
st.set_page_config(page_title= 'Dashboard - Preço do Petróleo', layout='wide', page_icon= ':fuelpump:,📊 ')

# Título da página
st.title('Dashboard - Variação do Preço do Petróleo :fuelpump:')

# Botão para atualizar os dados da aplicação
atualiza_dados()

# Webscraping dos dados de petróleo
url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?serid=38590&module=M'
coluna = 'Preco'
dados_taxa = webscraping(url,coluna)

# Construção dos dataframes 
#@st.cache_data
#def get_dolar_data():
df_dolar = pd.read_csv('dolar.csv', encoding = "ISO-8859-1", sep=";")
df_dolar.head()

if st.checkbox('Show dataframe'):
	st.write(df_dolar)
	
# Create a line chart
fig = px.line(df_dolar, x='Data', y='Valor')  # Assuming 'Data' and 'Valor' are columns in your DataFrame

# Display the chart in Streamlit
st.plotly_chart(fig)	

fig = px.line(df_dolar, x='Data', y='Valor', 
                   title='Variação do Dólar', 
                   labels={'Data': 'Data', 'Valor': 'Valor do Dólar'})


