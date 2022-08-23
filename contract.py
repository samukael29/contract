import sqlite3
import DocumentoWord
import DocumentoExcel
from importlib.abc import TraversableResources
import sqlite
from datetime import datetime


def fill_contract_from_excel_file():
    tabela = DocumentoExcel.carrega_tabela_dados()

    for linha in tabela.index:
        documento = DocumentoWord.carrega_contrato_template()

        referencias = DocumentoExcel.dicionario(tabela, linha)

        for paragrafo in documento.paragraphs:
            for codigo in referencias:
                valor = referencias[codigo]
                paragrafo.text = paragrafo.text.replace(codigo, valor)

        nome_novo_documento = f"Contrato - {tabela.loc[linha,'Nome']}.docx"
        DocumentoWord.salvar_documento(nome_novo_documento, documento)


def fill_contract_from_database():
    tabela = sqlite.listar()

    for linha in tabela:
        documento = DocumentoWord.carrega_contrato_template()

        referencias = dicionario(linha)

        for paragrafo in documento.paragraphs:
            for codigo in referencias:
                valor = referencias[codigo]
                paragrafo.text = paragrafo.text.replace(codigo, valor)

        nome_novo_documento = f"Contrato - {linha[0]}.docx"
        DocumentoWord.salvar_documento(nome_novo_documento, documento)


def dicionario(linha):
    nome = linha[0]
    item1 = linha[1]
    item2 = linha[2]
    item3 = linha[3]

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