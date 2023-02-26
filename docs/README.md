<div class="informational-msg">
    <h3>Atenção</h3>
    <p>Essa API ainda não foi disponibilizada online. Por conta disso as rotas registradas ainda não apresentam o caminho completo da URL, sendo exibidos somente como três pontos (...)</p>
    <p>Assim que ela for disponibilizada online essa mensagem irá desaparecer, ao mesmo tempo que serão atualizadas as rotas aqui na documentação, alterando os três pontos pela URL definitiva.</p>
</div>

# Introdução

**PyTIPI** é uma API desenvolvida em Python através do framework Robyn com o objetivo de buscar as informações referentes a cada um dos códigos de **NCM** _(Nomenclatura Comum do Mercosul)_ através da utilização do Web Scraping.

Ela utiliza os dados baixados de uma planilha de Excel disponibilizada no site oficial do governo brasileiro na aba da [Receita Federal](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/legislacao-por-assunto/tipi-tabela-de-incidencia-do-imposto-sobre-produtos-industrializados) através da **TIPI** _(Tabela de incidência do Imposto sobre produtos industrializados)_ que é baseada no Sistema Harmonizado de Designação e de Codificação de Mercadorias.

## 🚀 Tecnologias

- Python (3.11.1)
- Robyn (0.24.1)
- Pandas (1.5.3)
- Httpx (0.23.3)
- selectolax (0.3.12)

## 💡Funcionalidades

- Buscar todos os NCM's
- Buscar por um NCM específico

## :dart: Objetivos

Tornar o acesso a informação dos NCM's de todos os produtos registrados na TIPI mais fácil, rápido e de maniera confiável. Evitando a necessidade de buscar essa informação manualmente, ou até realizar um retrabalho para garantir que a informação adiquirida anteriormente esteja correta.

Além é claro de fechar com chave de ouro os conhecimentos adiquiridos na [ITE](https://ite.edu.br/) _(Instituição Toledo de Ensino)_, faculdade em que eu estou estudando, sendo o projeto que idealizei para o meu **TCC** _(Trabalho de Conclusão de Curso)_.
