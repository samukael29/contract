import sqlite3
import word_document
import excel_document
from importlib.abc import TraversableResources
import sqlite
from datetime import datetime

import os

def get_directory():
    current_directory = os.getcwd()
    print (current_directory)
    dirName = 'Contracts'
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        
    new_directory = f"{current_directory}\{dirName}"
    return new_directory



def fill_contract_from_excel_file():

    directory = get_directory()

    table = excel_document.load_file()

    for line in table.index:
        document = word_document.load_template_contract()

        references = excel_document.dictionary(table, line)

        for paragraph in document.paragraphs:
            for code in references:
                value = references[code]
                paragraph.text = paragraph.text.replace(code, value)

        new_document = f"Contrato - {table.loc[line,'Nome']}.docx"
        filename = f"{directory}\{new_document}"

        word_document.save_document(filename, document)


def fill_contract_from_database():

    directory = get_directory()

    table = sqlite.list_all()

    for line in table:
        document = word_document.load_template_contract()

        references = dictionary(line)

        for paragraph in document.paragraphs:
            for code in references:
                value = references[code]
                paragraph.text = paragraph.text.replace(code, value)

        new_document = f"Contrato - {line[0]}.docx"
        filename = f"{directory}\{new_document}"
        word_document.save_document(filename, document)


def dictionary(line):
    nome = line[0]
    item1 = line[1]
    item2 = line[2]
    item3 = line[3]

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