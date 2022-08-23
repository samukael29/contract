import sqlite3


def verificar_tabela_existe(cursor):
    listOfTables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Bens'").fetchall()
    if listOfTables == []:
        cursor.execute("create table Bens (Nome text, Item1 text, Item2 text, Item3 text)")


def excluir_tudo(banco, cursor):
    cursor.execute("Delete from Bens")
    banco.commit()


def criar_banco():
    banco = sqlite3.connect('banco.db')
    cursor = banco.cursor()
    return banco,cursor


def criar_novo_registro(nome,item1, item2, item3):
    banco, cursor = criar_banco()
    verificar_tabela_existe(cursor)
    comando = (f"Insert into Bens values ('{nome}', '{item1}','{item2}','{item3}')")
    cursor.execute(comando)
    banco.commit()

def update_registro(nome,item1, item2, item3):
    banco, cursor = criar_banco()
    verificar_tabela_existe(cursor)
    comando = (f"update Bens set Nome ='{nome}', Item1 = '{item1}', Item2 ='{item2}', Item3 ='{item3}' where Nome='{nome}'")
    cursor.execute(comando)
    banco.commit()


def limpar_tabela():
    banco, cursor = criar_banco()
    verificar_tabela_existe(cursor)
    excluir_tudo(banco, cursor)


def list_all():
    banco, cursor = criar_banco()
    verificar_tabela_existe(cursor)
    cursor.execute("select * from  Bens")
    retorno = cursor.fetchall()
    return retorno

def apagar(nome):
    banco, cursor = criar_banco()
    verificar_tabela_existe(cursor)
    comando = f"delete from  Bens where Nome ='{nome}'"
    cursor.execute(comando)
    banco.commit()

def get_by_name(nome):
    banco, cursor = criar_banco()
    verificar_tabela_existe(cursor)
    comando = (f"Select * from Bens where Nome like '%{nome}%'")
    cursor.execute(comando)
    return cursor.fetchall()
