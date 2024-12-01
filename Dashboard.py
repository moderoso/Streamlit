# Importação das bibliotecas
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np
import matplotlib as plt 
import plotly.graph_objects as go
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

df_datas_relevantes = pd.read_csv('Eventos_Relevantes_Petroleo.csv', encoding = "UTF-8", sep=";")
df_datas_relevantes['Inicio Mês'] = pd.to_datetime(df_datas_relevantes['Inicio Mês'],format="%d/%m/%Y")
df_datas_relevantes['Valor'] = df_datas_relevantes['Valor'].replace(',','.')
df_datas_relevantes['Valor'] = pd.to_numeric(df_datas_relevantes['Valor'])

df = importacao_dados_previsao(url)
df_preco = tratando_dados(df)
df_preco.rename(columns={"ds":"Data", "y":"Valor"},inplace=True)


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
col1.metric("Maior Valor (Ano Atual)", f"US${maior_valor_atual:.2f}")

# Data do último registro
ultima_data = df_preco['Data'].max()
col2.metric("Última Data Registrada", ultima_data.strftime('%d/%m/%Y'))

# Maior valor do período filtrado
maior_valor_filtrado = df_filtrado['Valor'].max()
col3.metric("Maior Valor (Período)", f"US${maior_valor_filtrado:.2f}")

# Menor valor do período filtrado
menor_valor_filtrado = df_filtrado['Valor'].min()
col4.metric("Menor Valor (Período)", f"US${menor_valor_filtrado:.2f}")


# Encontrando os valores extremos no período filtrado
data_maior_valor = df_filtrado[df_filtrado['Valor'] == maior_valor_filtrado]['Data'].iloc[0]
data_menor_valor = df_filtrado[df_filtrado['Valor'] == menor_valor_filtrado]['Data'].iloc[0]

# Selecionando os 10 maiores valores
df_ranking = df_filtrado.nlargest(10, 'Valor')

# Adicionando colunas de ano e mês
df_filtrado['Ano'] = df_filtrado['Data'].dt.year
df_filtrado['Mês'] = df_filtrado['Data'].dt.month

# Calculando a média do preço para cada combinação de ano e mês
df_mensal = df_filtrado.groupby(['Ano', 'Mês'])['Valor'].mean().reset_index()


col1, col2 = st.columns(2)

with col1:
    # **Gráfico 1: Evolução diária do preço com maior e menor valor**
    fig1 = go.Figure()

    # Adicionando a linha de evolução diária
    fig1.add_trace(go.Scatter(
        x=df_filtrado['Data'],
        y=df_filtrado['Valor'],
        mode='lines',
        name='Preço Diário',
        line=dict(color='blue', width=2),
    ))

    # Destacando o maior valor
    fig1.add_trace(go.Scatter(
        x=[data_maior_valor],
        y=[maior_valor_filtrado],
        mode='markers+text',
        name=f'Maior Valor: US${maior_valor_filtrado:.2f}',
        text=[f'{maior_valor_filtrado:.2f}'],
        textposition="top center",
        marker=dict(color='green', size=10),
    ))

    # Destacando o menor valor
    fig1.add_trace(go.Scatter(
        x=[data_menor_valor],
        y=[menor_valor_filtrado],
        mode='markers+text',
        name=f'Menor Valor: US${menor_valor_filtrado:.2f}',
        text=[f'{menor_valor_filtrado:.2f}'],
        textposition="bottom center",
        marker=dict(color='red', size=10),
    ))

    # Configurações do layout
    fig1.update_layout(
        title=f"Evolução do Preço do Petróleo ({anos_selecionados[0]} - {anos_selecionados[1]})",
        xaxis_title="Data",
        yaxis_title="Preço (US$)",
        legend_title="Legenda",
        template="plotly_white",
    )

    st.plotly_chart(fig1, use_container_width=True)

    # **Gráfico 2: Top 10 maiores valores no período filtrado**
    fig2 = px.bar(
    df_ranking,
    x=df_ranking['Data'].dt.strftime('%d/%m/%Y'),
    y='Valor',
    title=f"Top 10 Maiores Valores ({anos_selecionados[0]} - {anos_selecionados[1]})",
    labels={'Valor': 'Preço (US$)', 'Data': 'Data'},
    text='Valor'  # Adiciona os valores como rótulos
    )

    # Personalizando os rótulos
    fig2.update_traces(
        texttemplate='%{text:.2f}',  # Formato dos rótulos (2 casas decimais)
        textposition='outside',      # Posição dos rótulos (fora das barras)
        marker_color='blue',         # Cor das barras
        marker_line_width=1.5,       # Contorno das barras
        opacity=0.8                  # Transparência das barras
    )

    # Ajustes no layout
    y_max = df_ranking['Valor'].max()
    fig2.update_layout(
    yaxis_range=[0, y_max * 1.2],  # Adiciona 20% de folga ao topo do eixo Y
    xaxis_tickangle=-45,
    yaxis_title="Preço (US$)",
    template="plotly_white",
    showlegend=False
    )

    # Exibindo o gráfico no Streamlit
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    # **Gráfico 3: Média de preço por mês e ano**
    fig3 = px.line(
        df_mensal,
        x='Mês',
        y='Valor',
        color='Ano',
        title="Média Mensal do Preço por Ano",
        labels={'Mês': 'Mês', 'Valor': 'Preço (US$)', 'Ano': 'Ano'},
        markers=True,
    )

    fig3.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=list(range(1, 13)),
            ticktext=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
        ),
        yaxis_title="Preço Médio (US$)",
        template="plotly_white",
    )
    st.plotly_chart(fig3, use_container_width=True)

    # Gráfico 4: Evolução do Preço com Eventos Relevantes


    # Verificar valores extremos
    print("Valores máximos e mínimos do eixo Y:")
    print(f"Valor máximo: {df_filtrado['Valor'].max()}")
    print(f"Valor mínimo: {df_filtrado['Valor'].min()}")
    print(f"Valor máximo dos eventos: {df_datas_relevantes['Valor'].max()}")



    fig4 = go.Figure()

    # Linha de evolução diária
    fig4.add_trace(go.Scatter(
        x=df_filtrado['Data'],
        y=df_filtrado['Valor'],
        mode='lines',
        name='Preço Diário',
        line=dict(color='blue', width=2),
    ))

    # Pontos dos eventos relevantes
    for _, row in df_datas_relevantes.iterrows():
        fig4.add_trace(go.Scatter(
            x=[row['Inicio Mês']],
            y=[row['Valor']],
            mode='markers+text',
            name=row['Evento Global'],
            text=[row['Evento Global']],
            textposition="top center",
            marker=dict(color='red', size=8),
        ))

    # Configurações do layout
    fig4.update_layout(
        title="Evolução do Preço do Petróleo com Eventos Relevantes",
        xaxis_title="Data",
        yaxis_title="Preço (US$)",
        template="plotly_white",
        showlegend=False,
        yaxis_range=[df_filtrado['Valor'].min() - 5, df_filtrado['Valor'].max() + 5],  # Ajuste do eixo Y
    )

    # Exibir no Streamlit
    st.plotly_chart(fig4, use_container_width=True)
