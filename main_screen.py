from asyncio import subprocess
import re
import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from turtle import window_height
from webbrowser import get

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
        if(str({element})!= str("{'Id'}")):
            command1 =  f"var{element}.get()"
            command2 =  f'result = {command1}'
            exec(command2,globals())
            paramethers = paramethers + f"'{result}'"
            if(i < len(header)-1):
                paramethers = paramethers + ","
            i =i+1

    return paramethers

def update_record():
    if messagebox.askyesno("Confirmation","Do you really want to update it?"):
        result = generate_paramethers_get()
        command = f"sqlite.update_registro({result})"
        exec(command)
        list()
    else:
        return True

def add_new_record():
    if(selected_value.get()== "DataBase"):
        result = generate_paramethers_get()
        sqlite.criar_novo_registro(result)
        list()
    else: 
        return True




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
header = sqlite.list_table_fields("Bens")
varSearch = StringVar()

for element in header:
    var = f"var{element}"
    command = f"var{element} = StringVar()"
    exec(command)


#creating wappers

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.pack(expand = 1, fill ="both")

wrapper1 = ttk.Labelframe(tab1, text="Customer List")
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)

wrapper2 = ttk.Labelframe(tab1, text="Search")
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)

wrapper4 = ttk.Labelframe(tab1, text="Where do you want to save the information?")
wrapper4.pack(fill="both", expand="yes", padx=20, pady=10)

wrapper3 = ttk.Labelframe(tab1, text="Customer Data")
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)



#adding items to Wrapper1
trv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5),show="headings",height="6")
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
    if(str({element})!= str("{'Id'}")):
        label = f"lbl{element}" 
        label = Label(wrapper3, text=f"{element}")
        label.grid(row=i,column=0,padx=5,pady=3)

        entry = f"ent{element}"
        textvariable = f"var{element}"
        command = f"{entry} = Entry(wrapper3,textvariable={textvariable})"
        exec(command)
        command =f"{entry}.grid(row={i},column=1,padx=5,pady=3)"
        exec(command)


#adding items to Wrapper4
#creating radiobutton

selected_value = tk.StringVar()
values = (('Database', 'DataBase'),
         ('Excel File', 'Excel'))

grid_column = 0
for value in values:
    radiobutton = ttk.Radiobutton(
        wrapper4,
        text=value[0],
        value=value[1],
        variable=selected_value
    )
    radiobutton.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    grid_column += 1

selected_value.set('DataBase')

def show_selected_value():
    showinfo(
        title='Result',
        message=selected_value.get()
    )

btndisplaymessage = Button(wrapper4,text="Get Selected Size",command=show_selected_value)
btndisplaymessage.grid(row=0,column=7,padx=5,pady=3)


#creating buttons
up_btn = Button(wrapper3, text="Update", command=update_record)
up_btn.grid(row=0,column=7,padx=5,pady=3)

add_btn = Button(wrapper3, text="Add New", command=add_new_record)
add_btn.grid(row=1,column=7,padx=5,pady=3)

delete_btn = Button(wrapper3, text="Delete", command=delete_record)
delete_btn.grid(row=2,column=7,padx=5,pady=3)


btn_generate_contract_from_database = Button(wrapper3, text="Generate contract from database", command=generate_contract_from_database)
btn_generate_contract_from_database.grid(row=0,column=8,padx=5,pady=3)

btn_generate_contract_from_excel = Button(wrapper3, text="Generate contract from excel", command=generate_contract_from_excel)
btn_generate_contract_from_excel.grid(row=1,column=8,padx=5,pady=3)

btn_export_database_to_excel = Button(wrapper3, text="Export database to excel", command=export_database_to_excel)
btn_export_database_to_excel.grid(row=2,column=8,padx=5,pady=3)

root.mainloop()
