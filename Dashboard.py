# Importação das bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np

#from utils import atualiza_dados

# Configuração da página
st.set_page_config(page_title= 'Dashboard - Preço do Petróleo', layout='wide', page_icon= ':fuelpump:,📊 ')

# Título da página
st.title('Dashboard - Variação do Preço do Petróleo :fuelpump:')

# Botão para atualizar os dados da aplicação
#atualiza_dados()

# Webscraping dos dados de petróleo
#url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?serid=38590&module=M'
#coluna = 'Preco'
#dados_taxa = webscraping(url,coluna)

# Construção dos dataframes 
#@st.cache_data
#def get_dolar_data():
df_dolar = pd.read_csv('dolar.csv', encoding = "ISO-8859-1", sep=";")
df_dolar = df_dolar.drop(['Dia', 'Mês', 'Ano' ], axis=1)
df_dolar.head()

if st.checkbox('Show dataframe'):
	st.write(df_dolar)
	



# Construção dos dataframes 
dados_sem_dataindex = df_dolar
dados_sem_dataindex['Ano'] = dados_sem_dataindex['Data'].dt.year.astype(int)

media_mensal_anos = dados.groupby(pd.Grouper(freq= 'M'))[['Preco']].mean().reset_index() #Agrupando os dados por mês
media_mensal_anos['Ano'] = media_mensal_anos['Data'].dt.year.astype(int)
media_mensal_anos['Mes'] = media_mensal_anos['Data'].dt.month_name()

picos_preco = media_mensal_anos.set_index('Data').sort_values('Preco', ascending=False).head(10)

vales_preco = media_mensal_anos.set_index('Data').sort_values('Preco', ascending=True).head(10)


# Construção dos gráficos          
fig_picos_preco = px.bar(picos_preco,
                        x = picos_preco['Mes'].astype(str) + '/' + picos_preco['Ano'].astype(str),
                        y = 'Preco',
                        text_auto=True,
                        title= f'Top 10 meses com média de preços mais altos')
fig_picos_preco.update_xaxes(type='category')
fig_picos_preco.update_layout(xaxis_title= 'Data', yaxis_title = 'Preço (US$)')

fig_vales_preco = px.bar(vales_preco,
                        x = vales_preco['Mes'].astype(str) + '/' + vales_preco['Ano'].astype(str),
                        y = 'Preco',
                        text_auto=True,
                        title= f'Top 10 meses com média de preços mais baixos')
fig_vales_preco.update_xaxes(type='category')
fig_vales_preco.update_layout(xaxis_title= 'Data', yaxis_title = 'Preço (US$)')


# Visualização dos visuais no Streamlit
## Cartões
cor_estilizada = 'color: #0145AC;'
fonte_negrito = 'font-weight: bold;'

col1, col2, col3, col4 = st.columns(4)
with col1:
    metrica1 = dados.index.max().strftime('%d/%m/%Y')
    st.markdown(f"<h2 style='{cor_estilizada}'>{metrica1}</h2> <span style='{fonte_negrito}'> Dados atualizados até </span>", unsafe_allow_html=True)
    #st.metric('Dados atualizados até:', value=dados.index.max().strftime('%d/%m/%Y')) 
with col2: 
    metrica2 = dados.index.min().strftime('%d/%m/%Y')
    st.markdown(f"<h2 style='{cor_estilizada}'> {metrica2} </h2> <span style='{fonte_negrito}'> Dados monitorados desde</span> ", unsafe_allow_html=True) 
with col3:
    metrica3 = dados['Preco'].min()
    data_metrica3 = dados[dados['Preco']==dados['Preco'].min()].index
    st.markdown(f"<h2 style='{cor_estilizada}'> US$ {metrica3:.2f} </h2> <span style='{fonte_negrito}'> Menor preço histórico <br> (atingido em  {data_metrica3[0].strftime('%d/%m/%Y')})</span> ", unsafe_allow_html=True) 
    #st.metric('Menor preço histórico:', value=dados['Preco'].min().round(2))
with col4:
    metrica4 = dados['Preco'].max()
    data_metrica4 = dados[dados['Preco']==dados['Preco'].max()].index
    st.markdown(f"<h2 style='{cor_estilizada}'> US$ {metrica4:.2f} </h2> <span style='{fonte_negrito}'> Maior preço histórico <br> (atingido em  {data_metrica4[0].strftime('%d/%m/%Y')})</span> ", unsafe_allow_html=True)

st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

 # Select columns for the chart
#    x_column = st.selectbox("Select X-axis column", df_dolar.columns)
 #   y_column = st.selectbox("Select Y-axis column", df_dolar.columns)

    # Create the Seaborn chart
#    fig, ax = plt.subplots()  # Create a Matplotlib figure and axes
#    sns.scatterplot(x=x_column, y=y_column, data=df_dolar, ax=ax)  # Create the chart on the axes
#    st.pyplot(fig)  # Display the chart in Streamlit

# Data preparation (same as before)
#df_dolar['Data'] = pd.to_datetime(df_dolar['Data'], format='%d/%m/%Y')
#df_dolar['Dolar Comercia (R$)'] = df_dolar['Dolar Comercia (R$)'].astype(str).str.replace(',', '.').astype(float)

# Create the Plotly figure (same as before)
#fig = px.line(df_dolar, x="Data", y="Dolar Comercial (R$)")
#fig.update_layout(title="Dolar Comercial Over Time", xaxis_title="Date", yaxis_title="Dolar Comercial (R$)")

# Display the chart in Streamlit
#st.plotly_chart(fig)