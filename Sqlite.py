import sqlite3
from unicodedata import name
from unittest import result

#variables
databasename = "Banco.db"
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
    created_string = f"create table {tablename} ({string_fields_in_line})"
    return created_string



def verify_if_table_exists(cursor):
    listOfTables = cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tablename}'").fetchall()
    if listOfTables == []:
        cursor.execute(string_to_create_table())

def create_database():
    banco = sqlite3.connect(f"{databasename}")
    cursor = banco.cursor()
    return banco,cursor


def new_record(values):
    banco, cursor = create_database()
    verify_if_table_exists(cursor)

    line = ""
    fields = ""
    i = 0
    for field in list_table_fields():
        if(str({field})!= str("{'Id'}")):
            fields = fields + f"{field}"
            line = line + f"'{values[i]}'"
            if(i < len(list_table_fields())-1):
                fields = fields + ","                
                line = line + ","
        i=i+1

    command = (f"Insert into {tablename} ({fields}) values ({line})")
    cursor.execute(command)
    banco.commit()

def update_record(values):
    banco, cursor = create_database()
    verify_if_table_exists(cursor)

    line = ""
    i = 0
    for field in list_table_fields():
        if(str({field})== str("{'Id'}")):
            line_id = f"{field} = {values[i]}" 
        else:    
            line = line + f"{field} = '{values[i]}'"
            if(i < len(list_table_fields())-1):
                line = line + ","
        i=i+1

    command = f"update {tablename} set {line} where {line_id}"  
    cursor.execute(command)
    banco.commit()


def search_record(value):
    banco, cursor = create_database()
    verify_if_table_exists(cursor)

    line = ""
    i = 0
    for field in list_table_fields():
        line = line + f"{field} like '%{value}%'"
        if(i < len(list_table_fields())-1):
            line = line + "or "
        i=i+1

    command = f"select * from {tablename} where {line}"  
    cursor.execute(command)
    result = cursor.fetchall()
    return result

def list_all():
    banco, cursor = create_database()
    verify_if_table_exists(cursor)
    cursor.execute(f"select * from {tablename}")
    retorno = cursor.fetchall()
    return retorno

def delete_record(values):
    banco, cursor = create_database()
    verify_if_table_exists(cursor)

    line = ""
    table_columns = ""
    i = 0
    for field in list_table_fields():
        if(str({field})== str("{'Id'}")):
            table_columns = field
            line = values[i]

    command = f"delete from  {tablename} where {table_columns} = {line}"
    cursor.execute(command)
    banco.commit()


def list_table_fields():
    banco, cursor = create_database()
    verify_if_table_exists(cursor)
    cursor.execute(f"select * from {tablename}")
    names = [description[0] for description in cursor.description]
    return names