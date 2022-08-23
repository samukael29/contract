from msilib.schema import Directory
from docx import Document


def load_template_contract():
    document = Document("Contrato.docx")
    return document


def save_document(file_name, document):
    return document.save(file_name)

