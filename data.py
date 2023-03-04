import re
import pandas as pd
from scrapy import HTMLBase
from tools import runtime


class ManageData(HTMLBase):
    def __init__(self) -> None:
        super().__init__()
    
    def download_tipi_table(self):
        url_xlsx = 'https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/documentos-e-arquivos/tipi-em-excel.xlsx'
        response = self.get_html_content(url_xlsx)
        try:
            df = pd.read_excel(response, header=7)
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

    async def search_ncm(self, df:pd.DataFrame, search:str) -> pd.DataFrame:
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


@runtime
def main():
    try:
        ManageData().download_tipi_table()
        print('Planilha baixada com sucesso!')
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()