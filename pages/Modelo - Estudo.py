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
st.markdown('<p style="text-align: justify;">Esses fatores combinados geraram um desequilíbrio entre oferta e demanda, pressionando os preços para baixo ao longo desse período. Conforme os acontecimentos econômicos citados, é possível analisar que isso é um fator que impacta o aumento e a queda do valor do dólar.</p>', unsafe_allow_html = True)

#Adiciona Imagem na pagina
image = Image.open('images/petroleo_mundo.jpg')
st.image(image, caption='Petroleo no Mundo', width = 600)

st.markdown('<p style="text-align: justify;">A crise do petróleo de 1973 elevou os preços globais, e estimulou a exploração do recurso no Brasil. Durante este período, o Brasil investiu fortemente em tecnologia, incluindo a pesquisa em exploração offshore (em alto-mar).Em 2007, o Brasil fez a descoberta do pré-sal, um reservatório vasto de petróleo abaixo de uma camada de sal no fundo do oceano. Isso consolidou o Brasil como um importante produtor de petróleo, colocando-o entre os maiores exportadores do mundo.A Petrobras enfrentou crises políticas e econômicas nos últimos anos, incluindo investigações de corrupção (como a Lava Jato), o que afetou sua operação, mas mesmo assim, o Brasil continua sendo uma das principais potências petrolíferas globais.</p>', unsafe_allow_html = True)

st.markdown('<h3>Modelos preditivos utilizados no estudo </h3>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"> Para trazer uma previsão do preço do petróleo para o cliente, a empresa DataPro construiu alguns modelos, com diferentes técnicas, para avaliar a que mais atende. As técnicas escolhidas pela DataPro foram:</p>', unsafe_allow_html = True)

st.markdown('<h4>1. ARIMA </h4>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"> O modelo ARIMA (AutoRegressive Integrated Moving Average) é uma técnica de análise de séries temporais usada para prever dados que variam ao longo do tempo. Bastante utilizado em estatística e econometria para previsão e modelagem de dados temporais, ele combina três componentes principais:</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">AutoRegressivo (AR):</span>Captura a relação entre uma observação e um número definido de observações anteriores;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Integrado (I):</span>Representa a diferenciação dos dados para torná-los estacionários, ou seja, com propriedades estatísticas constantes ao longo do tempo;</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">Média Móvel (MA):</span>Molda a dependência entre uma observação e o erro de previsão de um número definido de observações anteriores.</p>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"> Essa combinação ajuda a capturar padrões e tendências nos dados, fornecendo uma base sólida para previsões futuras.</p>', unsafe_allow_html = True)

st.markdown('<h4>2. PROPHET </h4>', unsafe_allow_html = True)

st.markdown('<p style="text-align: justify;"> Desenvolvido pela Meta, é um modelo de previsão projetado para lidar com séries temporais que exibem tendências e sazonalidades.É particularmente útil para dados que possuem padrões sazonais e mudanças de tendência, e é desenhado para ser robusto a faltas de dados e a mudanças bruscas no comportamento da série. Ele utiliza o modelo de séries temporais decomposto com três componentes principais: tendência (g), sazonalidade (s) e feriados (h), combinados na seguinte equação:</p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"><span style="font-weight: bold">y(t)=g(t)+s(t)+h(t)+εt</span></p>', unsafe_allow_html = True)
st.markdown('<p style="text-align: justify;"> Uma ferramenta poderosa para previsão de séries temporais, especialmente quando se trata de dados com padrões sazonais complexos e mudanças de tendência, sua flexibilidade e robustez o tornam uma escolha popular para muitos problemas de previsão.</p>', unsafe_allow_html = True)











