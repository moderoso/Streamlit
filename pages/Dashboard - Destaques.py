# Importação das bibliotecas
from bs4 import BeautifulSoup
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

import streamlit as st
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Configuração da página
st.set_page_config(page_title= 'Dashboard - Preço do Petróleo', layout='wide', page_icon= ':fuelpump:')

# Título da página
st.title('Dashboard - Variação do Preço do Petróleo :fuelpump:')

# Botão para atualizar os dados da aplicação
#atualiza_dados()

# Webscraping dos dados de petróleo
url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'
site = requests.get(url)
soup = BeautifulSoup(site.content,'html.parser')

# Construção dos dataframes 
nomes_colunas = []
dados = []
# Obtendo nome do cabeçalhos da tabela para criar o dataframe
for row in soup.find_all('td',{'class':'dxgvHeader'}):
  nomes_colunas.append(row.text.strip())

# Criando função para percorrer as linhas da tabela com as diferentes classes
# Inserindo dado em lista e aninhando em outra lista para gerar nosso dataframe
def busca_dados(classe):
  for linha in soup.find_all('tr',{'class':classe}):
    campos = []
    for valor in linha.find_all('td'):
      campos.append(valor.text.strip().replace(',','.'))
    dados.append(campos)


# Leitura dos dados de petróleo gravados no BigQuery
tabela_bq = 'tb_preco_petroleo'
dados_preco = select_bq(tabela_bq)

df_merged = pd.merge(dados_preco, dados_taxa, left_index=True, right_index=True, how='left')
df_merged.Taxa = df_merged.Taxa/100

# Preparação do gráfico
x = df_merged.index
y = df_merged.Preco
y2 = df_merged.Taxa

picos_indices_max = np.where(((y == 143.95) & (x =='2008-07-07')) | ((y == 126.64) & (x == '2011-05-06'))| ((y == 133.18) & (x == '2022-03-08')))[0] 
picos_indices_min = np.where(((y == 33.73) & (x =='2008-12-30')) | ((y == 26.01) & (x == '2016-01-24')) | ((y == 9.12) & (x == '2020-04-21')))[0] 
st.plotly_chart(graf_marcado_multiplos(x, y, picos_indices_max, picos_indices_min,y2), use_container_width=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric = dados.index.max().strftime('%d/%m/%Y')
    st.markdown(f"<h2 style='{cor_estilizada}'>{metrica1}</h2> <span style='{fonte_negrito}'> Dados atualizados até </span>", unsafe_allow_html=True)
    #st.metric('Dados atualizados até:', value=dados.index.max().strftime('%d/%m/%Y')) 
with col2: 
    st.metric = dados.index.min().strftime('%d/%m/%Y')
    st.markdown(f"<h2 style='{cor_estilizada}'> {metrica2} </h2> <span style='{fonte_negrito}'> Dados monitorados desde</span> ", unsafe_allow_html=True) 
with col3:
    metrica3 = dados['Preco'].min()
    data_metrica3 = dados[dados['Preco']==dados['Preco'].min()].index
    st.markdown(f"<h2 style='{cor_estilizada}'> US$ {metrica3:.2f} </h2> <span style='{fonte_negrito}'> Menor preço histórico <br> (atingido em  {data_metrica3[0].strftime('%d/%m/%Y')})</span> ", unsafe_allow_html=True) 
    #st.metric('Menor preço histórico:', value=dados['Preco'].min().round(2))
with col4:
    metrica4 = dados['Preco'].max()
    data_metrica4 = dados[dados['Preco']==dados['Preco'].max()].index
    st.markdown(f"<h2 style='{cor_estilizada}'> US$ {metrica4:.2f} </h2> <span style='{fonte_negrito}'> Maior preço histórico <br> (atingido em  {data_metrica4[0].strftime('%d/%m/%Y')})</span> ", unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

## Gráficos
data = st.slider('Selecione o intervalo', min_value=media_mensal_anos['Ano'].min(), max_value=media_mensal_anos['Ano'].max(), value=(2019, media_mensal_anos['Ano'].max()))
col1, col2 = st.columns(2)
with col1:
    dados_intervalo = dados_sem_dataindex.query('@data[0] <= Ano <= @data[1]')
    st.plotly_chart(graf_marcado_max_min(dados_intervalo), use_container_width=True)
    st.divider()
    st.plotly_chart(fig_picos_preco, use_container_width=True)
with col2:
    fig_media_mensal_anos = px.line(media_mensal_anos.query('@data[0] <= Ano <= @data[1]'), 
                             x = 'Mes',
                             y = 'Preco',
                             markers = True,
                             range_y = (0, media_mensal_anos.max()),
                             color = 'Ano',
                             line_dash = 'Ano',
                             title = 'Média de preço por mês e ano')
    fig_media_mensal_anos.update_layout(yaxis_title = 'Média de Preço (US$)')
    st.plotly_chart(fig_media_mensal_anos, use_container_width=True)
    st.divider()
    st.plotly_chart(fig_vales_preco, use_container_width=True)    