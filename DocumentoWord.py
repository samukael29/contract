from docx import Document

def carrega_contrato_template():
    documento = Document("Contrato.docx")
    return documento


def salvar_documento(nome_novo_documento, documento):
    return documento.save(nome_novo_documento)