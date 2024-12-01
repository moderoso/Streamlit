# Importação das bibliotecas
import pandas as pd
import streamlit as st

from pmdarima import auto_arima
from sklearn.model_selection import TimeSeriesSplit

import numpy as np
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import mean_absolute_error
from statsmodels.tsa.arima.model import ARIMA

# Armazenamento dos dados em cache, melhorando a performance do site
@st.cache_data 


def importacao_dados_previsao(url):
    """
    Coleta dados de uma série temporal do site do IPEA.

    Args:
        url (str): URL da página do IPEA contendo os dados da série.

    Returns:
        pd.DataFrame: DataFrame com os dados coletados.
    """
    def busca_dados(classe, soup, dados):
        """
        Busca os dados nas linhas de uma classe específica.

        Args:
            classe (str): Nome da classe CSS das linhas.
            soup (BeautifulSoup): Objeto BeautifulSoup da página HTML.
            dados (list): Lista para armazenar os dados extraídos.
        """
        for linha in soup.find_all('tr', {'class': classe}):
            campos = []
            for valor in linha.find_all('td'):
                campos.append(valor.text.strip().replace(',', '.'))
            dados.append(campos)

    try:
        # Fazendo a requisição ao site
        site = requests.get(url)
        site.raise_for_status()  # Garante que a requisição foi bem-sucedida
        soup = BeautifulSoup(site.content, 'html.parser')

        # Inicializando listas para armazenar cabeçalhos e dados
        nomes_colunas = []
        dados = []

        # Obtendo os nomes das colunas da tabela
        for row in soup.find_all('td', {'class': 'dxgvHeader'}):
            nomes_colunas.append(row.text.strip())

        # Coletando os dados das linhas com as classes apropriadas
        busca_dados('dxgvDataRow', soup, dados)
        busca_dados('dxgvDataRowAlt', soup, dados)

        # Transformando os dados coletados em um DataFrame
        df = pd.DataFrame(data=dados, columns=nomes_colunas).drop_duplicates()
        df.dropna(inplace=True)

        # Retorno do DataFrame processado
        return df

    except Exception as e:
        print(f"Erro ao coletar dados: {e}")
        return pd.DataFrame()

def tratando_dados(df):
    # Renomeando as colunas para o formato padrão utilizado em time series para escolha do modelo
    df.rename(columns={"Data":"ds","Preço - petróleo bruto - Brent (FOB)":"y"},inplace=True)

    # Alterando o tipo do dado das colunas para Data e númerica
    df['ds'] = pd.to_datetime(df['ds'],format="%d/%m/%Y")
    df['y'] = pd.to_numeric(df['y'])
    df_preco = df.sort_values(by='ds')

    return df_preco

@st.cache_resource 

@st.cache_data 
def modelo_previsao_prophet(df_preco):

  ultimos_dias = df_preco['ds'].max() - pd.DateOffset(months=3)

  df_treino = df_preco[df_preco['ds'] < ultimos_dias]
  df_teste = df_preco[df_preco['ds'] >= ultimos_dias]


  # Armazenando resultados
  results_prophet = []

  model = Prophet(seasonality_mode='multiplicative',daily_seasonality=True, yearly_seasonality=True)  # ou 'multiplicative', dependendo do comportamento dos dados
  model.fit(df_treino)


  # Prevendo para o conjunto de validação
  forecast = model.predict(df_teste[['ds']])
  valid = df_teste.merge(forecast[['ds', 'yhat']], on='ds')

  # Calculando as métricas
  mae = mean_absolute_error(valid['y'], valid['yhat'])
  wmape_value = np.sum(np.abs(valid['y'] - valid['yhat'])) / np.sum(valid['y'])
  mape = np.mean(np.abs((valid['y'] - valid['yhat']) / valid['y'])) * 100

  results_prophet.append({
      'MAE': mae,
      'WMAPE': wmape_value,
      'MAPE': mape
  })

  # Consolidando os resultados
  results_df = pd.DataFrame(results_prophet)
  plot_resultado(results_df)

  # Treinando o modelo final e prevendo os próximos 90 dias
  final_model = Prophet(daily_seasonality=True, yearly_seasonality=True)
  final_model.fit(df_preco)

  future_dates = final_model.make_future_dataframe(periods=90)
  future_forecast = final_model.predict(future_dates)

  # Exibindo as previsões para os próximos 90 dias
  future_forecast[['ds', 'yhat']].tail(90)

  return future_forecast

def plot_previsao(df_real, previsao, titulo='Previsão do Preço do Petróleo (Próximos 90 dias)'):
    """
    Plota os dados reais e as previsões futuras usando matplotlib e exibe no Streamlit.

    Args:
        df_real (pd.DataFrame): DataFrame com os dados reais (colunas 'ds' e 'y').
        previsao (pd.DataFrame): DataFrame com as previsões (colunas 'ds' e 'yhat').
        titulo (str): Título do gráfico.
    """
    # Criando a figura
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plotando os valores reais
    ax.plot(df_real['ds'], df_real['y'], label='Valores Reais')
    
    # Plotando as previsões
    ax.plot(previsao['ds'], previsao['yhat'], label='Previsões', linestyle='--', color='orange')
    
    # Linha indicando o início das previsões
    ax.axvline(x=df_real['ds'].max(), color='red', linestyle='--', label='Início das Previsões')
    
    # Configurações do gráfico
    ax.set_xlabel('Data')
    ax.set_ylabel('Preço do Petróleo')
    ax.set_title(titulo)
    ax.legend()
    ax.grid(alpha=0.3)
    
    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)


def plot_previsao_10_meses(df_preco, future_forecast, titulo='Previsão do Preço do Petróleo (Últimos 10 Meses + Próximos 90 dias)'):

    """
    Plota os dados reais dos últimos 10 meses e as previsões para os próximos 90 dias.

    Args:
        df_preco (pd.DataFrame): DataFrame com os dados reais (colunas 'ds' e 'y').
        future_forecast (pd.DataFrame): DataFrame com as previsões (colunas 'ds' e 'yhat').
        titulo (str): Título do gráfico.
    """
    # Filtrando os últimos 10 meses do DataFrame
    last_10_months = df_preco['ds'].max() - pd.DateOffset(months=10)
    df_filtered = df_preco[df_preco['ds'] >= last_10_months]

    # Filtrando as previsões para incluir apenas os próximos 90 dias
    last_date = df_preco['ds'].max()
    future_forecast_filtered = future_forecast[
        (future_forecast['ds'] > (last_date + pd.Timedelta(days=-300))) & 
        (future_forecast['ds'] <= last_date + pd.Timedelta(days=90))
    ]

    # Criando a figura do gráfico
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plotando os últimos 10 meses de dados reais
    ax.plot(df_filtered['ds'], df_filtered['y'], label='Valores Reais', linewidth=2)

    # Plotando previsões futuras filtradas
    ax.plot(future_forecast_filtered['ds'], future_forecast_filtered['yhat'], label='Previsões', linestyle='--', color='orange')

    # Linha vertical indicando o início das previsões
    ax.axvline(x=last_date, color='red', linestyle='--', label='Início das Previsões')

    # Personalizando o gráfico
    ax.set_xlabel('Data')
    ax.set_ylabel('Preço do Petróleo')
    ax.set_title(titulo)
    ax.legend()
    ax.grid(alpha=0.3)

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)


def plot_resultado(dataframe):
    col1, col2, col3, col4 = st.columns(4)

    # Maior valor do ano atual
    mae = dataframe['MAE'].mean()
    col1.metric("Valor MAE do modelo:", f"{mae:.2f}%")

    # Data do último registro
    wmape = dataframe['WMAPE'].mean()
    col2.metric("Valor WMAPE do modelo:", f"{wmape:.2f}%")

    # Maior valor do período filtrado
    mape = dataframe['MAPE'].mean()
    col3.metric("Valor MAPE do modelo:", f"{mape:.2f}%")

    # Menor valor do período filtrado
    acuracia = 100 - mape
    col4.metric("Valor de acurácia do modelo:", f"{acuracia:.2f}%")

def modelo_previsao_ARIMA(df_preco, p=1, d=1, q=1):
    ultimos_dias = df_preco['ds'].max() - pd.DateOffset(months=3)

    # Separação dos conjuntos de treino e teste
    df_treino = df_preco[df_preco['ds'] < ultimos_dias]
    df_teste = df_preco[df_preco['ds'] >= ultimos_dias]

    results_arima = []
    # Ajustando o modelo ARIMA
    arima_model = ARIMA(df_treino['y'], order=(p, d, q))
    arima_fitted = arima_model.fit()

    # Previsões no conjunto de teste
    forecast = arima_fitted.forecast(steps=len(df_teste))
    valid = df_teste['y'].values  # Valores reais do conjunto de teste

    print(forecast)
   # Calculando as métricas
    mae = mean_absolute_error(valid, forecast)
    wmape_value = np.sum(np.abs(valid - forecast)) / np.sum(valid)
    mape = np.mean(np.abs((valid - forecast) / valid)) * 100

    results_arima.append({
        'MAE': mae,
        'WMAPE': wmape_value,
        'MAPE': mape
    })

    # Consolidando os resultados
    results_df = pd.DataFrame(results_arima)
    plot_resultado(results_df)

    # Treinando o modelo final com todos os dados
    final_arima_model = ARIMA(df_preco['y'], order=(p, d, q))
    final_arima_fitted = final_arima_model.fit()

    # Previsões futuras
    future_predictions = final_arima_fitted.forecast(steps=90)
    last_date = df_preco['ds'].max()
    future_dates = pd.date_range(last_date + pd.Timedelta(days=1), periods=90, freq='D')

    # Retornando previsões futuras
    future_forecast_df = pd.DataFrame({'ds': future_dates, 'yhat': future_predictions})
    return future_forecast_df

@st.cache_resource 

