# PyTIPI
[![Documentação](https://img.shields.io/badge/Acessar-Documentação-informational?style=for-the-badge)](https://viniciuslucchesi.github.io/tipi-api/#/)

É uma API desenvolvida em Python através do framework Robyn com o objetivo de buscar as alíquotas para cada um dos códigos do **NCM** _(Nomenclatura Comum do Mercosul)_ através da utilização do Web Scraping.

Ela utiliza os dados baixados de uma planilha de Excel disponibilizada no site oficial do governo brasileiro na aba da [Receita Federal](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/legislacao-por-assunto/tipi-tabela-de-incidencia-do-imposto-sobre-produtos-industrializados) através da **TIPI** _(Tabela de incidência do Imposto sobre produtos industrializados)_ que é baseada no Sistema Harmonizado de Designação e de Codificação de Mercadorias.

## 🚀Tecnologias

- Python (3.11.1)
- Robyn (0.24.1)
- Pandas (1.5.3)
- Httpx (0.23.3)
- selectolax (0.3.12)

## 💡Funcionalidades
- Buscar todos os NCM's
- Buscar por um NCM

## ⚙️Rotas

Retorno de um NCM específico
```text
[GET] .../api/ncm/9011.20.10
```
```json
[
  {
    "NCM": "9011.20.10",
    "EX": null,
    "DESCRIÇÃO": "Para fotomicrografia",
    "ALÍQUOTA(%)": 3.25
  }
]
```

Retorno de todos os NCM's encontrados
```text
[GET] .../api/ncm/all
```
```json
[
    {
        "NCM": "1.01",
        "EX": null,
        "DESCRI\u00c7\u00c3O": "Cavalos, asininos e muares, vivos.",
        "AL\u00cdQUOTA(%)": null
    },
    {
        "NCM": "101.2",
        "EX": null,
        "DESCRI\u00c7\u00c3O": "Cavalos",
        "AL\u00cdQUOTA(%)": null
    },
    {
        "NCM": "0101.21.00",
        "EX": null,
        "DESCRI\u00c7\u00c3O": "Reprodutores de ra\u00e7a pura",
        "AL\u00cdQUOTA(%)": 0
    },
    {
        "NCM": "0101.29.00",
        "EX": null,
        "DESCRI\u00c7\u00c3O": "Outros",
        "AL\u00cdQUOTA(%)": 0
    },
    {
        "NCM": "0101.30.00",
        "EX": null,
        "DESCRI\u00c7\u00c3O": "Asininos",
        "AL\u00cdQUOTA(%)": 0
    },
    {
        "NCM": "0101.90.00",
        "EX": null,
        "DESCRI\u00c7\u00c3O": "Outros",
        "AL\u00cdQUOTA(%)": 0
    },
    {
        "NCM": "1.02",
        "EX": null,
        "DESCRI\u00c7\u00c3O": "Animais vivos da esp\u00e9cie bovina.",
        "AL\u00cdQUOTA(%)": null
    },
    {
        "NCM": "102.2",
        "EX": null,
        "DESCRI\u00c7\u00c3O": "Bovinos dom\u00e9sticos",
        "AL\u00cdQUOTA(%)": null
    },
    {
        "NCM": "0102.21",
        "EX": null,
        "DESCRI\u00c7\u00c3O": "Reprodutores de ra\u00e7a pura",
        "AL\u00cdQUOTA(%)": null
    },
    ...
    {
        "NCM": "9706.90.00",
        "EX": null,
        "DESCRI\u00c7\u00c3O": "Outras",
        "AL\u00cdQUOTA(%)": 0
    }
]
```
