# PyTIPI
[![Documentação](https://img.shields.io/badge/Acessar-Documentação-informational?style=for-the-badge)](https://viniciuslucchesi.github.io/tipi-api/#/)

É uma API desenvolvida em Python através do framework Robyn com o objetivo de buscar as alíquotas para cada um dos códigos do **NCM** _(Nomenclatura Comum do Mercosul)_ através da utilização do Web Scraping.

Ela utiliza os dados baixados de uma planilha de Excel disponibilizada no site oficial do governo brasileiro na aba da [Receita Federal](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/legislacao-por-assunto/tipi-tabela-de-incidencia-do-imposto-sobre-produtos-industrializados) através da **TIPI** _(Tabela de incidência do Imposto sobre produtos industrializados)_ que é baseada no Sistema Harmonizado de Designação e de Codificação de Mercadorias.

## 🚀Tecnologias

- Python (3.11.2)
- Robyn (0.25.0)
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
    "DESCRIÇÃO": "Cavalos, asininos e muares, vivos.",
    "ALÍQUOTA(%)": null
  },
  {
    "NCM": "101.2",
    "EX": null,
    "DESCRIÇÃO": "Cavalos",
    "ALÍQUOTA(%)": null
  },
  {
    "NCM": "0101.21.00",
    "EX": null,
    "DESCRIÇÃO": "Reprodutores de raça pura",
    "ALÍQUOTA(%)": 0
  },
  {
    "NCM": "0101.29.00",
    "EX": null,
    "DESCRIÇÃO": "Outros",
    "ALÍQUOTA(%)": 0
  },
  {
    "NCM": "0101.30.00",
    "EX": null,
    "DESCRIÇÃO": "Asininos",
    "ALÍQUOTA(%)": 0
  },
  {
    "NCM": "0101.90.00",
    "EX": null,
    "DESCRIÇÃO": "Outros",
    "ALÍQUOTA(%)": 0
  },
  {
    "NCM": "1.02",
    "EX": null,
    "DESCRIÇÃO": "Animais vivos da espécie bovina.",
    "ALÍQUOTA(%)": null
  },
  {
    "NCM": "102.2",
    "EX": null,
    "DESCRIÇÃO": "Bovinos domésticos",
    "ALÍQUOTA(%)": null
  },
  {
    "NCM": "0102.21",
    "EX": null,
    "DESCRIÇÃO": "Reprodutores de raça pura",
    "ALÍQUOTA(%)": null
  },
  {
    "NCM": "0102.21.10",
    "EX": null,
    "DESCRIÇÃO": "Prenhes ou com cria ao pé",
    "ALÍQUOTA(%)": 0
  },
  ...
  {
    "NCM": "9706.90.00",
    "EX": null,
    "DESCRIÇÃO": "Outras",
    "ALÍQUOTA(%)": 0
  }
]
```
