import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import streamlit as st


# vamos começar com a função para calcular o MACD
def calcular_macd(df):
    rapidaMME = df['Close'].ewm(span=12).mean()
    lentaMME = df['Close'].ewm(span=26).mean()
    MACD = rapidaMME - lentaMME
    sinal = MACD.ewm(span=9).mean()
    return MACD , sinal

# a seguir vamos plotar o grafico
def plotar_grafico(df, acao):
    df.index = pd.to_datetime(df['Date'])
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['Close'],
        name='preco fechamento',
        line_color='#FECB52',
        text=df.index.strftime('%d/%m'),
        hovertemplate='%{text}<br>Preço: %{y}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['preco_compra'],
        name='Compra',
        mode='markers',
        marker=dict(color='#00CC69', size=10),
        text=df.index.strftime('%d/%m'),
        hovertemplate='%{text}<br>Preço Compra: %{y}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['preco_venda'],
        name='Venda',
        mode='markers',
        marker=dict(color='#EF553B', size=10),
        text=df.index.strftime('%d/%m'),
        hovertemplate='%{text}<br>Preço Venda: %{y}<extra:</extra>'
    ))
    st.plotly_chart(fig)

# configurando o streamlit

st.title('Analise de Ações')
st.sidebar.header('Parametros')

#inputs dos usuarios
acao = st.sidebar.text_input('Digite o simbolo da Ação. Sempre usar SA ao final', 'PETR4.SA')
analise = st.sidebar.selectbox('Selecione o tipo de análise', ['MACD'])
executar = st.sidebar.button('Executar')


if executar:
    #obtendo dados das ações
    ticker = yf.Ticker(acao)
    df = ticker.history(period='1mo').reset_index()

    #calculo macd
    df['MACD'] , df['sinal'] = calcular_macd(df)

    #identificar compra e venda
    df['flag'] = ''
    df['preco_compra'] = np.nan
    df['preco_venda'] = np.nan
    for i in range(1, len(df)):
        if df['MACD'][i] > df['sinal'][i]:
            if df['flag'][i - 1] != 'C':
                df['flag'][i] = 'C'
                df['preco_compra'][i] = df['Close'][i]
            else:
                df['flag'][i] = 'C'
        elif df['MACD'][i] < df['sinal'][i]:
            if df['flag'][i - 1] != "V":
                df['flag'][i] = "V"
                df['preco_venda'][i] = df['Close'][i]
            else:
                df['flag'][i] = 'V'

    #plotando grafico
    plotar_grafico(df, acao)

    #mensagem final
    ultimo_status = df['flag'].iloc[-1]
    preco_fechamento = round(df['Close'].iloc[-1], 2)

    #mapeando status
    status_map = {'V': 'VENDA', 'C': 'COMPRA', "":'MANTER' }
    status_texto = status_map.get(ultimo_status, 'INDEFINIDO')

    # definindo cor mensagem
    cor_map= {'VENDA': 'red', 'COMPRA': 'green', 'MANTER': 'yellow' }
    cor = cor_map.get(status_texto, 'black')

    msg = f'{acao}, Operação: <span style="color:{cor}">{status_texto}</span> - preço de Fechamento: {preco_fechamento}'

    # mostrar informações da ação
    info = ticker.info
    nome_acao = info.get('shortName', 'Ação não Disponivel')
    st.subheader(nome_acao)
    st.markdown(msg, unsafe_allow_html=True)
