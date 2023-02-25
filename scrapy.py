import re
import time
import httpx
import pandas as pd
from functools import wraps
from selectolax.parser import HTMLParser
from dataclasses import dataclass, asdict


@dataclass
class InfoTIPI:
    link:str
    extension:str
    
@dataclass
class rowTIPI:
    ncm:str
    ex:str
    desc:str
    aliquota:str

# DECORATORS TO TEST VELOCITY
def runtime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(result)
        print(f'{func.__name__} took {end - start:.6f} seconds to complete')
        return result
    return wrapper


# Scrapy functions
def get_html() -> HTMLParser:
    url = 'https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/legislacao-por-assunto/tipi-tabela-de-incidencia-do-imposto-sobre-produtos-industrializados'
    resp = httpx.get(url)
    return HTMLParser(resp.text)

def get_last_updated() -> str:
    html = get_html()
    return html.css_first('span.documentModified').css_first('span.value').text()

def get_link_to_file(html:HTMLParser, extension:str) -> dict:
    file = html.css_first('p.callout').css(f'a[href$=".{extension}"]')
    data = InfoTIPI(
        link=file[0].attrs['href'],
        extension=file[0].text()
    )
    return asdict(data)

def get_all_link_to_files(html:HTMLParser) -> list:
    files = html.css_first('p.callout').css('a')
    result = []
    for type in files:
        data = InfoTIPI(
            link=type.attrs['href'],
            extension=type.text()
        )
        result.append(asdict(data))
    return result


# PICKLE functions
# @runtime
def download_tipi(url:str) -> None:
    request = httpx.get(url).content
    try:
        df = pd.read_excel(request, header=7)
        df = wipe_data(df)
        df.to_pickle('TIPI.pickle')
    except Exception as error:
        print('ERRO: ', error)

# @runtime
def load_pickle() -> pd.DataFrame:
    return pd.read_pickle('TIPI.pickle')


# Panda functions
def wipe_data(df:pd.DataFrame) -> pd.DataFrame:
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

def search_ncm(df:pd.DataFrame, search:str) -> pd.DataFrame:
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
    html = get_html()
    url_xlsx = get_link_to_file(html, 'XLSX')
    download_tipi(url_xlsx.get('link'))