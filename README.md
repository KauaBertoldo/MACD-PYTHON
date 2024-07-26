Projeto de Análise de Ações com MACD

Este projeto implementa uma ferramenta de análise de ações utilizando o indicador MACD (Moving Average Convergence Divergence) em Python. A aplicação permite aos usuários inserir o símbolo de uma ação, realizar a análise e visualizar o gráfico com os pontos de compra e venda destacados.

Funcionalidades: 
Entrada de Símbolo da Ação: Permite ao usuário inserir o símbolo da ação a ser analisada (sempre adicionar .SA ao final do símbolo).
Seleção de Tipo de Análise: Atualmente, suporta apenas análise utilizando o indicador MACD.
Plotagem de Gráfico: Gera um gráfico interativo com o preço de fechamento das ações e marcações nos pontos de compra e venda.
Mensagem de Operação: Exibe uma mensagem final indicando a operação sugerida (compra, venda ou manter) com base no último fechamento.

Tecnologias Utilizadas
Python: Linguagem de programação utilizada para desenvolvimento.
yFinance: Biblioteca para obtenção de dados históricos das ações.
Pandas: Biblioteca para manipulação e análise de dados.
NumPy: Biblioteca para operações numéricas.
Plotly: Biblioteca para criação de gráficos interativos.
Streamlit: Biblioteca para criação de interfaces web interativas.
