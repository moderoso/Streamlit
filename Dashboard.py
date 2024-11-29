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
df_dolar.head()

if st.checkbox('Show dataframe'):
	st.write(df_dolar)
	

fig = px.line(df_dolar, x=df_dolar.index, y="Último")
fig.update_layout(title='Dolar Value',
                   xaxis_title='Date',
                   yaxis_title='Value')


st.plotly_chart(fig)

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