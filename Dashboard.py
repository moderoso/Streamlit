# Importação das bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np
import matplotlib as plt 

import altair as alt

from utils import importacao_dados_previsao, tratando_dados

# Configuração da página
st.set_page_config(page_title= 'Dashboard - Preço do Petróleo', layout='wide', page_icon= ':fuelpump:,📊 ')

# Título da página
st.title('Dashboard - Variação do Preço do Petróleo :fuelpump:')

# Botão para atualizar os dados da aplicação
#atualiza_dados()

# Webscraping dos dados de petróleo
url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'

# Construção dos dataframes 
df_dolar = pd.read_csv('Valor_Dolar.csv', encoding = "ISO-8859-1", sep=";")
df_dolar.head()

df_datas_relevantes = pd.read_csv('Eventos_Relevantes_Petroleo.csv', encoding = "ISO-8859-1", sep=";")
df_datas_relevantes.head()

df_prod_pretoleo = pd.read_csv('Producao_Petroleo_Anual.csv', encoding = "ISO-8859-1", sep=";")
df_prod_pretoleo.head()

df = importacao_dados_previsao(url)
df_preco = tratando_dados(df)
df_preco.rename(columns={"ds":"Data", "y":"Valor"},inplace=True)

st.dataframe(df_preco)

# Inserindo barra para filtrar os anos
anos = df_preco['Data'].dt.year.unique()
anos_selecionados = st.slider("Selecione o intervalo de anos", 
                              min_value=int(anos.min()), 
                              max_value=int(anos.max()), 
                              value=(int(anos.min()), int(anos.max())))

# Filtrando o dataframe com base nos anos selecionados
df_filtrado = df_preco[(df_preco['Data'].dt.year >= anos_selecionados[0]) & 
                       (df_preco['Data'].dt.year <= anos_selecionados[1])]

col1, col2, col3, col4 = st.columns(4)

# Maior valor do ano atual
ano_atual = pd.Timestamp.now().year
df_atual = df_preco[df_preco['Data'].dt.year == ano_atual]
maior_valor_atual = df_atual['Valor'].max()
col1.metric("Maior Valor (Ano Atual)", f"${maior_valor_atual:.2f}")

# Data do último registro
ultima_data = df_preco['Data'].max()
col2.metric("Última Data Registrada", ultima_data.strftime('%d/%m/%Y'))

# Maior valor do período filtrado
maior_valor_filtrado = df_filtrado['Valor'].max()
col3.metric("Maior Valor (Período)", f"${maior_valor_filtrado:.2f}")

# Menor valor do período filtrado
menor_valor_filtrado = df_filtrado['Valor'].min()
col4.metric("Menor Valor (Período)", f"${menor_valor_filtrado:.2f}")



col1, col2, col3, col4 = st.columns(4)

# Maior valor do ano atual
ano_atual = pd.Timestamp.now().year
df_atual = df_preco[df_preco['Data'].dt.year == ano_atual]
maior_valor_atual = df_atual['Valor'].max()
col1.metric("Maior Valor (Ano Atual)", f"${maior_valor_atual:.2f}")

# Data do último registro
ultima_data = df_preco['Data'].max()
col2.metric("Última Data Registrada", ultima_data.strftime('%d/%m/%Y'))

# Maior valor do período filtrado
maior_valor_filtrado = df_filtrado['Valor'].max()
col3.metric("Maior Valor (Período)", f"${maior_valor_filtrado:.2f}")

# Menor valor do período filtrado
menor_valor_filtrado = df_filtrado['Valor'].min()
col4.metric("Menor Valor (Período)", f"${menor_valor_filtrado:.2f}")
