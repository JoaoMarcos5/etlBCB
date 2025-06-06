import requests
import pandas as pd

def requestApiBcb(data: str) -> pd.DataFrame:
    """
    Função que faz uma requisição a API do Banco Central do Brasil e retorna um DataFrame com os dados de Meios de Pagamentos Trimestral
    
    Parâmetros:
    data: data - string - aaaat (ex: 20231)

    Saída:
    DataFrame - Estrutura de dados do pandas
    """
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json"
    req = requests.get(url)
    dados = req.json()
    df = pd.json_normalize(dados['value'])
    df['datatrimestre'] = pd.to_datetime(df['datatrimestre'])
    return df
    
