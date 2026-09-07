# Projeto Gerencial BI — primeira interação

## O que este projeto apresenta

Este repositório é uma vitrine de análises comerciais voltadas a gestores. O estudo atual explora rentabilidade, faturamento líquido, margem, mix de produtos, evolução ao longo do tempo e prioridades de clientes. Também apresenta leituras de churn, RFV (recência, frequência e valor) e agrupamentos de clientes para apoiar decisões de cobertura e recuperação.

Os nomes e identificadores usados nos artefatos publicados são fictícios. Os resultados servem para demonstrar o método, a narrativa e a experiência do dashboard; a base transacional original não é publicada.

## Artefatos atuais

- [Notebook de análise](../notebooks/rentabilidade-comercial/analise.ipynb): roteiro reproduzível, validações, gráficos e interpretações de negócio.
- [Dashboard executivo](../dashboards/rentabilidade-comercial/index.html): navegação por desempenho comercial, clientes, churn, RFV e segmentos.

## Como usar o dashboard

Abra `dashboards/rentabilidade-comercial/index.html` no navegador. A publicação pública carrega uma pequena amostra sintética, suficiente para explorar filtros, páginas e gráficos sem expor dados internos. No ambiente local, quando existir o arquivo agregado ignorado `data.js`, ele assume prioridade sobre a amostra.

## Como o projeto evolui

Para cada novo conjunto de dados:

1. validar encoding, separador, tipos e significado das colunas;
2. registrar a pergunta de negócio e o público da análise;
3. criar um novo notebook em `notebooks/<tema>/`;
4. documentar cálculos, limites de interpretação e gráficos;
5. criar um dashboard em `dashboards/<tema>/` quando houver uma decisão recorrente para acompanhar;
6. atualizar esta apresentação com o novo artefato.

Não publique bases, credenciais, arquivos de design internos ou artefatos de execução local. O `.gitignore` já protege esses itens no fluxo de versionamento.
