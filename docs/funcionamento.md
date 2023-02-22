# 🧐 Como a API funciona?

## Coleta dos dados

Os dados são coletados utilizando a técnica de Web Scraping, através das bibliotecas **httpx** e **selectolax**. Realizei a coleta dos dados em algumas etapas separadas, sendo elas:

- Busca pela data da última modificação
- Busca pela URL do arquivo XLSX que contém as informações que precisamos

Ambas as etapas são realizadas na página exibida abaixo:
> ![Alt text](assets/web_page_tipi.png ':size=700')

Caso a data da última modificação coletada seja igual a data que nós temos registrado no sistema, a respeito da última modificação lida, a planilha contendo as informações sobre as alíquotas dos produtos não será baixada.

Caso essa data esteja diferente o sistema irá realizar o download da nova planilha, contendo os dados atualizados e já os disponibilizando dentro da API.

## Tratamento dos dados

Após sua coleta os dados são armazenados em um arquivo no próprio servidor utilizando o formato **.pickle** já que esse permite uma grande velocidade ao ser lido/escrito utilizando a biblioteca **pandas**.

Aqui os dados serão formatados, removendo espaços em branco e outros caracteres que ocupariam espaço desnecessário no **JSON** que será enviado ao cliente que requisitar a API.

## Extrutura da API

Essa API foi criada utilizando o framework python chamado **Robyn**, que foi escrito em Ruby, possibilitando uma altíssima velocidade em comparação a outros frameworks web como Flask ou até mesmo o FastAPI.