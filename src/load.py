import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    """
    Função criada para salvar o dataframe como um arquivo csv.

    Parameentro:
        df(pd.DataFrame): o datafrana que deve ser salvo.
        nome_arquivo(str): caminho e nome do arquivo de saída (ex:'dados.csv').
        separador(str): caractre usado para reprensentar o ponto decimal (ex:'.' ou ',').
        decimal(str): caractere usado para representar o ponto decimal(ex: '.' ou ',').

        saida esperada:
        o Dataframe deve ser salvo em um arquivo.csv







    """
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
    return


def salvarSqlite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):



    conn = sqlite3.connect(nome_banco)

    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)
    conn.close()

    return


def salvarMySql(
    df: pd.DataFrame, usuario: str, senha: str, host: str, banco: str, nome_tabela: str
):
    engine = create_engine(f"mysql+pysmysql://{usuario}:{senha}@{host}:{banco}")

    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)
