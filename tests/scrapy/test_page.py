import re
import pytest
from selectolax.parser import HTMLParser
from scrapy import HTMLBase, GovernmentScraping
from data import ManageData


# ManageData
def test_download_tipi_table():
    error = ManageData().download_tipi_table()
    assert error == None 


# GovernmentScraping
def test_function_get_last_updated_matches_string_pattern():
    pattern = '[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}h[0-9]{2}'
    gov_page = GovernmentScraping()
    last_update = gov_page.get_last_update()
    assert re.match(pattern, last_update) != None

def test_function_get_link_to_file_xlsx():
    pattern = {
        'link': 'https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/documentos-e-arquivos/tipi-em-excel.xlsx', 
        'extension': 'XLSX'
    }
    gov_page = GovernmentScraping()
    url_xlsx = gov_page.get_link_to_file('XLSX')
    assert url_xlsx == pattern


# HTMLBase tests
def test_get_html_text_is_html_parser():
    """
    Results:
        (type(html) == HTMLParser) => The response expected
        (type(html) != HTMLParser) => Status code different from 200
    """
    html = HTMLBase().get_html_text()
    assert type(html) == HTMLParser

def test_get_html_content_is_not_integer():
    """
    Results:
        (type(resp) != int) => The response expected
        (type(resp) == int) => Status code different from 200
    """
    url = 'https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/documentos-e-arquivos/tipi-em-excel.xlsx'
    resp = HTMLBase().get_html_content(url)
    assert type(resp) != int 