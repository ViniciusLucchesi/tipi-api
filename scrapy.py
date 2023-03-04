import httpx
from selectolax.parser import HTMLParser
from dataclasses import dataclass, asdict
from tools import runtime


@dataclass
class TipiExtension:
    link:str
    extension:str


class HTMLBase:
    def __init__(self) -> None:
        self.url = 'https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/legislacao-por-assunto/tipi-tabela-de-incidencia-do-imposto-sobre-produtos-industrializados'
    
    def get_html_text(self) -> HTMLParser|int:
        """
        Returns HTMLParser if HTTPX.get() request is 200, 
            otherwise returns an integer type status code
        """
        resp = httpx.get(self.url)
        if resp.status_code == 200:
            return HTMLParser(resp.text)
        return resp.status_code

    def get_html_content(self, xlsx_link):
        """
        Returns HTML content if HTTPX.get() request is 200, 
            otherwise returns an integer type status code
        """
        resp = httpx.get(xlsx_link)
        if resp.status_code == 200:
            return resp.content
        return resp.status_code


class GovernmentScraping(HTMLBase):
    def __init__(self) -> None:
        super().__init__()
        self.html = self.get_html_text()

    def get_last_update(self) -> str:
        """
        Returns the date of the last update displayed on the page https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/legislacao-por-assunto/tipi-tabela-de-incidencia-do-imposto-sobre-produtos-industrializados
        """
        return self.html.css_first('span.documentModified').css_first('span.value').text()
    
    def get_link_to_file(self, extension:str) -> dict:
        """
        Get a link to a specific format file

        Args:
            extension (str): accepted document types [XLSX, PDF, DOCX]

        Returns:
            A dictionary with the link corresponding to the searched format and the searched format itself

            dictionary = {
                'link': 'https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/documentos-e-arquivos/tipi-em-excel.xlsx', 
                'extension': 'XLSX'
            }
        """
        file = self.html.css_first('p.callout').css(f'a[href$=".{extension.upper()}"]')
        data = TipiExtension(
            link=file[0].attrs['href'],
            extension=file[0].text()
        )
        return asdict(data)



@runtime
def main():
    print(GovernmentScraping().get_link_to_file('xlsx').__doc__)


if __name__ == '__main__':
    main()