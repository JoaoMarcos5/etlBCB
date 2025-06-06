import pandas as pd
import sqlite3
from sqlalchemy import create_engine

def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    """
    Salva um DataFrame do Pandas em um arquivo CSV com configurações personalizadas.

    Parâmetros:
    df (pd.DataFrame): O DataFrame a ser salvo.
    nome_arquivo (str): Nome do arquivo de destino (ex: "dados.csv").
    separador (str): Caractere utilizado para separar as colunas (ex: "," ou ";").
    decimal (str): Caractere usado para representar casas decimais (ex: "." ou ",").

    Retorno:
    None: A função apenas salva o arquivo e não retorna nenhum valor.
    """
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
    return

def salvarSQLite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):
    """
    Salva um DataFrame do Pandas em uma tabela de um banco de dados SQLite.

    Parâmetros:
    df (pd.DataFrame): O DataFrame a ser salvo.
    nome_banco (str): Nome do arquivo do banco de dados SQLite (ex: "dados.db").
    nome_tabela (str): Nome da tabela onde os dados serão inseridos.

    Retorno:
    None: A função apenas salva os dados no banco e não retorna nenhum valor.
    """
    conn = sqlite3.connect(nome_banco)

    df.to_sql(nome_tabela, conn, if_exists='replace', index=False)

    conn.close()

    return


def salvarMySql(
        df: pd.DataFrame, usuario: str, senha: str, host: str, banco: str, nome_tabela: str
        ):
    """
    Salva um DataFrame do Pandas em uma tabela de um banco de dados MySQL.

    Parâmetros:
    df (pd.DataFrame): O DataFrame a ser salvo.
    usuario (str): Nome do usuário do banco de dados.
    senha (str): Senha do usuário do banco de dados.
    host (str): Endereço do servidor MySQL (ex: "localhost" ou IP).
    banco (str): Nome do banco de dados onde os dados serão inseridos.
    nome_tabela (str): Nome da tabela onde os dados serão inseridos.

    Retorno:
    None: A função apenas salva os dados no banco e não retorna nenhum valor.
    """
    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")

    df.to_sql(nome_tabela, con=engine, if_exists='replace', index=False)

    return
