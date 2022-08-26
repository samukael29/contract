from asyncio import subprocess
import re
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#importing created objects
import sqlite
import contract
import excel_document

def bind_treeview(table):
    trv.delete(*trv.get_children())
    for i in table:
        trv.insert('','end',values=i)


def list():
    table = sqlite.list_all()
    bind_treeview(table)
    clear_boxes()

def search():
    table = sqlite.get_by_name(varSearch.get())    
    bind_treeview(table)

def get_row_information(event):
    rowid = trv.identify_row(event.y)
    selected_item = trv.item(trv.focus())
    i = 0
    for element in header:
        variable = f"var{element}" 
        command = f"{variable}.set(selected_item['values'][{i}])"
        exec(command)
        i = i + 1

def clear_boxes():
    for element in header:
        variable = f"var{element}" 
        command = f"{variable}.set('')"
        exec(command)
 
def generate_paramethers_get():
    paramethers = ""   
    i = 1
    for element in header:    
        paramethers = paramethers + f"var{element}.get()"
        if(i < len(header)):
            paramethers = paramethers + ","
        i =i+1

    return paramethers

def update_record():
    if messagebox.askyesno("Confirmation","Do you really want to update it?"):
        result = generate_paramethers_get()
        command = f"sqlite.update_registro({result})"
        print(command)
        exec(command)
        list()
    else:
        return True

def add_new_record():
    result = generate_paramethers_get()
    command = f"sqlite.criar_novo_registro({result})"
    list()

def delete_record():
    if messagebox.askyesno("Confirmar a deleção?", "Tem certeza que deseja excluir?"):
        # sqlite.apagar(varnome.get())
        list()
    else:
        return True

def generate_contract_from_database():
        contract.fill_contract_from_database()

def generate_contract_from_excel():
    contract.fill_contract_from_excel_file()

def export_database_to_excel():
    table = sqlite.list_all()
    excel_document.create_file(table,header)





#Creating the screen
root = Tk()
root.title("My Application")
root.geometry("800x700")


#declare general variables
header = ['Nome','Item1','Item2','Item3']
varSearch = StringVar()

for element in header:
    var = f"var{element}"
    command = f"var{element} = StringVar()"
    exec(command)


#creating wappers
wrapper1 = ttk.Labelframe(root, text="Customer List")
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)

wrapper2 = ttk.Labelframe(root, text="Search")
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)

wrapper3 = ttk.Labelframe(root, text="Customer Data")
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)



#adding items to Wrapper1
trv = ttk.Treeview(wrapper1,columns=(1,2,3,4),show="headings",height="6")
trv.pack()
for i, element in enumerate(header):
    trv.heading(i+1,text=f"{element}")
trv.bind('<Double 1>',get_row_information)
list() #populating treeview


#adding items to Wrapper2
lblsearch = Label(wrapper2,text="Search")
lblsearch.pack(side=tk.LEFT, padx=10)

entsearch = Entry(wrapper2,textvariable=varSearch)
entsearch.pack(side=tk.LEFT,padx=6)

btnsearch = Button(wrapper2, text="Search", command=search)
btnsearch.pack(side=tk.LEFT,padx=6)

btnclear = Button(wrapper2, text="Clear", command=list)
btnclear.pack(side=tk.LEFT,padx=6)


#adding items to Wrapper3
for i, element in enumerate(header):

    label = f"lbl{element}" 
    label = Label(wrapper3, text=f"{element}")
    label.grid(row=i,column=0,padx=5,pady=3)

    entry = f"ent{element}"
    textvariable = f"var{element}"
    command = f"{entry} = Entry(wrapper3,textvariable={textvariable})"
    exec(command)
    command =f"{entry}.grid(row={i},column=1,padx=5,pady=3)"
    exec(command)

    
up_btn = Button(wrapper3, text="Update", command=update_record)
up_btn.grid(row=4,column=0,padx=5,pady=3)

add_btn = Button(wrapper3, text="Add New", command=add_new_record)
add_btn.grid(row=4,column=1,padx=5,pady=3)

delete_btn = Button(wrapper3, text="Delete", command=delete_record)
delete_btn.grid(row=4,column=2,padx=5,pady=3)


btn_generate_contract_from_database = Button(wrapper3, text="Generate contract from database", command=generate_contract_from_database)
btn_generate_contract_from_database.grid(row=0,column=6,padx=5,pady=3)

btn_generate_contract_from_excel = Button(wrapper3, text="Generate contract from excel", command=generate_contract_from_excel)
btn_generate_contract_from_excel.grid(row=1,column=6,padx=5,pady=3)

btn_export_database_to_excel = Button(wrapper3, text="Export database to excel", command=export_database_to_excel)
btn_export_database_to_excel.grid(row=2,column=6,padx=5,pady=3)

root.mainloop()
