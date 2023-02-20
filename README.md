# PyTIPI

PyTIPI é uma API desenvolvida em Python através do framework Robyn com o objetivo de buscar as alíquotas para cada um dos códigos do **NCM** (Nomenclatura Comum do Mercosul), segundo os dados disponibilizados pelo site [oficial do governo brasileiro](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/legislacao-por-assunto/tipi-tabela-de-incidencia-do-imposto-sobre-produtos-industrializados) na **Tabela de incidência do Imposto sobre produtos industrializados** que é baseada no Sistema Harmonizado de Designação e de Codificação de Mercadorias.

## 📰 Últimas Atualizações

### ⚖️ Decretos Oficiais

- [Decreto n°11.182, de 24 de agosto de 2022](http://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/decreto/D11182.htm)
- [Ato Declaratório Executivo RFB n°5, de 29 de agosto de 2022](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=125815)
- [Ato Declaratório Executivo RFB n°6, de 20 de dezembro de 2022](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=127946)


### ⚙️ API - Em breve
```text
1. Disponibilisar um site (exibindo todos os NCMs)
2. Impelentar download dos 3 formatos de arquivos
3. Implementar rotas assíncronas
```

## 🚀Tecnologias

- Python (3.11) 
- Robyn (0.25)

## 💡Funcionalidades

- Buscar todos os NCM's
- Buscar por um **NCM** específico
- Buscar por todos os itens de uma determinada categoria (com base no NCM)

## ⚙️Rotas

Retorna todas as informações contidas na TIPI
```text
[GET] /api/ncm/all
```

Retorna somente um NCM específico
```text
[GET] /api/ncm/<numero_do_ncm>
```

Retorna uma lista com base em um NCM
```text
[GET] /api/all/ncm/<numero_do_ncm>
```


## 🧐 Como ela funciona

### Coleta dos dados
Os dados são coletados utilizando a técnica de Scraping, através das bibliotecas **httpx** e **selectolax**.

### Tratamento dos dados
Após sua coleta os dados são armazenados em um arquivo no próprio servidor utilizando o formato **.pickle** já que esse permite uma grande velocidade ao ser lido/escrito utilizando a biblioteca **pandas**.

### Extrutura da API
Essa API foi criada utilizando o framework python chamado **Robyn**, que foi escrito em Ruby, possibilitando uma altíssima velocidade em comparação a outros frameworks web como Flask ou até mesmo o FastAPI. 
