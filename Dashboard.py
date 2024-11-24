# Para realizar o WebScraping
from bs4 import BeautifulSoup
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

from prophet import Prophet
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from statsmodels.tsa.arima.model import ARIMA


# Importação da biblioteca streamlit
import streamlit as st

# Configuração da página
st.set_page_config(page_title= 'Sobre o Projeto', layout='wide', page_icon= ':fuelpump:')

# Título da página
st.title('Desenvolvimento do Projeto 🛠️')

# Descrição do projeto
st.markdown('<p style="text-align: justify;">Este projeto foi um Tech Challenge proposto na quarta fase do curso de Pós-graduação em Data Analytics da faculdade Fiap em que nós alunos fomos convidados a analisar o preço histórico do barril de petróleo e a partir dessa análise cumprir alguns desafios:</p>', unsafe_allow_html = True)
st.markdown('- Criar um dashboard interativo')
st.markdown('- Apresentar insights')
st.markdown('- Criar um modelo preditivo com Série Temporal')
st.markdown('- Fazer deploy do modelo em produção')

# Visualização da fluxo de trabalho do projeto
st.markdown('## Fluxo de Trabalho')
miro_url = 'https://miro.com/app/live-embed/uXjVN1YW9H4=/?moveToViewport=-1349,-868,3306,1721&embedId=214115551426'
st.markdown(f'<iframe width="80%" height="600" src="{miro_url}" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" allowfullscreen></iframe>', unsafe_allow_html=True)

# Links
st.markdown('## Links Úteis')
st.markdown('##### Repositório do projeto')
st.markdown('[Repositório do projeto no Github](https://github.com/kfpetruz/Dash-e-Modelo-Preditivo-Combustiveis)')
st.markdown('##### Fontes de dados')
st.markdown('[Preço do Petróleo](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view)')
st.markdown('[Taxa de Câmbio Dólar-Real](http://www.ipeadata.gov.br/ExibeSerie.aspx?serid=38590&module=M)')
st.markdown('##### Fontes informacionais')
st.markdown('[Site BBC News Brasil - publicado em maio/2015](https://www.bbc.com/portuguese/noticias/2015/05/150508_china_desaceleracao_lgb)') 
st.markdown('[Site Exame - publicado em novembro/2015](https://exame.com/economia/precos-do-petroleo-se-aproximam-do-fundo-do-poco-de-2008/)')
st.markdown('[Site Veja - publicado em abril/2020](https://veja.abril.com.br/economia/petroleo-tem-menor-preco-em-18-anos-por-queda-na-demanda-devido-covid-19)')
st.markdown('[Jornal Nexo - março/2022](https://www.nexojornal.com.br/expresso/2022/03/17/5-gr%C3%A1ficos-para-entender-20-anos-de-pre%C3%A7os-da-gasolina)')  
st.markdown('[Oito motivos para a queda do preço do  petróleo -  Acesso em 20 novembro. 2024](https://www.dw.com/pt-br/oito-motivos-para-a-queda-do-pre%C3%A7o-do-petr%C3%B3leo/a-19051686)') 

# Equipe do projeto
st.markdown('## Equipe FIAP')
st.markdown('#####  Caio Vinicius Branco Gonçalves - RM 354248', unsafe_allow_html = True)
st.markdown('##### Jhonny da Silva Mineu - RM 355135', unsafe_allow_html = True)
st.markdown('#####  Marina Mendez Araujo - RM 355100', unsafe_allow_html = True)
st.markdown('##### Mônada Raquel Brito de Oliveira - RM 354367', unsafe_allow_html = True)
st.markdown('##### Volmir Moderoso Santos - RM 355589', unsafe_allow_html = True)



