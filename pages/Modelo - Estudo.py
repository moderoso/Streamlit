# Importação das bibliotecas
import streamlit as st
from statsmodels.tsa.seasonal import seasonal_decompose
from utils import decomposicao,teste_estatistico

# Configuração da página
st.set_page_config(page_title= 'Modelo - Decomposição e Análise', layout='wide', page_icon= ':fuelpump:')

# Título da página e estudo
st.title('Modelo - Estudo 📊')
st.markdown('<p style="text-align: justify;"> Com o contexto do petróleo e seu impacto no mundo, a DataPro realizou um estudo contendo informações relevantes para uma evolução dos indicadores pautada nos pontos de variações externas anteriormente explicadas, aplicando alguns algoritmos de previsibilidade para a obtenção dos preços médios. De acordo com o gráfico apresentado, é possível analisar o impacto dos eventos geopolíticos no preço do barril de petróleo. Durante a crise econômica de 2008/2009, o preço do petróleo sofreu uma queda acentuada devido à recessão global, que resultou em uma redução significativa na demanda por petróleo. A relutância dos membros da OPEP em ajustar suas cotas de produção exacerbou o desequilíbrio entre oferta e demanda, resultando em um excesso de oferta no mercado global e, consequentemente, uma queda substancial nos preços do petróleo. Entre os anos de 2014 e 2018, os preços do petróleo enfrentaram novos períodos de queda, impulsionados principalmente pela ascensão dos Estados Unidos como um dos maiores produtores de petróleo. Esse fenômeno resultou em diversos fatores que impactaram o mercado global de petróleo, incluindo:</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Diminuição da demanda e aumento da oferta para os Estados Unidos</span>, principal consumidor global de petróleo, devido ao aumento da produção interna;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Expansão da produção de petróleo pelo Iraque</span>que elevou a oferta global;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Retorno do Irã ao mercado internacional de petróleo</span>, após o acordo nuclear e a consequente remoção do embargo econômico imposto pelos Estados Unidos;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Aumento da produção nacional no Brasil</span>, com a exploração do pré-sal, o que reduziu a necessidade de importações de petróleo e ampliou a oferta interna;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Resistência da OPEP em reduzir a produção</span>, o que manteve a oferta superior à demanda no mercado global, contribuindo para a queda dos preços.</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;">Esses fatores combinados geraram um desequilíbrio entre oferta e demanda, pressionando os preços para baixo ao longo desse período.</p>', unsafe_allow_html = True)




st.subheader('Modelo de Decomposição')



st.subheader('Período Sazonal')
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Sazonalidade diária:</span> Análise das variações diárias utilizando o parâmetro period=1.</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Sazonalidade semanal:</span> Padrões que se repetem semanalmente. Por exemplo, em dados de tráfego da web, pode haver flutuações sazonais dependendo do dia da semana. O período sazonal associado seria 7 dias.</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Sazonalidade mensal:</span> Variações que ocorrem a cada mês. Muitos fenômenos naturais e comportamentais exibem sazonalidade mensal, como vendas sazonais em certas indústrias, flutuações na demanda por energia elétrica, etc. O período sazonal associado seria 30 dias (em média).</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Sazonalidade anual:</span> Padrões que se repetem anualmente. Por exemplo, em dados climáticos, podemos observar variações sazonais nas temperaturas ao longo das estações do ano. O período sazonal associado seria 365 dias.</p>', unsafe_allow_html = True)

# Leitura dos dados de petróleo gravados no BigQuery
#tabela_bq = 'tb_preco_petroleo'
#dados = select_bq(tabela_bq)

# Agrupamento dos dados em semanal, mensal e diário
#df_semanal = dados.resample('W')['Preco'].mean()
#df_mensal = dados.resample('M')['Preco'].mean()
#df_anual = dados.resample('Y')['Preco'].mean()

# Seleção do modelo de decomposição e período sazonal
#modelo = st.sidebar.selectbox("Selecione o modelo de decomposição", ['Multiplicativo','Aditivo'])
#formato = st.sidebar.selectbox("Selecione o período sazonal", ['1','7','30','365'])

# Para cada combinação de seleção, é apresentado as análises de decomposição, teste estatístico e gráficos de autocorrelação
if (modelo == 'Multiplicativo' and formato == '1'):
    st.markdown('<h2> Sazonalidade diária com decomposição multiplicativa </h2>', unsafe_allow_html = True)
    result_mult_diaria = seasonal_decompose(dados, period = 1, model='multiplicative')
    decomposicao(dados,result_mult_diaria)
    string_teste = 'Resultado referente aos dados diários do preço do petróleo:'
    teste_estatistico(dados,string_teste)
    st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Séries Temporais Diárias:</span> Para séries temporais diárias, podem ser observados lags significativos no ACF e PACF em torno de múltiplos de 7 (uma semana), indicando padrões semanais de autocorrelação devido a comportamentos repetitivos que ocorrem a cada semana. Além disso, para séries temporais diárias, também podem ser observados lags significativos em torno de 30 (um mês), indicando padrões mensais de autocorrelação.</p>', unsafe_allow_html = True)

elif (modelo == 'Aditivo' and formato == '1'):
    st.markdown('<h2> Sazonalidade diária com decomposição aditiva </h2>', unsafe_allow_html = True)
    result_adit_diaria = seasonal_decompose(dados, period = 1, model='aditive')
    decomposicao(dados,result_adit_diaria)   
    string_teste = 'Resultado referente aos dados diários do preço do petróleo:'
    teste_estatistico(dados,string_teste)
    st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Séries Temporais Diárias:</span> Para séries temporais diárias, podem ser observados lags significativos no ACF e PACF em torno de múltiplos de 7 (uma semana), indicando padrões semanais de autocorrelação devido a comportamentos repetitivos que ocorrem a cada semana. Além disso, para séries temporais diárias, também podem ser observados lags significativos em torno de 30 (um mês), indicando padrões mensais de autocorrelação.</p>', unsafe_allow_html = True)

elif (modelo == 'Multiplicativo' and formato == '7'):
    st.markdown('<h2> Sazonalidade semanal com decomposição multiplicativa </h2>', unsafe_allow_html = True)
    result_mult_diaria = seasonal_decompose(dados, period = 7, model='multiplicative')
    decomposicao(dados,result_mult_diaria)
    string_teste = 'Resultado referente a média semanal do preço do petróleo:'
    teste_estatistico(df_semanal,string_teste)
    st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Séries Temporais Semanais:</span> Para séries temporais semanais, podem ser observados lags significativos no ACF e PACF em torno de múltiplos de 4 (um mês), indicando padrões mensais de autocorrelação. Além disso, lags em torno de 52 (um ano) podem ser observados para capturar padrões anuais de autocorrelação.</p>', unsafe_allow_html = True)

elif (modelo == 'Aditivo' and formato == '7'):
    st.markdown('<h2> Sazonalidade semanal com decomposição aditiva </h2>', unsafe_allow_html = True)
    result_adit_diaria = seasonal_decompose(dados, period = 7, model='aditive')
    decomposicao(dados,result_adit_diaria)
    string_teste = 'Resultado referente a média semanal do preço do petróleo:'
    teste_estatistico(df_semanal,string_teste)
    st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Séries Temporais Semanais:</span> Para séries temporais semanais, podem ser observados lags significativos no ACF e PACF em torno de múltiplos de 4 (um mês), indicando padrões mensais de autocorrelação. Além disso, lags em torno de 52 (um ano) podem ser observados para capturar padrões anuais de autocorrelação.</p>', unsafe_allow_html = True)

elif (modelo == 'Multiplicativo' and formato == '30'):
    st.markdown('<h2> Sazonalidade mensal com decomposição multiplicativa </h2>', unsafe_allow_html = True)
    result_mult_diaria = seasonal_decompose(dados, period = 30, model='multiplicative')
    decomposicao(dados,result_mult_diaria)
    string_teste = 'Resultado referente a média mensal do preço do petróleo:'
    teste_estatistico(df_mensal,string_teste)
    st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Séries Temporais Mensais:</span> Para séries temporais mensais, lags em torno de 12 (um ano) podem ser frequentemente ressaltados no ACF e PACF, indicando padrões anuais de autocorrelação. Além disso, para séries mensais, também podem ser observados lags em torno de 6 (meio ano) devido a sazonalidades semestrais.</p>', unsafe_allow_html = True)

elif (modelo == 'Aditivo' and formato == '30'):
    st.markdown('<h2> Sazonalidade mensal com decomposição aditiva </h2>', unsafe_allow_html = True)
    result_adit_diaria = seasonal_decompose(dados, period = 30, model='aditive')
    decomposicao(dados,result_adit_diaria) 
    string_teste = 'Resultado referente a média mensal do preço do petróleo:'
    teste_estatistico(df_mensal,string_teste)
    st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Séries Temporais Mensais:</span> Para séries temporais mensais, lags em torno de 12 (um ano) podem ser frequentemente ressaltados no ACF e PACF, indicando padrões anuais de autocorrelação. Além disso, para séries mensais, também podem ser observados lags em torno de 6 (meio ano) devido a sazonalidades semestrais.</p>', unsafe_allow_html = True)

elif (modelo == 'Multiplicativo' and formato == '365'):
    st.markdown('<h2> Sazonalidade anual com decomposição multiplicativa </h2>', unsafe_allow_html = True)
    result_mult_diaria = seasonal_decompose(dados, period = 365, model='multiplicative')
    decomposicao(dados,result_mult_diaria)
    string_teste = 'Resultado referente a média anual do preço do petróleo:'
    teste_estatistico(df_anual,string_teste)
    st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Séries Temporais Anuais:</span> Para séries temporais anuais, podem ser observados lags em torno de 1 (um ano) no ACF e PACF, indicando autocorrelação anual. Além disso, podem ser observados lags em torno de 5 (cinco anos) para capturar padrões de autocorrelação de longo prazo. </p>', unsafe_allow_html = True)

elif (modelo == 'Aditivo' and formato == '365'):
    st.markdown('<h2> Sazonalidade anual com decomposição aditiva </h2>', unsafe_allow_html = True)
    result_adit_diaria = seasonal_decompose(dados, period = 365, model='aditive')
    decomposicao(dados,result_adit_diaria)
    string_teste = 'Resultado referente a média anual do preço do petróleo:'
    teste_estatistico(df_anual,string_teste)
    st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Séries Temporais Anuais:</span> Para séries temporais anuais, podem ser observados lags em torno de 1 (um ano) no ACF e PACF, indicando autocorrelação anual. Além disso, podem ser observados lags em torno de 5 (cinco anos) para capturar padrões de autocorrelação de longo prazo. </p>', unsafe_allow_html = True)