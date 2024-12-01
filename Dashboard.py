# Importação das bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np
import matplotlib as plt 

import altair as alt

from utils import importacao_dados_previsao, tratando_dados

# Configuração da página
st.set_page_config(page_title= 'Dashboard - Preço do Petróleo', layout='wide', page_icon= ':fuelpump:,📊 ')

# Título da página
st.title('Dashboard - Variação do Preço do Petróleo :fuelpump:')

# Botão para atualizar os dados da aplicação
#atualiza_dados()

# Webscraping dos dados de petróleo
url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'

# Construção dos dataframes 
df_dolar = pd.read_csv('Valor_Dolar.csv', encoding = "UTF-8", sep=";")
df_dolar.head()

df_datas_relevantes = pd.read_csv('Eventos_Relevantes_Petroleo.csv', encoding = "UTF-8", sep=";")
df_datas_relevantes.head()

df_prod_pretoleo = pd.read_csv('Producao_Petroleo_Anual.csv', encoding = "ISO-8859-1", sep=";")
df_prod_pretoleo.head()

df = importacao_dados_previsao(url)
df_preco = tratando_dados(df)
df_preco.rename(columns={"ds":"Data", "y":"Valor"},inplace=True)

# Imprimindo dataframe na tela
st.dataframe(df_datas_relevantes)

# Inserindo barra para filtrar os anos
anos = df_preco['Data'].dt.year.unique()
anos_selecionados = st.slider("Selecione o intervalo de anos", 
                              min_value=int(anos.min()), 
                              max_value=int(anos.max()), 
                              value=(int(anos.min()), int(anos.max())))

# Filtrando o dataframe com base nos anos selecionados
df_filtrado = df_preco[(df_preco['Data'].dt.year >= anos_selecionados[0]) & 
                       (df_preco['Data'].dt.year <= anos_selecionados[1])]




# PLOTANDO OS 4 CARDS DO DASHBOARD

col1, col2, col3, col4 = st.columns(4)

# Maior valor do ano atual
ano_atual = pd.Timestamp.now().year
df_atual = df_preco[df_preco['Data'].dt.year == ano_atual]
maior_valor_atual = df_atual['Valor'].max()
col1.metric("Maior Valor (Ano Atual)", f"${maior_valor_atual:.2f}")

# Data do último registro
ultima_data = df_preco['Data'].max()
col2.metric("Última Data Registrada", ultima_data.strftime('%d/%m/%Y'))

# Maior valor do período filtrado
maior_valor_filtrado = df_filtrado['Valor'].max()
col3.metric("Maior Valor (Período)", f"${maior_valor_filtrado:.2f}")

# Menor valor do período filtrado
menor_valor_filtrado = df_filtrado['Valor'].min()
col4.metric("Menor Valor (Período)", f"${menor_valor_filtrado:.2f}")






# PLOTANDO GRÁFICO COM A EVOLUÇÃO E OS EVENTOS RELEVANTES AO LONGO DO TEMPO

# Criando o gráfico
fig, ax = plt.pyplot.subplots(figsize=(10, 6))

# Plotando a evolução diária do preço
ax.plot(df_filtrado['Data'], df_filtrado['Valor'], label='Preço Diário', color='blue')

# Adicionando os eventos no gráfico
for _, row in df_datas_relevantes.iterrows():
    ax.scatter(row['Inicio Mês'], row['Valor'], color='red', label=row['evento'])
    ax.text(row['Inicio Mês'], row['Valor'], row['evento'], fontsize=8, ha='right')

# Configurações do gráfico
ax.set_title("Evolução do Preço do Petróleo com Eventos Relevantes")
ax.set_xlabel("Data")
ax.set_ylabel("Preço ($)")
ax.legend()

# Exibindo o gráfico no Streamlit
st.pyplot(fig)




# PLOTANDO GRÁFICO DE LINHAS COM MAIOR E MENOR VALOR DINÂMICOS

# Encontrando os valores extremos no período filtrado
data_maior_valor = df_filtrado[df_filtrado['Valor'] == maior_valor_filtrado]['Data'].iloc[0]
data_menor_valor = df_filtrado[df_filtrado['Valor'] == menor_valor_filtrado]['Data'].iloc[0]

# Criando o gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Plotando a evolução diária do preço
ax.plot(df_filtrado['Data'], df_filtrado['Valor'], label='Preço Diário', color='blue', alpha=0.7)

# Destacando o maior valor
ax.scatter(data_maior_valor, maior_valor_filtrado, color='green', s=100, label=f'Maior Valor: ${maior_valor_filtrado:.2f}')
ax.text(data_maior_valor, maior_valor_filtrado, f'{maior_valor_filtrado:.2f}', color='green', fontsize=10, ha='center', va='bottom')

# Destacando o menor valor
ax.scatter(data_menor_valor, menor_valor_filtrado, color='red', s=100, label=f'Menor Valor: ${menor_valor_filtrado:.2f}')
ax.text(data_menor_valor, menor_valor_filtrado, f'{menor_valor_filtrado:.2f}', color='red', fontsize=10, ha='center', va='top')

# Configurações do gráfico
ax.set_title(f"Evolução do Preço do Petróleo ({anos_selecionados[0]} - {anos_selecionados[1]})")
ax.set_xlabel("Data")
ax.set_ylabel("Preço ($)")
ax.legend()

# Exibindo o gráfico no Streamlit
st.pyplot(fig)




# PLOTANDO TOP 10 PREÇOS NO PERÍODO FILTRADO

# Selecionando os 10 maiores valores
df_ranking = df_filtrado.nlargest(10, 'Valor')

# Criando o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df_ranking['Data'].dt.strftime('%d/%m/%Y'), df_ranking['Valor'], color='blue', alpha=0.7)

# Adicionando título e rótulos
ax.set_title(f"Top 10 Maiores Valores no Período ({anos_selecionados[0]} - {anos_selecionados[1]})")
ax.set_xlabel("Data")
ax.set_ylabel("Valor ($)")
ax.tick_params(axis='x', rotation=45)  # Rotaciona os rótulos no eixo X para melhor visualização

# Exibindo o gráfico no Streamlit
st.pyplot(fig)




# PLOTANDO GRÁFICO DE LINHAS COM A MÉDIA DE PREÇO NO MÊS DE CADA ANO FILTRADO

# Adicionando colunas de ano e mês
df_filtrado['Ano'] = df_filtrado['Data'].dt.year
df_filtrado['Mês'] = df_filtrado['Data'].dt.month

# Calculando a média do preço para cada combinação de ano e mês
df_mensal = df_filtrado.groupby(['Ano', 'Mês'])['Valor'].mean().reset_index()

# Pivotando os dados para formato adequado ao gráfico
df_pivot = df_mensal.pivot(index='Mês', columns='Ano', values='Valor')

# Criando o gráfico
fig, ax = plt.subplots(figsize=(12, 6))

# Plotando as linhas para cada ano
for ano in df_pivot.columns:
    ax.plot(df_pivot.index, df_pivot[ano], label=f'Ano {ano}', marker='o')

# Configurações do gráfico
ax.set_title(f"Média Mensal do Preço do Petróleo ({anos_selecionados[0]} - {anos_selecionados[1]})")
ax.set_xlabel("Mês")
ax.set_ylabel("Média do Preço ($)")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
ax.legend(title="Ano", loc='upper right')

# Exibindo o gráfico no Streamlit
st.pyplot(fig)