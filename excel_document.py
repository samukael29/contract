import pandas as pd
import numpy as np
from datetime import datetime
import openpyxl

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

def create_file(table,header):
    book = openpyxl.Workbook()

    #listas as sheets que ja existem no arquivo
    print(book.sheetnames)

    # criar uma nova sheet
    book.create_sheet('registros2')

    #selecionar uma sheet
    sheet = book['registros2']

    #adicionar dados em linhas
    sheet.append(header)
    for line in table:
        sheet.append(line)

    #salvar arquivo
    book.save('dados.xlsx')

# create_file()


