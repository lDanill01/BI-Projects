# Laboratório de dados e inteligência de negócios

Este projeto reúne análises reproduzíveis em notebooks e dashboards interativos construídos a partir de diferentes fontes, setores e nichos de mercado.

O objetivo é transformar dados brutos em conhecimento útil para exploração, diagnóstico e apoio à decisão, combinando:

- **Data analysis:** leitura, preparação, exploração, métricas, padrões e indicadores;
- **Data science:** investigação de relações, segmentações, previsões e avaliação de hipóteses;
- **Machine learning:** modelos preditivos, comparação de desempenho, validação e monitoramento de limitações;
- **Dashboards:** comunicação visual, filtros, navegação e síntese para públicos técnicos e de negócio.

## Comece por aqui

- [Apresentação do projeto atual](apresentacao/PROJETO_ATUAL.md)
- [Análise de rentabilidade comercial](notebooks/rentabilidade-comercial/analise.ipynb)
- [Dashboard de rentabilidade comercial](dashboards/rentabilidade-comercial/index.html)
- [Exploração operacional do Airbnb](notebooks/airbnb-exploracao/analise.ipynb)
- [Notebook de previsão de preços](notebooks/airbnb-exploracao/price_prediction.ipynb)
- [Dashboard operacional do Airbnb](dashboards/airbnb-exploracao/index.html)

Os notebooks registram o caminho da análise, suas validações, visualizações e limitações. Os dashboards apresentam os resultados de forma navegável e orientada à interação.

## Estrutura pública

```text
apresentacao/                     contexto e primeira interação
notebooks/<tema>/                 análises reproduzíveis em Jupyter
dashboards/<tema>/                interfaces interativas para exploração
```

Cada estudo deve ter uma pasta própria e documentar a fonte, a pergunta investigada, o público, as transformações, os resultados e os limites de interpretação.

## Fluxo de trabalho

1. identificar e validar a fonte de dados;
2. entender o contexto e a pergunta de negócio;
3. preparar os dados sem perder rastreabilidade;
4. explorar padrões com tabelas e gráficos claros;
5. aplicar modelos estatísticos ou de machine learning quando fizer sentido;
6. revisar métricas, vieses, qualidade e limitações;
7. transformar descobertas recorrentes em dashboards ou relatórios;
8. registrar aprendizados para os próximos estudos.

## Como adicionar uma nova análise

Crie um notebook em `notebooks/<tema>/`. Quando houver uma decisão ou acompanhamento recorrente, crie também `dashboards/<tema>/`. Para manter a publicação segura, use dados sintéticos ou agregados públicos no dashboard e mantenha bases internas, credenciais e artefatos locais fora do GitHub.

Este repositório é evolutivo: novas fontes, setores, métodos, notebooks e dashboards podem ser adicionados sem alterar a organização dos estudos existentes.
