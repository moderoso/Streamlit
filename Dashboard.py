# Importação das bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from utils import webscraping,graf_marcado_max_min,atualiza_dados

# Configuração da página
st.set_page_config(page_title= 'Dashboard - Preço do Petróleo', layout='wide', page_icon= ':fuelpump:')

# Título da página
st.title('Dashboard - Variação do Preço do Petróleo :fuelpump:')

# Botão para atualizar os dados da aplicação
atualiza_dados()

# Webscraping dos dados de petróleo
url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?serid=38590&module=M'
coluna = 'Preco'
dados = webscraping(url,coluna)

# Construção dos dataframes 
dados_sem_dataindex = dados.reset_index()
dados_sem_dataindex['Ano'] = dados_sem_dataindex['Data'].dt.year.astype(int)

media_mensal_anos = dados.groupby(pd.Grouper(freq= 'M'))[['Preco']].mean().reset_index() #Agrupando os dados por mês
media_mensal_anos['Ano'] = media_mensal_anos['Data'].dt.year.astype(int)
media_mensal_anos['Mes'] = media_mensal_anos['Data'].dt.month_name()

picos_preco = media_mensal_anos.set_index('Data').sort_values('Preco', ascending=False).head(10)

vales_preco = media_mensal_anos.set_index('Data').sort_values('Preco', ascending=True).head(10)

# Construção dos gráficos          
fig_picos_preco = px.bar(picos_preco,
                        x = picos_preco['Mes'].astype(str) + '/' + picos_preco['Ano'].astype(str),
                        y = 'Preco',
                        text_auto=True,
                        title= f'Top 10 meses com média de preços mais altos')
fig_picos_preco.update_xaxes(type='category')
fig_picos_preco.update_layout(xaxis_title= 'Data', yaxis_title = 'Preço (US$)')

fig_vales_preco = px.bar(vales_preco,
                        x = vales_preco['Mes'].astype(str) + '/' + vales_preco['Ano'].astype(str),
                        y = 'Preco',
                        text_auto=True,
                        title= f'Top 10 meses com média de preços mais baixos')
fig_vales_preco.update_xaxes(type='category')
fig_vales_preco.update_layout(xaxis_title= 'Data', yaxis_title = 'Preço (US$)')
