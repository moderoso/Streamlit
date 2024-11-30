# Importação da biblioteca streamlit
import streamlit as st

# Configuração da página
st.set_page_config(page_title= 'Projeto ML preço do Petróleo', layout='wide', page_icon= ':fuelpump:')

# Título da página
st.title('Projeto ML preço do Petróleo 🛠️')

# Descrição do projeto
st.markdown('<p style="text-align: justify;">A GalPreto, uma empresa líder no agenciamento de petróleo, busca otimizar as suas estratégias de mercado e prever flutuações de preço com maior precisão. Para isso, contratou a DataPro para desenvolver um dashboard interativo com visualizações intuitivas, insights em tempo real e um modelo de Machine Learning para previsão do preço do petróleo:</p>', unsafe_allow_html = True)
st.markdown('- Análise Exploratória')
st.markdown('- Desenvolvimento dashboard com os insights abaixo na ferramenta Streamlit')
st.markdown('- Desenvolvimento de um modelo Machine Learning')


# Visualização da fluxo de trabalho do projeto
#st.markdown('## Fluxo de Trabalho')
#miro_url = 'https://miro.com/app/live-embed/uXjVN1YW9H4=/?moveToViewport=-1349,-868,3306,1721&embedId=214115551426'
#st.markdown(f'<iframe width="80%" height="600" src="{miro_url}" frameborder="0" scrolling="no" allow="fullscreen; clipboard-read; clipboard-write" #allowfullscreen></iframe>', unsafe_allow_html=True)

# Links
#st.markdown('## Links Úteis')
#st.markdown('##### Fontes de dados')
#st.markdown('Link acessado em 20 novembro 2024   ' '[A história do petróleo no Brasil](https://www.gov.br/anp/pt-br/acesso-a-informacao/institucional/historia-petroleo-brasil)')
#st.markdown('Link acessado em 20 novembro 2024   ' '[Qual é a origem do petróleo?](https://www.bbc.com/portuguese/articles/cnk0e0yydelo)')
#st.markdown('Link acessado em 20 novembro 2024   ' '[OPEC]( https://www.opec.org/opec_web/en/index.htm)')
#st.markdown('Link acessado em 20 novembro 2024   ' '[OpenAI. “O Chat GPT é uma ferramenta de processamento de linguagem natural orientada por IA, que possibilita conversas semelhantes às humanas com o #chatbot](https://openai.com/blog/chat-gpt-3-launch/)')
#st.markdown('Link acessado em 20 novembro 2024   ' '[Geopolítica do Petróleo](https://mundoeducacao.uol.com.br/geografia/geopolitica-petroleo.html)') 
#st.markdown('Link acessado em 20 novembro 2024   ' '[Nos Bastidores da Terra: Geóloga Explica a Formação do #Petróleo](https://super.abril.com.br/coluna/deriva-continental/nos-bastidores-da-terra-geologa-explica-a-formacao-do-petroleo#google_vignette)')
#st.markdown('Link acessado em 20 novembro 2024   ' '[Organização dos Países Exportadores de Petróleo](https://pt.wikipedia.org/wiki/Organiza%C3%A7%C3%A3o_dos_Pa%C3%ADses_Exportadores_de_Petr%C3%B3leo)')
#st.markdown('Link acessado em 20 novembro 2024   ' '[Agência Internacional de Energia](https://pt.wikipedia.org/wiki/Ag%C3%AAncia_Internacional_de_Energia)')  
#st.markdown('Link acessado em 20 novembro 2024   ' '[Oito motivos para a queda do preço do  petróleo](https://www.dw.com/pt-br/oito-motivos-para-a-queda-do-pre%C3%A7o-do-petr%C3%B3leo/a-19051686)') 

st.markdown('<p style="text-align: justify;"><br /><br /><br /><br /></p>', unsafe_allow_html = True)



st.write("### Fontes de dados")
st.write("Links acessado em 20 novembro 2024"
         "\n* A história do petróleo no Brasil   https://www.gov.br/anp/pt-br/acesso-a-informacao/institucional/historia-petroleo-brasil"
         "\n* Qual é a origem do petróleo?  https://www.bbc.com/portuguese/articles/cnk0e0yydelo"
         "\n* OPEC  https://www.opec.org/opec_web/en/index.htm"
         "\n* OpenAI. “O Chat GPT é uma ferramenta de processamento de linguagem natural orientada por IA, que possibilita conversas semelhantes às humanas com o chatbot   https://openai.com/blog/chat-gpt-3-launch"
         "\n* Geopolítica do Petróle  https://mundoeducacao.uol.com.br/geografia/geopolitica-petroleo.html"
         "\n* Nos Bastidores da Terra: Geóloga Explica a Formação do Petróleo  https://super.abril.com.br/coluna/deriva-continental/nos-bastidores-da-terra-geologa-explica-a-formacao-do-petroleo#google_vignette"
         "\n* Organização dos Países Exportadores de Petróleo https://pt.wikipedia.org/wiki/Organiza%C3%A7%C3%A3o_dos_Pa%C3%ADses_Exportadores_de_Petr%C3%B3leo"
		 "\n* Agência Internacional de Energia   https://pt.wikipedia.org/wiki/Ag%C3%AAncia_Internacional_de_Energia"
         "\n* Oito motivos para a queda do preço do  petróleo  https://www.dw.com/pt-br/oito-motivos-para-a-queda-do-pre%C3%A7o-do-petr%C3%B3leo/a-19051686"
		 )

st.markdown('<p style="text-align: justify;"><br /><br /><br /><br /></p>', unsafe_allow_html = True)


# Equipe do projeto
st.write("### Equipe FIAP - 5DTAT - Grupo 10")
#st.markdown('<h5>Equipe FIAP - 5DTAT - Grupo 10</h5>', unsafe_allow_html = True)
st.markdown('#### Caio Vinicius Branco Gonçalves - RM 354248')
st.markdown('#### Jhonny da Silva Mineu - RM 355135')
st.markdown('#### Marina Mendez Araujo - RM 355100')
st.markdown('#### Mônada Raquel Brito de Oliveira - RM 354367')
st.markdown('#### Volmir Moderoso Santos - RM 355589')


