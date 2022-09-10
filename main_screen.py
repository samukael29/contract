import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#-------------------------------------------------------------------------------------------------#
#importing created objects
import sqlite
import contract
import excel_document

#-------------------------------------------------------------------------------------------------#
#Starting the screen and set caracteristics
root = Tk()
root.title("My Application")
root.geometry("1200x700")

#-------------------------------------------------------------------------------------------------#
#Declaring global variables
header = sqlite.list_table_fields()

#-------------------------------------------------------------------------------------------------#
#Starting the page
tabControl = ttk.Notebook(root)

#Creating frames
tab_frame_database = ttk.Frame(tabControl)
tab_frame_excel = ttk.Frame(tabControl)

#Creating tabs and add it to created frame
tabControl.add(tab_frame_database, text ='DataBase')
tabControl.add(tab_frame_excel, text ='Excel')
tabControl.pack(expand = 1, fill ="both")

#Creating wrappers inside each tab
wrapper2 = ttk.Labelframe(tab_frame_database, text="Search")
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper1 = ttk.Labelframe(tab_frame_database, text="Customer List")
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3 = ttk.Labelframe(tab_frame_database, text="Customer Data")
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

#-------------------------------------------------------------------------------------------------#
#Creating dinamically label and editbox based on database table columns
for element in header:
    var = f"var{element}"
    command = f"var{element} = StringVar()"
    exec(command)

def get_values():  
    values = []
    empty_value = 0
    i = 1
    for element in header:    
        command1 =  f"var{element}.get()"
        command2 =  f'result = {command1}'
        exec(command2,globals())
        values.append(result)
        if (result == "" and str({element})!= str("{'Id'}")):
            empty_value = 1

    return values, empty_value

def clear_boxes():
    for element in header:
        variable = f"var{element}" 
        command = f"{variable}.set('')"
        exec(command)

for i, element in enumerate(header):
    if(str({element})!= str("{'Id'}")):
        label = f"lbl{element}" 
        label = Label(wrapper3, text=f"{element}")
        label.grid(row=i-1,column=0,padx=5,pady=3)

        entry = f"ent{element}"
        textvariable = f"var{element}"
        command = f"{entry} = Entry(wrapper3,textvariable={textvariable})"
        exec(command)
        command =f"{entry}.grid(row={i-1},column=1,padx=5,pady=3)"
        exec(command)
        
#-------------------------------------------------------------------------------------------------#
#Implementing label and editbox to search information on grid
def search():
    table = sqlite.search_record(varSearch.get())    
    bind_treeview(table)

varSearch = StringVar()
varSearch.trace("w", lambda name, index, mode, varSearch=varSearch: search())

lblsearch = Label(wrapper2,text="Type to search")
lblsearch.grid(row=0,column=0)
entsearch = Entry(wrapper2,textvariable=varSearch,width=100)
entsearch.grid(row=0,column=1)

#-------------------------------------------------------------------------------------------------#
#Implementing radiobutton
def selected_value_radio():
    list()

selected_value = StringVar()
selected_value.trace("w", lambda name, index, mode, selected_value=selected_value: selected_value_radio())
values = (('Show all registers', 'AllRegisters'),
         ('Show only first four registers', 'OnlyFirstFour'))

grid_column = 0
for value in values:
    radiobutton = ttk.Radiobutton(
        wrapper2,
        text=value[0],
        value=value[1],
        variable=selected_value
    )
    radiobutton.grid(column=grid_column, row=1)
    grid_column += 1
selected_value.set('AllRegisters')

#-------------------------------------------------------------------------------------------------#
#Implementing treeview
def list():
    table = sqlite.list_all()
    bind_treeview(table)
    varSearch.set('')
    clear_boxes()

def get_row_information(event):
    rowid = trv.identify_row(event.y)
    selected_item = trv.item(trv.focus())
    i = 0
    for element in header:
        variable = f"var{element}" 
        command = f"{variable}.set(selected_item['values'][{i}])"
        exec(command)
        i = i + 1

def bind_treeview(table):
    trv.delete(*trv.get_children())
    if (selected_value.get() == "AllRegisters"):
        for i in table:
            trv.insert('','end',values=i)
    else: 
        if (selected_value.get() == "OnlyFirstFour"):
            x=1
            for i in table:
                if(x <=4):
                    trv.insert('','end',values=i)
                x=x+1

trv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5),show="headings",height="6")
trv.pack()
for i, element in enumerate(header):
    trv.heading(i+1,text=f"{element}")
trv.bind('<Double 1>',get_row_information)
list() 

#-------------------------------------------------------------------------------------------------#
#Implementing inserting button
def add_new_record():
# if(selected_value.get()== "DataBase"):
    result,empty_value = get_values()
    if(empty_value == 0):
        sqlite.new_record(result)
    else:
        showinfo(title='Campo(s) em branco',message="Um ou mais campos estão em branco. Você deve preencher todos os campos para salvar")
    list()

add_btn = Button(wrapper3, text="Add New", command=add_new_record)
add_btn.grid(row=0,column=7,padx=5,pady=3)

#-------------------------------------------------------------------------------------------------#
#Implementing updating button
def update_record():
    result,empty_value = get_values()
    if(empty_value == 0):
        if messagebox.askyesno("Confirmation","Do you really want to update it?"):
            sqlite.update_record(result)
    else:
        showinfo(title='Campo(s) em branco',message="Um ou mais campos estão em branco. Você deve preencher todos os campos para salvar")
    list()

up_btn = Button(wrapper3, text="Update", command=update_record)
up_btn.grid(row=1,column=7,padx=5,pady=3)

#-------------------------------------------------------------------------------------------------#
#Implementing deleting button
def delete_record():
    result,empty_value = get_values()
    if(empty_value == 0):
        if messagebox.askyesno("Confirmar a deleção?", "Tem certeza que deseja excluir?"):
            sqlite.delete_record(result)
    else:
        showinfo(title='Id em branco',message="Um item deve ser selecionado para ser excluido")
    list()

delete_btn = Button(wrapper3, text="Delete", command=delete_record)
delete_btn.grid(row=2,column=7,padx=5,pady=3)

#-------------------------------------------------------------------------------------------------#
#Implementing generate contract from database button
def generate_contract_from_database():
        contract.fill_contract_from_database()

btn_generate_contract_from_database = Button(wrapper3, text="Generate contract from database", command=generate_contract_from_database)
btn_generate_contract_from_database.grid(row=0,column=8,padx=5,pady=3)

#-------------------------------------------------------------------------------------------------#
#Implementing generate contract from excel button
def generate_contract_from_excel():
    contract.fill_contract_from_excel_file()

btn_generate_contract_from_excel = Button(wrapper3, text="Generate contract from excel", command=generate_contract_from_excel)
btn_generate_contract_from_excel.grid(row=1,column=8,padx=5,pady=3)

#-------------------------------------------------------------------------------------------------#
#Implementing Export database to excel button
def export_database_to_excel():
    table = sqlite.list_all()
    excel_document.create_file(table,header)

btn_export_database_to_excel = Button(wrapper3, text="Export database to excel", command=export_database_to_excel)
btn_export_database_to_excel.grid(row=2,column=8,padx=5,pady=3)

#-------------------------------------------------------------------------------------------------#
#Implementing save to spreadsheet button
def save_to_spreadsheet():
    result,empty_value = get_values()
    if(empty_value == 0):
        excel_document.adding_information_to_excel_file(header,result)
    else:
        showinfo(title='Campo(s) em branco',message="Um ou mais campos estão em branco. Você deve preencher todos os campos para salvar")
    list()

btn_save_to_spreadsheet = Button(wrapper3, text="Save to spreadsheet", command=save_to_spreadsheet)
btn_save_to_spreadsheet.grid(row=3,column=8,padx=5,pady=3)

#-------------------------------------------------------------------------------------------------#
#Finishing the screen
root.mainloop()

#-------------------------------------------------------------------------------------------------#

