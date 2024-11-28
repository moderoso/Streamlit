# Importação das bibliotecas
import streamlit as st
import pandas as pd
from utils import modelo_previsao_prophet,tratando_dados,importacao_dados_previsao,plot_previsao,plot_previsao_10_meses,modelo_previsao_ARIMA

# Configuração da página
st.set_page_config(page_title= 'Modelo - Predição', layout='wide', page_icon= ':fuelpump:')

# Título da página e descrição introdutória do modelo escolhido, parâmetros e performance
st.title('Modelo Preditivo :telescope: ⚡')

st.markdown('<p style="text-align: justify;">Testando atualização do MVP do projeto com o GitHub na minha máquina <span style="font-weight: bold">-- Jhonny</span>. </p>', unsafe_allow_html = True)
st.subheader('Escolha um tipo de modelo abaixo: ')

opcao = st.radio(
    "Selecione uma das opções abaixo:",
    ("Prophet", "ARIMA")
)
# Leitura dos dados de petróleo com WebScraping
url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'
df = importacao_dados_previsao(url)

# Tratando os dados coletados para retornar o df que será usado nas predições
df_preco = tratando_dados(df)

# Execução da lógica com base na escolha
if opcao == "Prophet":
    # Aplicando o dataframe após o tratamento para treinar o modelo usando o Prophet
    future_forecast = modelo_previsao_prophet(df_preco)

    # Plotando o resultado 
    plot_previsao(df_preco,future_forecast)

    # Plotando o resultado dos últimos 10 meses + os próximos 90 dias previstos
    plot_previsao_10_meses(df_preco,future_forecast)
elif opcao == "ARIMA":
    future_forecast = modelo_previsao_ARIMA(df_preco)

    # Plotando o resultado 
    plot_previsao(df_preco,future_forecast)

    # Plotando o resultado dos últimos 10 meses + os próximos 90 dias previstos
    plot_previsao_10_meses(df_preco,future_forecast)