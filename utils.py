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
import seaborn as sns
import statsmodels.api as sm

from prophet import Prophet
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from statsmodels.tsa.arima.model import ARIMA

# Armazenamento dos dados em cache, melhorando a performance do site
@st.cache_data 
# Leitura do dados no site e armazenamento no banco de dados no BigQuery
# Armazenamento dos dados em cache
@st.cache_data 
# Consulta full de cada tabela criada no BigQuery


# Os dados do site de petróleo não são atualizados todos os dias, mas como a aplicação está armazenando os dados em cache, quando estiverem desatualizados, se faz necessário clicar 
def atualiza_dados():
    if st.sidebar.button("###### Clique para atualizar os dados da aplicação"):
        # Limpa o cache de dados
        st.cache_data.clear()
        st.cache_resource.clear()

# Gráfico de decomposição sazonal, que pode ser selecionados para diferentes períodos pelo usuário
def decomposicao(dados,resultado):
    st.subheader('Série Temporal Original')
    st.line_chart(dados)
    st.subheader('Tendência')
    st.markdown('<p style="text-align: justify;">Quando falamos sobre tendência na decomposição de uma série temporal, estamos interessados em identificar padrões de crescimento ou declínio que ocorrem ao longo de um período de tempo significativo, ignorando as variações sazonais e flutuações aleatórias que podem ocorrer em escalas de tempo menores.</p>', unsafe_allow_html = True)
    st.line_chart(resultado.trend)
    st.subheader('Sazonalidade')
    st.markdown('<p style="text-align: justify;">A sazonalidade indica variações sistemáticas que ocorrem em determinados momentos ou períodos do ano e são independentes da tendência de longo prazo e das flutuações aleatórias na série temporal. Ela reflete regularidades que podem ser observadas ao longo de múltiplos ciclos sazonais.</p>', unsafe_allow_html = True)
    st.line_chart(resultado.seasonal)
    st.subheader('Residual')
    st.markdown('<p style="text-align: justify;">Na decomposição de uma série temporal, o resíduo (também conhecido como erro ou componente aleatório) é a parte da série que não pode ser explicada pela tendência de longo prazo e pela sazonalidade. Em outras palavras, o resíduo representa as flutuações irregulares e imprevisíveis que não seguem nenhum padrão discernível na série temporal.</p>', unsafe_allow_html = True)
    st.line_chart(resultado.resid)

# Realização do teste de Dickey-Fuller Aumentado e dos gráfico de autocorreção de acordo com a seleção do usuário
def teste_estatistico(dados,string_teste):
    st.subheader('Testes Estatísticos')
    st.markdown('<p style="text-align: justify;">O teste de Dickey-Fuller Aumentado (ADF), frequentemente implementado na função adfuller do pacote statsmodels em Python, é um teste estatístico utilizado para determinar se uma série temporal é estacionária ou não. Uma série temporal é considerada estacionária quando suas propriedades estatísticas, como média e variância, permanecem constantes ao longo do tempo. Em outras palavras, não há padrões sistemáticos ou tendências discerníveis na série que afetem sua média ou variância.</p>', unsafe_allow_html = True)

    st.markdown(f'<p style="text-align: justify;"><span style="font-weight: bold">{string_teste}</span></p>', unsafe_allow_html = True)
    
    resultado_adf = adfuller(dados)
    st.markdown(f'<p style="text-align: justify;">Estatística do teste ADF: {resultado_adf[0]}.</p>', unsafe_allow_html = True)
    st.markdown(f'<p style="text-align: justify;">Valor-p: {resultado_adf[1]}.</p>', unsafe_allow_html = True)
    st.markdown(f'<p style="text-align: justify;">Valores críticos:</p>', unsafe_allow_html = True)
    for chave, valor in resultado_adf[4].items():
        st.markdown(f'<p style="text-align: justify;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{chave}: {valor}.</p>', unsafe_allow_html = True)
    st.markdown('<p style="text-align: justify;">Se o valor-p for menor que o nível de significância escolhido (geralmente 0.05), rejeitamos a hipótese nula e concluímos que a série é estacionária. Caso contrário, não rejeitamos a hipótese nula e inferimos que a série não é estacionária. Isso significa que a série possui tendência.</p>', unsafe_allow_html = True)
    
    # Interpretação do resultado do teste
    if resultado_adf[1] < 0.05:
        st.markdown(f'<p style="text-align: justify;">Dessa forma, a série temporal é estacionária (rejeitamos a hipótese nula).</p>', unsafe_allow_html = True)
    else:
        st.markdown(f'<p style="text-align: justify;">Dessa forma, a série temporal não é estacionária (falhamos em rejeitar a hipótese nula).</p>', unsafe_allow_html = True)

    st.subheader('Gráficos de Autocorrelação')
    st.markdown(f'<p style="text-align: justify;">Para identificar a presença de sazonalidade nos gráficos de autocorrelação simples (ACF) e autocorrelação parcial (PACF), é possível procurar padrões de picos significativos em intervalos regulares.</p>', unsafe_allow_html = True)
    st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Autocorrelação Simples (ACF):</span> os picos indicam a correlação entre a série temporal atual e suas observações passadas em vários lags. Se houver picos significativos em intervalos regulares, isso sugere a presença de sazonalidade na série temporal.</p>', unsafe_allow_html = True)
    st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Autocorrelação Parcial (PACF):</span> os picos representam a correlação entre a série temporal atual e suas observações passadas, removendo o efeito das observações intermediárias. Picos significativos em intervalos regulares no PACF também indicam a presença de sazonalidade.</p>', unsafe_allow_html = True)
    
    # Costrução dos gráficos de autocorrelação
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        plot_acf(dados, ax=ax)
        plt.xlabel('Lag')
        plt.ylabel('ACF')
        plt.title('Função de Autocorrelação (ACF)')
        fig.patch.set_alpha(0)
        st.pyplot(fig)
    with col2:
        fig, ax = plt.subplots()
        plot_pacf(dados, ax=ax)
        plt.xlabel('Lag')
        plt.ylabel('PACF')
        plt.title('Função de Autocorrelação (PACF)')
        fig.patch.set_alpha(0)
        st.pyplot(fig)



# Armazenamento do modelo em cache
@st.cache_resource 
# Função criada para encontrar a melhor perfomance do modelo ETS, com base nos dados de treino e teste
def modelo_ets_perfomance(dados, qt_dias):
    dados = dados.tail(qt_dias)
    # Definindo os parâmetros a serem testados
    parametros_grid = {
        'trend': ['additive', 'multiplicative'],
        'seasonal': ['additive', 'multiplicative'],
        'seasonal_periods': [30],  # Assumindo um padrão sazonal mensal
    }

    # Configurando a validação cruzada de séries temporais
    tscv = TimeSeriesSplit(n_splits=5)

    # Inicializando as variáveis para armazenar os melhores resultados
    melhor_mae = float('inf')
    melhor_wmape = float('inf')
    melhores_parametros = None
    df_completo = pd.DataFrame(columns=['Qtd dias treinados', 'Qtd dias testados', 'MAE', 'WMAPE', 'Tendência', 'Sazonalidade', 'Períodos Sazonais'])

    # Loop através dos parâmetros
    for trend in parametros_grid['trend']:
        for seasonal in parametros_grid['seasonal']:
            for seasonal_periods in parametros_grid['seasonal_periods']:
                # Criando o modelo ETS
                modelo_ets = ExponentialSmoothing(dados['Preco'], trend=trend, seasonal=seasonal, seasonal_periods=seasonal_periods)

                # Iterando sobre diferentes janelas de treinamento
                for train_index, test_index in tscv.split(dados):
                    dados_treino, dados_teste = dados.iloc[train_index], dados.iloc[test_index]

                    # Treinando o modelo
                    resultado = modelo_ets.fit()

                    # Fazendo previsões
                    previsao = resultado.forecast(steps=len(dados_teste))

                    # Calculando o MAE
                    mae = mean_absolute_error(dados_teste['Preco'].values, previsao)

                    # Calculando o WMAPE
                    wmape_teste = wmape(dados_teste['Preco'].reset_index(drop=True), previsao.reset_index(drop=True)) 

                    # Dados para adicionar como nova linha, para retornar todos os resultados
                    nova_linha = {'Qtd dias treinados': len(dados_treino), 'Qtd dias testados': len(dados_teste), 'MAE': mae, 'WMAPE': f'{wmape_teste:.2%}', 'Tendência': trend, 'Sazonalidade': seasonal, 'Períodos Sazonais': seasonal_periods}
                    
                    # Criando um novo DataFrame com a nova linha
                    nova_linha_df = pd.DataFrame([nova_linha])
                    
                    # Adicionando nova linha ao DataFrame original usando concatenação
                    df_completo = pd.concat([df_completo, nova_linha_df], ignore_index=True)

                # Atualizando os melhores parâmetros se este conjunto tiver um MAE menor
                if mae < melhor_mae:
                    melhor_mae = mae
                    melhores_parametros = {'trend': trend, 'seasonal': seasonal, 'seasonal_periods': seasonal_periods}
                    melhores_dados_treinamento = dados_treino
                    melhores_dados_teste = dados_teste
                    melhor_resultado_fit = resultado
                    melhor_wmape = wmape_teste

    return melhor_mae, melhores_parametros, melhores_dados_teste, melhores_dados_treinamento, melhor_resultado_fit, melhor_wmape,df_completo

# Armazenamento do modelo em cache
@st.cache_resource
# Modelo ETS para previsão dos dias, utilizando qtd de dias recentes para treinamento, qtd de dias que deseja prever e, os parâmetros de tendência e sazonalidade
def modelo_ets_previsao(dados, qt_dias_historico, qt_dias_prever, trend, seasonal):
    dados = dados.tail(qt_dias_historico)

    # Criando o modelo ETS
    modelo_ets = ExponentialSmoothing(dados['Preco'], trend=trend, seasonal=seasonal, seasonal_periods=30)

    # Treinando o modelo
    resultado = modelo_ets.fit()

    # Fazendo previsões
    previsao = resultado.forecast(steps=qt_dias_prever)

    return previsao

# Futuros dias úteis da semana
def dias_uteis_futuros(data_inicial,qtd_dias):
  dias_uteis = []
  while len(dias_uteis) < qtd_dias:
      # Avança um dia de cada vez
      data_inicial += timedelta(days=1)  
      # Verifica se o dia da semana não é sábado (5) nem domingo (6)
      if data_inicial.weekday() not in [5, 6]:
          dias_uteis.append(data_inicial)
  return dias_uteis

# Gráfico de linha com marcação dos picos máximos e mínimos dos preços
def graf_marcado_max_min(dados):
    # Encontrar índice do maior e menor Preco
    indice_maior_preco = dados['Preco'].idxmax()
    indice_menor_preco = dados['Preco'].idxmin()

    # Plotar o gráfico
    fig = go.Figure()

    # Adicionar dados de linha
    fig.add_trace(go.Scatter(x=dados['Data'], y=dados['Preco'], mode='lines',showlegend=False))

    # Adicionar pico máximo
    fig.add_trace(go.Scatter(x=[dados['Data'].loc[indice_maior_preco]], y=[dados['Preco'].loc[indice_maior_preco]],
                            mode='markers', name='Máximo', marker=dict(color='red', size=10)))

    # Adicionar pico mínimo
    fig.add_trace(go.Scatter(x=[dados['Data'].loc[indice_menor_preco]], y=[dados['Preco'].loc[indice_menor_preco]],
                            mode='markers', name='Mínimo', marker=dict(color='green', size=10)))

    # Atualizar layout do gráfico
    fig.update_layout(title='Preço por barril de Petróleo ao longo do tempo',
                    xaxis_title='Data', yaxis_title='Preço (US$)',legend=dict(orientation='h', y=1.15, x=0.5, xanchor='center', yanchor='top'))
    
    return fig

# Gráfico de dois eixos, com multiplas marcações de picos mínimos e máximos ao longo do tempo
def graf_marcado_multiplos(x, y, picos_indices_max, picos_indices_min,y2):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Preço do barril de Petróleo (US$)'))

    # Adiciona a série de picos mais altos apenas uma vez
    if np.any(picos_indices_max):
        x_max = [x[i] for i in picos_indices_max]
        y_max = [y[i] for i in picos_indices_max]
        fig.add_trace(go.Scatter(x=x_max, y=y_max, mode='markers', name='Máximos', marker=dict(color='red', size=10)))

    # Adiciona a série de picos mais baixos apenas uma vez
    if np.any(picos_indices_min):
        x_min = [x[i] for i in picos_indices_min]
        y_min = [y[i] for i in picos_indices_min]
        fig.add_trace(go.Scatter(x=x_min, y=y_min, mode='markers', name='Mínimos', marker=dict(color='green', size=10)))

    fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='Taxa de Câmbio (R$/US$)', yaxis='y2'))

    fig.update_layout( title='Preço do barril de Petróleo x Taxa de Câmbio',
        yaxis=dict(title='Preço do barril de Petróleo (US$)', side='left'),
        yaxis2=dict(title='Taxa de Câmbio (R$/US$)', overlaying='y', side='right'),
        legend=dict(orientation='h', y=1.15, x=0.5, xanchor='center', yanchor='top')
    )
    return fig

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

def modelo_previsao_prophet(df_preco):
    # Configurando o TimeSeriesSplit
    n_splits = 5  # Número de divisões para validação cruzada
    tscv = TimeSeriesSplit(n_splits=n_splits)

    # Armazenando resultados
    results_prophet = []

    # Validação cruzada
    for fold, (train_index, val_index) in enumerate(tscv.split(df_preco)):
        # Dividindo os dados em treino e validação
        treino = df_preco.iloc[train_index]
        valid = df_preco.iloc[val_index]

        # Criando e ajustando o modelo Prophet
        model = Prophet(daily_seasonality=True, yearly_seasonality=True)
        model.fit(treino)

        # Prevendo para o conjunto de validação
        forecast = model.predict(valid[['ds']])
        valid = valid.merge(forecast[['ds', 'yhat']], on='ds')

        # Calculando as métricas
        mae = mean_absolute_error(valid['y'], valid['yhat'])
        wmape_value = np.sum(np.abs(valid['y'] - valid['yhat'])) / np.sum(valid['y'])
        mape = np.mean(np.abs((valid['y'] - valid['yhat']) / valid['y'])) * 100

        results_prophet.append({
            'fold': fold + 1,
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

def modelo_previsao_ARIMA(df_preco):
    # Configurando o TimeSeriesSplit
    n_splits = 5
    tscv = TimeSeriesSplit(n_splits=n_splits)

    # Armazenando os resultados
    results_arima = []

    for fold, (train_index, val_index) in enumerate(tscv.split(df_preco)):
        print(f"Treinando o Fold {fold + 1}...")

        train_data = df_preco.iloc[train_index]['y']
        val_data = df_preco.iloc[val_index]['y']

        # Seleção automática de parâmetros
        auto_arima_model = auto_arima(train_data, seasonal=False, stepwise=True, trace=False)

        # Obtendo os melhores parâmetros
        p, d, q = auto_arima_model.order
        print(f"Parâmetros otimizados para o Fold {fold + 1}: p={p}, d={d}, q={q}")

        # Treinando o modelo ARIMA
        arima_model = ARIMA(train_data, order=(p, d, q))
        arima_fitted = arima_model.fit()

        # Fazendo previsões
        y_val_pred = arima_fitted.forecast(steps=len(val_data))

        # Calculando métricas
        mae = mean_absolute_error(val_data, y_val_pred)
        wmape_value = np.sum(np.abs(val_data - y_val_pred)) / np.sum(val_data)
        mape = np.mean(np.abs((val_data - y_val_pred) / val_data)) * 100

        results_arima.append({
            'fold': fold + 1,
            'MAE': mae,
            'WMAPE': wmape_value,
            'MAPE': mape
        })

    results_df = pd.DataFrame(results_arima)
    print("\nResultados da validação cruzada:")
    print(results_df)

    # Treinando o modelo final
    final_arima_model = auto_arima(df_preco['y'], seasonal=False, stepwise=True).fit(df_preco['y'])
    future_predictions = final_arima_model.predict(n_periods=90)

    # Datas futuras
    last_date = df_preco['ds'].max()
    future_dates = pd.date_range(last_date + pd.Timedelta(days=1), periods=90, freq='D')

    # Resultado final
    future_forecast_df = pd.DataFrame({'ds': future_dates, 'yhat': future_predictions})

    return future_forecast_df

