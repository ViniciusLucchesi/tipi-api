# 📖 Introdução

**PyTIPI** é uma API desenvolvida em Python através do framework Robyn com o objetivo de buscar as alíquotas para cada um dos códigos do **NCM** (Nomenclatura Comum do Mercosul), segundo os dados disponibilizados pelo site [oficial do governo brasileiro](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/legislacao-por-assunto/tipi-tabela-de-incidencia-do-imposto-sobre-produtos-industrializados) na **Tabela de incidência do Imposto sobre produtos industrializados** que é baseada no Sistema Harmonizado de Designação e de Codificação de Mercadorias.

## 🚀Tecnologias

- Python (3.11)
- Robyn (0.25)

## 💡Funcionalidades

- Buscar todos os NCM's
- Buscar por um NCM específico
- Buscar por todos os itens de uma determinada categoria (com base no NCM)

## 🧐 Como ela funciona

### Coleta dos dados

Os dados são coletados utilizando a técnica de Scraping, através das bibliotecas **httpx** e **selectolax**.

### Tratamento dos dados

Após sua coleta os dados são armazenados em um arquivo no próprio servidor utilizando o formato **.pickle** já que esse permite uma grande velocidade ao ser lido/escrito utilizando a biblioteca **pandas**.

### Extrutura da API

Essa API foi criada utilizando o framework python chamado **Robyn**, que foi escrito em Ruby, possibilitando uma altíssima velocidade em comparação a outros frameworks web como Flask ou até mesmo o FastAPI.
