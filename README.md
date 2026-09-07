# Análise de dados — template

Projeto para análises de dados em Python: jogue seus dados na pasta `dados/` e o agente conduz a análise guiada, uma pergunta de cada vez.

## Como usar

1. Coloque seus dados em **`dados/`**.
2. Abra o OpenCode na pasta do projeto e digite:

   ```
   /analise
   ```

   O OpenCode faz o resto: localiza os dados, faz perguntas sobre o objetivo e começa a análise.

## Estrutura do projeto

| Arquivo | Papel |
|---|---|
| `AGENTS.md` | Regras que valem **sempre** (célula curta, sem jargão, dashboards, gráficos, identidade visual). |
| `.design/` | **Identidade visual** do projeto (paleta, tipografia, tokens, componentes). Tudo que estiver aqui prevalece sobre a paleta padrão e deve ser seguido pelos dashboards. Veja `.design/README.md`. |
| `notebooks/<slug>/` | Cada análise é um notebook novo, em pasta própria. |
| `dashboards/<slug>/` | Cada dashboard é um HTML autocontido, em pasta própria. |
| `.agents/command/analise.md` | O **comando**: o que `/analise` dispara. |

### Skills de fluxo (usadas na análise, nesta ordem)

| Skill | Papel |
|---|---|
| `analista-senior` | O **método**: conduz a análise uma pergunta por vez. |
| `verificacao-leitura` | Confere **uma vez** se os dados foram lidos corretamente (encoding, separador, tipos). |
| `revisao-critica` | Confere, **a cada pergunta respondida**, se o resultado se sustenta. |
| `graficos` | Escolhe o **tipo de gráfico** certo, aplica cores, rótulos e responsividade. |
| `especialista-excel` | Exporta análises para planilhas `.xlsx` entregáveis com fórmulas vivas. |
| `dashboard` | Cria dashboards interativos em HTML com htmx, CSS e JavaScript (segue `.design/`). |

### Skills complementares

| Skill | Papel |
|---|---|
| `especialista-sql` | Consultas, modelagem e otimização SQL (SQLite, PostgreSQL, MySQL, SQL Server). |
| `mapas` | Visualizações geoespaciais (coroplético, marcadores, rotas, 3D) com bibliotecas gratuitas. |
| `dataviz` | Dashboards HTML renderizados por medidas DAX no Power BI. |
| `data-creation` (DAX) | Cria, revisa e otimiza medidas, colunas e tabelas DAX. |
| `ui-ux` | Inteligência de design de UI/UX (estilos, paletas, fontes, stacks). |
| `ux-researcher-designer` | Pesquisa de UX: personas, jornadas, testes de usabilidade. |
| `3d-web-experience` | Experiências 3D na web (Three.js, React Three Fiber, WebGL). |
| `graphify` | Transforma entradas em grafo de conhecimento persistente. |
| `skill-orchestrator` | Orquestra as skills do projeto e decide qual acionar. |

## Formatos suportados

CSV, Excel (`.xlsx`), Parquet, JSON, SQLite.
