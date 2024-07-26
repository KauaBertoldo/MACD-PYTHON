#Link para abrir o projeto 
https://macd-python-qgs3vhxpd2rk5wscs2iir9.streamlit.app/

# Projeto de Análise de Ações com MACD

Este projeto implementa uma ferramenta de análise de ações utilizando o indicador MACD (Moving Average Convergence Divergence) em Python. A aplicação permite aos usuários inserir o símbolo de uma ação, realizar a análise e visualizar o gráfico com os pontos de compra e venda destacados.

## Funcionalidades

- **Entrada de Símbolo da Ação:** Permite ao usuário inserir o símbolo da ação a ser analisada (sempre adicionar `.SA` ao final do símbolo).
- **Plotagem de Gráfico:** Gera um gráfico interativo com o preço de fechamento das ações e marcações nos pontos de compra e venda.
- **Mensagem de Operação:** Exibe uma mensagem final indicando a operação sugerida (compra, venda ou manter) com base no último fechamento.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação utilizada para desenvolvimento.
- **yFinance:** Biblioteca para obtenção de dados históricos das ações.
- **Pandas:** Biblioteca para manipulação e análise de dados.
- **NumPy:** Biblioteca para operações numéricas.
- **Plotly:** Biblioteca para criação de gráficos interativos.
- **Streamlit:** Biblioteca para criação de interfaces web interativas.

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Instale as bibliotecas necessárias com:
    ```sh
    pip install yfinance pandas numpy plotly streamlit
    ```
3. Salve o código da aplicação em um arquivo, por exemplo, `app.py`.
4. Execute a aplicação com o comando:
    ```sh
    streamlit run app.py
    ```

![Imagem Do Programa](https://github.com/KauaBertoldo/MACD-PYTHON/blob/main/Captura%20de%20tela%202024-07-26%20085457.png)
