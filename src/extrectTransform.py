import requests
import pandas as pd


def requestApiBcb(data) -> pd.DataFrame:

    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json"
    req = requests.get(url)
    print("status code", req.status_code)
    dados = req.json()

    df = pd.json_normalize(dados["value"])
    df["datatrimestre"] = pd.to_datetime(df["datatrimestre"])

    return df
