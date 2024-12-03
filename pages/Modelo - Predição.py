# Importação das bibliotecas
import streamlit as st
import pandas as pd
from utils import modelo_previsao_prophet,tratando_dados,importacao_dados_previsao,plot_previsao,plot_previsao_10_meses,modelo_previsao_ARIMA,metricas_utilizadas

# Configuração da página
st.set_page_config(page_title= 'Modelo - Predição', layout='wide', page_icon= ':fuelpump:')

# Título da página e descrição introdutória do modelo escolhido, parâmetros e performance
st.title('Modelo Preditivo :telescope: ⚡')

# Leitura dos dados de petróleo com WebScraping
url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'
df = importacao_dados_previsao(url)

# Tratando os dados coletados para retornar o df que será usado nas predições
df_preco = tratando_dados(df)

st.markdown('<h3>Modelos preditivos utilizados no estudo </h3>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"> Para trazer uma previsão do preço do petróleo para o cliente, a empresa DataPro construiu alguns modelos, com diferentes técnicas, para avaliar a que mais atende. As técnicas escolhidas pela DataPro foram:</p>', unsafe_allow_html = True)

st.markdown('<h5>1. ARIMA </h5>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"> O modelo ARIMA (AutoRegressive Integrated Moving Average) é uma técnica de análise de séries temporais usada para prever dados que variam ao longo do tempo. Bastante utilizado em estatística e econometria para previsão e modelagem de dados temporais, ele combina três componentes principais:</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">AutoRegressivo (AR):</span>Captura a relação entre uma observação e um número definido de observações anteriores;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Integrado (I):</span>Representa a diferenciação dos dados para torná-los estacionários, ou seja, com propriedades estatísticas constantes ao longo do tempo;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Média Móvel (MA):</span>Molda a dependência entre uma observação e o erro de previsão de um número definido de observações anteriores.</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"> Essa combinação ajuda a capturar padrões e tendências nos dados, fornecendo uma base sólida para previsões futuras.</p>', unsafe_allow_html = True)

st.markdown('<h5>2. PROPHET </h5>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"> Desenvolvido pela Meta, é um modelo de previsão projetado para lidar com séries temporais que exibem tendências e sazonalidades.É particularmente útil para dados que possuem padrões sazonais e mudanças de tendência, e é desenhado para ser robusto a faltas de dados e a mudanças bruscas no comportamento da série. Ele utiliza o modelo de séries temporais decomposto com três componentes principais: tendência (g), sazonalidade (s) e feriados (h), combinados na seguinte equação:</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">y(t)=g(t)+s(t)+h(t)+εt</span></p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"> Uma ferramenta poderosa para previsão de séries temporais, especialmente quando se trata de dados com padrões sazonais complexos e mudanças de tendência, sua flexibilidade e robustez o tornam uma escolha popular para muitos problemas de previsão.</p>', unsafe_allow_html = True)



st.subheader('Escolha um tipo de modelo preditivo abaixo: ')

opcao = st.radio(
    "Selecione uma das opções abaixo:",
    ("Prophet", "ARIMA")
)


# Execução da lógica com base na escolha
if opcao == "Prophet":
    metricas_utilizadas()

    # Aplicando o dataframe após o tratamento para treinar o modelo usando o Prophet
    future_forecast = modelo_previsao_prophet(df_preco)

    # Plotando o resultado 
    plot_previsao(df_preco,future_forecast)

    # Plotando o resultado dos últimos 10 meses + os próximos 90 dias previstos
    plot_previsao_10_meses(df_preco,future_forecast)
elif opcao == "ARIMA":
    metricas_utilizadas()

    # Aplicando o dataframe após o tratamento para treinar o modelo usando o ARIMA
    future_forecast = modelo_previsao_ARIMA(df_preco)

    # Plotando o resultado 
    plot_previsao(df_preco,future_forecast)

    # Plotando o resultado dos últimos 10 meses + os próximos 90 dias previstos
    plot_previsao_10_meses(df_preco,future_forecast)