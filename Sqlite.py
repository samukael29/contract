import sqlite3

#variables
databasename = "banco.db"
tablename =  "Bens"
table_dictionary = {
    'Id':'INTEGER PRIMARY KEY AUTOINCREMENT',
    'Nome':'text',
    'Item1':'text',
    'Item2':'text',
    'Item3':'text'
}

def string_to_create_table():
    string_fields_in_line = ""   
    i = 1
    for item in table_dictionary.items():    
        string_fields_in_line = string_fields_in_line + f"{item[0]} {item[1]}"
        if(i < len(table_dictionary)):
            string_fields_in_line = string_fields_in_line + ","
        i =i+1
    create_string = f"create table Bens ({string_fields_in_line})"


def verificar_tabela_existe(cursor):
    listOfTables = cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tablename}'").fetchall()
    if listOfTables == []:
        # cursor.execute("create table Bens (Nome text, Item1 text, Item2 text, Item3 text)")
        cursor.execute(string_to_create_table())


def excluir_tudo(banco, cursor):
    cursor.execute("Delete from Bens")
    banco.commit()


def criar_banco():
    banco = sqlite3.connect(f"{databasename}")
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
    cursor.execute(f"select * from {tablename}")
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

def list_table_fields(tablename):
    banco, cursor = criar_banco()
    verificar_tabela_existe(cursor)
    cursor.execute(f"select * from {tablename}")
    names = [description[0] for description in cursor.description]
    return names

