# NYC Flights - Flight Delay Analysis

Analise exploratoria de voos de Nova York com foco em atrasos, destinos criticos e indicadores operacionais. O notebook responde perguntas analiticas sobre pontualidade, velocidade media e comportamento dos atrasos.

## Objetivo

Identificar padroes de atraso em voos, comparar destinos e criar uma leitura analitica que possa apoiar decisoes operacionais em transporte aereo.

## O que o projeto demonstra

- Carga e tratamento inicial de dados de voos.
- Analise de atrasos superiores a duas horas.
- Estatisticas descritivas para investigar distribuicoes e outliers.
- Agrupamentos por destino e calculo de indicadores derivados.
- Visualizacoes com Plotly para histogramas, boxplots e comparacoes.
- Organizacao do notebook por perguntas de negocio.

## Stack

- Python
- Pandas e NumPy
- Plotly
- Jupyter Notebook / Google Colab

## Arquivos

| Arquivo | Descricao |
| --- | --- |
| `NYF.ipynb` | Notebook principal com analise exploratoria de voos. |

## Como executar

1. Abra o notebook no Google Colab ou Jupyter.
2. Disponibilize o arquivo `nyflights.csv` no caminho esperado ou ajuste a celula de leitura.
3. Execute as celulas em ordem.

## Pontos fortes para portfólio

O projeto tem boa clareza analitica porque parte de perguntas objetivas e transforma dados operacionais em indicadores. Para Engenharia de Dados Júnior, ele mostra raciocinio com dados transacionais, agregacoes e metricas derivadas.

## Limitações atuais

- O dataset nao esta versionado nem documentado no repositorio.
- O notebook depende de Google Drive.
- Falta modularizacao das transformacoes.
- Nao ha validacao automatica para colunas esperadas, datas ou valores numericos.
- A conclusao final poderia sintetizar os achados em recomendacoes operacionais.

## Próximas melhorias recomendadas

- Criar um dicionario de dados com as colunas principais.
- Separar transformacoes em funcoes testaveis.
- Adicionar uma etapa de validacao de schema.
- Incluir consultas SQL equivalentes para demonstrar fluencia analitica.
- Criar um painel simples com os principais indicadores de atraso.
