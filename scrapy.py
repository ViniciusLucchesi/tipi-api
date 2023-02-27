import re
import httpx
import pandas as pd
from selectolax.parser import HTMLParser
from dataclasses import dataclass, asdict


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

    def get_html_content(self, url):
        resp = httpx.get(url)
        if resp.status_code == 200:
            return resp.content
        return resp.status_code


class GovernmentScraping(HTMLBase):
    def __init__(self) -> None:
        super().__init__()
        self.html = self.get_html_text()

    def get_last_update(self) -> str:
        return self.html.css_first('span.documentModified').css_first('span.value').text()
    
    def get_link_to_file(self, extension:str) -> dict:
        file = self.html.css_first('p.callout').css(f'a[href$=".{extension.upper()}"]')
        data = TipiExtension(
            link=file[0].attrs['href'],
            extension=file[0].text()
        )
        return asdict(data)


class ManageData(GovernmentScraping):
    def __init__(self) -> None:
        super().__init__()
    
    def download_tipi_table(self):
        url_xlsx = 'https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/documentos-e-arquivos/tipi-em-excel.xlsx'
        request = self.get_html_content(url_xlsx)
        try:
            df = pd.read_excel(request, header=7)
            df = self.wipe_data(df)
            df.to_pickle('TIPI.pickle')
            return None
        except Exception as error:
            return error
    
    def wipe_data(self, df:pd.DataFrame) -> pd.DataFrame:
        # Headers
        df.columns = df.columns.map(lambda x: x.replace(' ', ''))
        df = df.replace('(-)|(:)', '', regex=True)

        # Content
        df['DESCRIÇÃO'] = df['DESCRIÇÃO'].str.strip()
        invalid_ncm = df[df['NCM'].isnull()].index
        aliquotas_nt = df[df['ALÍQUOTA(%)'] == 'NT'].index
        for ncm in invalid_ncm:
            df.loc[ncm, 'NCM'] = df.loc[(ncm - 1), 'NCM']
        for aliquota in aliquotas_nt:
            df.loc[aliquota, 'ALÍQUOTA(%)'] = 0
        
        # Pretty
        resp = df.sort_index().reset_index()
        resp = resp.drop('index', axis=1)
        return resp

    def load_data(self) -> pd.DataFrame:
        return pd.read_pickle('TIPI.pickle')

    def search_ncm(self, df:pd.DataFrame, search:str) -> pd.DataFrame:
        regex = re.sub('(\.)', '\.', search)
        regex = f'^({regex})$'
        retorno = df[df['NCM'].str.contains(regex)]

        if retorno['ALÍQUOTA(%)'].isna:
            clean = re.sub('(\.)', '', search)
            regex = re.sub('(\.)', '\.?', search)
            regex = f'^0?({clean}|{regex}).*$'

            resp = df[df['NCM'].str.contains(regex)]
            resp = resp.sort_index().reset_index()
            resp = resp.drop('index', axis=1)
            return resp
        
        return retorno



if __name__ == '__main__':
    url = 'https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/documentos-e-arquivos/tipi-em-excel.xlsx'
    resp = HTMLBase().get_html_content(url)
    print(type(resp.content))
