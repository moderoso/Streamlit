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

picos_indices_max = np.where(((y == 143.95) & (x =='2008-07-07')) | ((y == 126.64) & (x == '2011-05-06'))| ((y == 133.18) & (x == '2022-03-08')))[0] 
picos_indices_min = np.where(((y == 33.73) & (x =='2008-12-30')) | ((y == 26.01) & (x == '2016-01-24')) | ((y == 9.12) & (x == '2020-04-21')))[0] 
st.plotly_chart(graf_marcado_multiplos(x, y, picos_indices_max, picos_indices_min,y2), use_container_width=True)	
	
	
	



