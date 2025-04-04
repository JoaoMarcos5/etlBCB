import pandas as pd



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
def salvarCsv(df:pd.DataFrame, nome_arquivo:str, separador: str,decimal: str):
    df.to_csv(nome_arquivo, sep=separador,decimal=decimal)
    return
