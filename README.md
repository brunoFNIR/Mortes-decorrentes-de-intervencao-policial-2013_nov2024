# Análise de Mortes Decorrentes de Ação Policial no Estado de São Paulo (2013 - Nov/2024)

## Visão Geral do Projeto

Este projeto tem como objetivo realizar uma análise exploratória e temporal de dados sobre mortes decorrentes de intervenção policial no Estado de São Paulo, abrangendo o período de 2013 a novembro de 2024. O trabalho busca identificar padrões, tendências e distribuições geográficas e temporais das ocorrências, fornecendo insights valiosos sobre este tema crítico.

Além da análise detalhada em um Jupyter Notebook, o projeto culmina em um **Dashboard Interativo** desenvolvido com **Streamlit**, permitindo que os usuários explorem as visualizações de dados de forma dinâmica e intuitiva.

## Estrutura do Repositório

O repositório está organizado da seguinte forma:

* `data/`: Contém o dataset original (`ocorrencias_mortes_acao_policial_2013_2024.csv`).
* `notebooks/`: Contém o Jupyter Notebook (`analise_exploratoria_mortes_acao_policial.ipynb`) com a análise exploratória detalhada, limpeza e transformações dos dados.
* `app.py`: O script principal do aplicativo Streamlit que gera o dashboard interativo.
* `utils.py`: Módulo Python com funções de processamento e preparação de dados, para garantir modularidade e reusabilidade do código.
* `requirements.txt`: Lista todas as bibliotecas Python necessárias para executar o projeto.
* `.gitignore`: Arquivo para o Git ignorar pastas e arquivos gerados (como `__pycache__`).

## O Dashboard Interativo (Streamlit)

O dashboard interativo permite visualizar:

* **Distribuições de Variáveis Categóricas:** Análise de ocorrências por Corporação, Situação, Sexo e Cor de Pele.
* **Distribuição por Idade:** Histograma da idade das pessoas envolvidas.
* **Análise Temporal:** Número de ocorrências ao longo do tempo (mensal).
* **Análise Geográfica:** Distribuição espacial das ocorrências por Longitude e Latitude.
* **Análise Detalhada por Município (Top 5):**
    * Número total de mortes para os 5 municípios com maior volume.
    * Média móvel de 3 meses do número de ocorrências por mês para os Top 5 municípios, revelando tendências suavizadas.
    * Série temporal do número de ocorrências por mês para os Top 5 municípios, com uma linha de tendência linear para identificar padrões de crescimento/decaimento.

### Acesso ao Dashboard Online

Este projeto está hospedado no Streamlit Community Cloud e pode ser acessado através do link abaixo:

**[Acesse o Dashboard Interativo Aqui](https://mortes-decorrentes-de-intervencao-policial-2013nov2024-q5vmzgp.streamlit.app)**

## Contato

* **Bruno Felipe Novelli Ivanaskas Rodrigues**
* [LinkedIn](https://www.linkedin.com/in/brunofnir/)
* [Email](brunofnir@gmail.com)
