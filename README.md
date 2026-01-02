# 📈 Análise de Ações da B3 com Python

Este projeto tem como objetivo realizar uma análise exploratória de ações listadas na B3, utilizando dados reais obtidos via API.
A aplicação permite calcular indicadores financeiros, gerar visualizações e extrair insights que auxiliam na tomada de decisão.

O projeto foi desenvolvido com foco em boas práticas de organização, simulação de um cenário real de análise de dados e construção de portfólio para a área de Análise de Dados.

## 🎯 Objetivos do Projeto

- Praticar a análise de dados financeiros reais

- Trabalhar com APIs externas para coleta de dados

- Calcular indicadores relevantes do mercado financeiro

- Criar visualizações claras e interpretáveis

- Estruturar um projeto Python de forma profissional

- Demonstrar capacidade analítica aplicada a problemas reais

## 📌 Perguntas que o projeto busca responder

- Qual foi o retorno da ação nos últimos 12 meses?

- Como o preço da ação se comportou ao longo do período?

- É possível identificar tendências a partir do histórico de preços?

- Como transformar dados financeiros em informações úteis?

## 🛠️ Tecnologias Utilizadas

- Python

- Pandas — manipulação e análise de dados

- yfinance — coleta de dados financeiros via API

- Matplotlib / Seaborn — visualização de dados

- Git & GitHub — versionamento e organização do projeto


## ▶️ Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/ffabiolemos/b3-stock-analysis.git
cd b3-stock-analysis

2️⃣ Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Execute o projeto
python -m src.main

## 📊 Exemplo de Uso

Ao executar o projeto, o usuário informa o ticker da ação (com sufixo .SA):

Digite o ticker da ação (ex: PETR4.SA): PETR4.SA


O sistema retorna:

- Retorno percentual no período analisado

- Gráfico com o histórico de preços da ação

## 📈 Resultados Esperados

- Cálculo do retorno percentual em 12 meses

- Visualização do comportamento do preço da ação

- Identificação de tendências e variações

- Base para comparações futuras entre diferentes ações

## 👨‍💻 Sobre o Autor

Projeto desenvolvido por Fábio Lemos, profissional em transição para a área de Análise de Dados, com interesse em dados financeiros, visualização e geração de insights para apoio à tomada de decisão.

🔗 GitHub: https://github.com/ffabiolemos

🔗 LinkedIn: https://www.linkedin.com/in/ffabiolemos
