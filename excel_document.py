import pandas as pd
from datetime import datetime

def load_file():
    table = pd.read_excel("Informações.xlsx")
    return table

def dictionary(table, line):
    nome = table.loc[line, "Nome"]
    item1 = table.loc[line, "Item1"]
    item2 = table.loc[line, "Item2"]
    item3 = table.loc[line, "Item3"]

    references = {
        "XXXX": nome,
        "YYYY": item1,
        "ZZZZ": item2,
        "WWWW": item3,
        "DD": str(datetime.now().day),
        "MM": str(datetime.now().month),
        "AAAA": str(datetime.now().year), 
    }
    return references