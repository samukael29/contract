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


def save_spreadsheet(dataframe):
    writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
    dataframe.to_excel(writer, sheet_name='Sheet1', index=True)
    writer.save()

def adding_information_to_excel_file(header,values):
    
    dataframe = pd.DataFrame()
    row = ""
    i =0
    for item in header:
        if(str({item})!= str("{'Id'}")):
            row = row + f"{item} : ['{values[i]}']"
            if(i < len(header)-1):
                row = row + ","
        i=i+1
    
    print(row)
    dataframe.
    print(dataframe)

    
    # dataframe = pd.DataFrame({'Name': ['Samuel', 'Judite', 'Genoveva', 'Cleidiane'],
    #                 'Age': [40, 50, 60, 70]})

    # save_spreadsheet(dataframe)
