import pandas as pd
from datetime import datetime

def carrega_tabela_dados():
    tabela = pd.read_excel("Informações.xlsx")
    return tabela

def dicionario(tabela, linha):
    nome = tabela.loc[linha, "Nome"]
    item1 = tabela.loc[linha, "Item1"]
    item2 = tabela.loc[linha, "Item2"]
    item3 = tabela.loc[linha, "Item3"]

    referencias = {
        "XXXX": nome,
        "YYYY": item1,
        "ZZZZ": item2,
        "WWWW": item3,
        "DD": str(datetime.now().day),
        "MM": str(datetime.now().month),
        "AAAA": str(datetime.now().year), 
    }
    return referencias