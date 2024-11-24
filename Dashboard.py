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
#st.markdown('## Links Úteis')
st.markdown('##### Fontes de dados')
st.markdown('Link acessado em 20 novembro 2024   ' '[A história do petróleo no Brasil](https://www.gov.br/anp/pt-br/acesso-a-informacao/institucional/historia-petroleo-brasil)')
st.markdown('Link acessado em 20 novembro 2024   ' '[Qual é a origem do petróleo?](https://www.bbc.com/portuguese/articles/cnk0e0yydelo)')
st.markdown('Link acessado em 20 novembro 2024   ' '[OPEC]( https://www.opec.org/opec_web/en/index.htm)')
st.markdown('Link acessado em 20 novembro 2024   ' '[OpenAI. “O Chat GPT é uma ferramenta de processamento de linguagem natural orientada por IA, que possibilita conversas semelhantes às humanas com o chatbot](https://openai.com/blog/chat-gpt-3-launch/)')
st.markdown('Link acessado em 20 novembro 2024   ' '[Geopolítica do Petróleo](https://mundoeducacao.uol.com.br/geografia/geopolitica-petroleo.html)') 
st.markdown('Link acessado em 20 novembro 2024   ' '[Nos Bastidores da Terra: Geóloga Explica a Formação do Petróleo](https://super.abril.com.br/coluna/deriva-continental/nos-bastidores-da-terra-geologa-explica-a-formacao-do-petroleo#google_vignette)')
st.markdown('Link acessado em 20 novembro 2024   ' '[Organização dos Países Exportadores de Petróleo](https://pt.wikipedia.org/wiki/Organiza%C3%A7%C3%A3o_dos_Pa%C3%ADses_Exportadores_de_Petr%C3%B3leo)')
st.markdown('Link acessado em 20 novembro 2024   ' '[Agência Internacional de Energia](https://pt.wikipedia.org/wiki/Ag%C3%AAncia_Internacional_de_Energia)')  
st.markdown('Link acessado em 20 novembro 2024   ' '[Oito motivos para a queda do preço do  petróleo](https://www.dw.com/pt-br/oito-motivos-para-a-queda-do-pre%C3%A7o-do-petr%C3%B3leo/a-19051686)') 

# Equipe do projeto
st.markdown('## Equipe FIAP')
st.markdown('#### Caio Vinicius Branco Gonçalves - RM 354248')
st.markdown('#### Jhonny da Silva Mineu - RM 355135')
st.markdown('#### Marina Mendez Araujo - RM 355100')
st.markdown('#### Mônada Raquel Brito de Oliveira - RM 354367')
st.markdown('#### Volmir Moderoso Santos - RM 355589')



