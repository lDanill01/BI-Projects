# Projeto de análises comerciais em Python

Projeto público de apresentação de análises comerciais em Python e dashboards interativos. A estrutura foi preparada para receber novos dados, notebooks e experiências de navegação sem publicar bases transacionais ou materiais internos.

## Comece por aqui

- [Apresentação do projeto atual](apresentacao/PROJETO_ATUAL.md)
- [Notebook de rentabilidade comercial](notebooks/rentabilidade-comercial/analise.ipynb)
- [Dashboard executivo](dashboards/rentabilidade-comercial/index.html)

O dashboard abre diretamente no navegador e usa dados sintéticos de demonstração quando a base local não está disponível. A base real e os agregados locais permanecem fora da publicação.

## Estrutura pública

```text
apresentacao/                     contexto e primeira interação
notebooks/<tema>/                 análises reproduzíveis em Jupyter
dashboards/<tema>/                interfaces HTML interativas
```

Cada novo estudo deve ter sua própria pasta, pergunta de negócio, validação de leitura, explicações em linguagem de negócio e registro das limitações dos dados.

## Como o projeto evolui

Ao adicionar um dataset, crie um novo notebook em `notebooks/<tema>/`. Quando a análise apoiar uma decisão recorrente, crie também `dashboards/<tema>/` e inclua uma amostra sintética para que a experiência pública continue navegável sem dados reais.

## Publicação no GitHub

O `.gitignore` exclui `.data/`, `.design/`, `.agents/`, `docs/`, `AGENTS.md`, ambientes virtuais, dependências locais e o `data.js` gerado a partir da base real. Revise `git status` antes de criar o commit e faça o commit e o push manualmente.
