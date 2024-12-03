# Importação das bibliotecas
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
#from vega_datasets import data

from statsmodels.tsa.seasonal import seasonal_decompose
from PIL import Image
from utils import importacao_dados_previsao

# Configuração da página
st.set_page_config(page_title= 'Modelo - Decomposição e Análise', layout='wide', page_icon= ':fuelpump:')

# Título da página e estudo
st.title('Modelo - Estudo 📊')

#Texto sobre o estudo
st.markdown('<p style="text-align: justify;"> Com o contexto do petróleo e seu impacto no mundo, a DataPro realizou um estudo contendo informações relevantes para uma evolução dos indicadores pautada nos pontos de variações externas anteriormente explicadas, aplicando alguns algoritmos de previsibilidade para a obtenção dos preços médios. De acordo com o gráfico apresentado, é possível analisar o impacto dos eventos geopolíticos no preço do barril de petróleo. Durante a crise econômica de 2008/2009, o preço do petróleo sofreu uma queda acentuada devido à recessão global, que resultou em uma redução significativa na demanda por petróleo. A relutância dos membros da OPEP em ajustar suas cotas de produção exacerbou o desequilíbrio entre oferta e demanda, resultando em um excesso de oferta no mercado global e, consequentemente, uma queda substancial nos preços do petróleo. Entre os anos de 2014 e 2018, os preços do petróleo enfrentaram novos períodos de queda, impulsionados principalmente pela ascensão dos Estados Unidos como um dos maiores produtores de petróleo. Esse fenômeno resultou em diversos fatores que impactaram o mercado global de petróleo, incluindo:</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Diminuição da demanda e aumento da oferta para os Estados Unidos</span>, principal consumidor global de petróleo, devido ao aumento da produção interna;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Expansão da produção de petróleo pelo Iraque</span>, que elevou a oferta global;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Retorno do Irã ao mercado internacional de petróleo</span>, após o acordo nuclear e a consequente remoção do embargo econômico imposto pelos Estados Unidos;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Aumento da produção nacional no Brasil</span>, com a exploração do pré-sal, o que reduziu a necessidade de importações de petróleo e ampliou a oferta interna;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Resistência da OPEP em reduzir a produção</span>, o que manteve a oferta superior à demanda no mercado global, contribuindo para a queda dos preços.</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;">Esses fatores combinados geraram um desequilíbrio entre oferta e demanda, pressionando os preços para baixo ao longo desse período. Conforme os acontecimentos econômicos citados, é possível analisar que isso é um fator que impacta o aumento e a queda do valor do dólar.</p>', unsafe_allow_html = True)

#Adiciona Imagem na pagina
image = Image.open('images/petroleo_mundo.png')
st.image(image, caption='Petroleo no Mundo', width = 600)


#Texto sobre o estudo
st.markdown('<p style="text-align: justify;">A crise do petróleo de 1973 elevou os preços globais, e estimulou a exploração do recurso no Brasil. Durante este período, o Brasil investiu fortemente em tecnologia, incluindo a pesquisa em exploração offshore (em alto-mar).Em 2007, o Brasil fez a descoberta do pré-sal, um reservatório vasto de petróleo abaixo de uma camada de sal no fundo do oceano. Isso consolidou o Brasil como um importante produtor de petróleo, colocando-o entre os maiores exportadores do mundo.A Petrobras enfrentou crises políticas e econômicas nos últimos anos, incluindo investigações de corrupção (como a Lava Jato), o que afetou sua operação, mas mesmo assim, o Brasil continua sendo uma das principais potências petrolíferas globais.</p>', unsafe_allow_html = True)

st.markdown('<h3>Formação preço do petróleo</h3>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;">O preço do petróleo é determinado por uma complexa interação de fatores econômicos, geopolíticos e até mesmo eventos climáticos. Até mesmo baseado no na flutuação do valor em dólar cobrado mundialmente. A lei da oferta e da demanda é o princípio fundamental que rege esse mercado, mas outros elementos também desempenham um papel crucial.</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Oferta e Demanda:</span> Oferta: A quantidade de petróleo produzido e disponível no mercado influencia diretamente o preço. Fatores como descobertas de novas reservas, investimentos em exploração e produção, políticas governamentais e capacidade de produção dos países exportadores impactam a oferta.<br />Demanda: O consumo global de petróleo, impulsionado principalmente pelo setor de transporte e pela indústria, exerce uma forte pressão sobre os preços. O crescimento econômico mundial, a eficiência energética e o desenvolvimento de fontes de energia alternativas influenciam a demanda.</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Organização dos Países Exportadores de Petróleo (OPEP):</span> A OPEP, composta por países com grandes reservas de petróleo, possui um papel fundamental na regulação da oferta global. Através de acordos de produção, a organização busca estabilizar os preços do petróleo, influenciando significativamente o mercado.</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Agência Internacional de Energia (IEA):</span> É uma organização internacional com sede em Paris, ligada à Organização para a Cooperação e Desenvolvimento Econômico (OCDE). A IEA atua como uma espécie de "orientadora política" para seus 30 países membros (todos economias desenvolvidas).</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Geopolítica:</span> Conflitos em regiões produtoras de petróleo, sanções econômicas, instabilidade política e mudanças nos regimes de governo podem causar interrupções no fornecimento e levar a aumentos nos preços.</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Dólar Americano:</span> O petróleo é negociado em dólares americanos no mercado internacional. A valorização do dólar tende a tornar o petróleo mais caro para os compradores que utilizam outras moedas, o que pode pressionar os preços para cima.</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Estoques:</span> Os níveis de estoque de petróleo nos países consumidores e produtores também influenciam os preços. Estoques elevados podem indicar uma oferta abundante e pressionar os preços para baixo, enquanto estoques baixos podem sinalizar uma oferta restrita e levar a aumentos nos preços.</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Especulação:</span> Investidores e especuladores podem influenciar os preços do petróleo através de suas atividades nos mercados futuros. A compra e venda de contratos futuros sobre petróleo podem amplificar as oscilações de preços.</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Eventos Imprevistos:</span> Desastres naturais, como furacões e terremotos, podem interromper a produção de petróleo e causar aumentos nos preços. Além disso, novas descobertas de grandes reservas ou avanços tecnológicos na produção também podem impactar o mercado.</p>', unsafe_allow_html = True)

st.markdown('<h3>Modelos preditivos utilizados no estudo </h3>', unsafe_allow_html = True)


# Webscraping dos dados de petróleo
url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'

# Construção dos dataframes 
df_dolar = pd.read_csv('Valor_Dolar_US.csv', encoding = "UTF-8", sep=";")
df_dolar.rename(columns={"Data":"Data", "Taxa de câmbio - R$ / US$ - comercial - compra - média":"Valor Dolar"},inplace=True)
#df_dolar.sort_values(by='Valor Dolar', ascending=True)

df_dolar['Data'] = pd.to_datetime(df_dolar['Data'],format="%d/%m/%Y")
df_dolar['Valor Dolar'] = pd.to_numeric(df_dolar['Valor Dolar'])

df_petroleo = importacao_dados_previsao(url)
df_petroleo.rename(columns={"Data":"Data", "Preço - petróleo bruto - Brent (FOB)":"Valor Petroleo"},inplace=True)
#df_petroleo.sort_values(by='Valor Petroleo', ascending=True)

df_petroleo['Data'] = pd.to_datetime(df_petroleo['Data'],format="%d/%m/%Y")
df_petroleo['Valor Petroleo'] = pd.to_numeric(df_petroleo['Valor Petroleo'])
#setting palette
colors_dolar=['#000099','#6f5f6f']

dolar_chart = px.bar(df_dolar, x='Data', y='Valor Dolar',
              opacity= .8,
              orientation='v',
              color_discrete_sequence=colors_dolar,
              title='Valor Médio Dolar ao longo do tempo',
              )
st.plotly_chart(dolar_chart, theme="streamlit", use_container_width=True)


#setting palette
colors=['#1A8A41','#521052']

petro_chart = px.bar(df_petroleo, x='Data', y='Valor Petroleo',
#              opacity= 1,
#              category_orders='Data',
			  color_discrete_sequence=colors,
              title='Valor Médio Petroleo ao longo do tempo',)
st.plotly_chart(petro_chart, theme="streamlit", use_container_width=True)







