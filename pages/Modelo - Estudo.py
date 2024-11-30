# Importação das bibliotecas
import streamlit as st
from statsmodels.tsa.seasonal import seasonal_decompose
from utils import decomposicao,teste_estatistico
from PIL import Image

# Configuração da página
st.set_page_config(page_title= 'Modelo - Decomposição e Análise', layout='wide', page_icon= ':fuelpump:')

# Título da página e estudo
st.title('Modelo - Estudo 📊')
st.markdown('<p style="text-align: justify;"> Com o contexto do petróleo e seu impacto no mundo, a DataPro realizou um estudo contendo informações relevantes para uma evolução dos indicadores pautada nos pontos de variações externas anteriormente explicadas, aplicando alguns algoritmos de previsibilidade para a obtenção dos preços médios. De acordo com o gráfico apresentado, é possível analisar o impacto dos eventos geopolíticos no preço do barril de petróleo. Durante a crise econômica de 2008/2009, o preço do petróleo sofreu uma queda acentuada devido à recessão global, que resultou em uma redução significativa na demanda por petróleo. A relutância dos membros da OPEP em ajustar suas cotas de produção exacerbou o desequilíbrio entre oferta e demanda, resultando em um excesso de oferta no mercado global e, consequentemente, uma queda substancial nos preços do petróleo. Entre os anos de 2014 e 2018, os preços do petróleo enfrentaram novos períodos de queda, impulsionados principalmente pela ascensão dos Estados Unidos como um dos maiores produtores de petróleo. Esse fenômeno resultou em diversos fatores que impactaram o mercado global de petróleo, incluindo:</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Diminuição da demanda e aumento da oferta para os Estados Unidos</span>, principal consumidor global de petróleo, devido ao aumento da produção interna;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Expansão da produção de petróleo pelo Iraque</span>, que elevou a oferta global;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Retorno do Irã ao mercado internacional de petróleo</span>, após o acordo nuclear e a consequente remoção do embargo econômico imposto pelos Estados Unidos;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Aumento da produção nacional no Brasil</span>, com a exploração do pré-sal, o que reduziu a necessidade de importações de petróleo e ampliou a oferta interna;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Resistência da OPEP em reduzir a produção</span>, o que manteve a oferta superior à demanda no mercado global, contribuindo para a queda dos preços.</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;">Esses fatores combinados geraram um desequilíbrio entre oferta e demanda, pressionando os preços para baixo ao longo desse período.</p>', unsafe_allow_html = True)

#Adiciona Imagem na pagina
image = Image.open('images/petroleo_mundo.jpg')
st.image(image, caption='Petroleo no Mundo', width = 600)

st.write("### Credits")
st.write("The Lottie animation, found on lottiefiles.com are "
         "\n* from Suhayra Sarwar   https://lottiefiles.com/90021-graph-stats"
         "\n* from Nirdhum Narayan  https://lottiefiles.com/99430-statistics"
         "\n* from Nirdhum Narayan  https://lottiefiles.com/99500-company-statistic-graph"
         "\n* from Ilya Pavlov   https://lottiefiles.com/8586-rocket-in-space"
         )



