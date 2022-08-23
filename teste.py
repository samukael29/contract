import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Sqlite

def bind_treeview(table):
    trv.delete(*trv.get_children())
    for i in table:
        trv.insert('','end',values=i)


def list():
    table = Sqlite.list_all()
    bind_treeview(table)
    clear_boxes()

def search():
    table = Sqlite.get_by_name(varnomesearch.get())    
    bind_treeview(table)

def get_row_information(event):
    rowid = trv.identify_row(event.y)
    selected_item = trv.item(trv.focus())
    varnome.set(selected_item['values'][0])
    varitem1.set(selected_item['values'][1])
    varitem2.set(selected_item['values'][2])
    varitem3.set(selected_item['values'][3])


def clear_boxes():
    varnome.set("")
    varnomesearch.set("")
    varitem1.set("")
    varitem2.set("")
    varitem3.set("")

def update_record():
    if messagebox.askyesno("Confirmation","Do you really want to update it?"):
        Sqlite.update_registro(varnome.get(),varitem1.get(),varitem2.get(),varitem3.get())
        list()
    else:
        return True

def add_new_record():
    Sqlite.criar_novo_registro(varnome.get(),varitem1.get(),varitem2.get(),varitem3.get())
    list()

def delete_record():
    if messagebox.askyesno("Confirmar a deleção?", "Tem certeza que deseja excluir?"):
        Sqlite.apagar(varnome.get())
        list()
    else:
        return True

def generate_contract_from_database():
    return True

def generate_contract_from_excel():
    return True

def export_database_to_excel():
    return True





#Creating the screen
root = Tk()
root.title("My Application")
root.geometry("800x700")


#declare general variables
varnome = StringVar()
varnomesearch = StringVar()
varitem1 = StringVar()
varitem2 = StringVar()
varitem3 = StringVar()


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

trv.heading(1,text="Nome")
trv.heading(2,text="Item1")
trv.heading(3,text="Item2")
trv.heading(4,text="Item3")
trv.bind('<Double 1>',get_row_information)
list() #populating treeview


#adding items to Wrapper2
lblsearch = Label(wrapper2,text="Search")
lblsearch.pack(side=tk.LEFT, padx=10)

entsearch = Entry(wrapper2,textvariable=varnomesearch)
entsearch.pack(side=tk.LEFT,padx=6)

btnsearch = Button(wrapper2, text="Search", command=search)
btnsearch.pack(side=tk.LEFT,padx=6)

btnclear = Button(wrapper2, text="Clear", command=list)
btnclear.pack(side=tk.LEFT,padx=6)


#adding items to Wrapper3
lbl1 = Label(wrapper3, text="Nome")
lbl1.grid(row=0,column=0,padx=5,pady=3)
ent1 = Entry(wrapper3,textvariable=varnome)
ent1.grid(row=0,column=1,padx=5,pady=3)

lbl2 = Label(wrapper3, text="Item1")
lbl2.grid(row=1,column=0,padx=5,pady=3)
ent2 = Entry(wrapper3,textvariable=varitem1)
ent2.grid(row=1,column=1,padx=5,pady=3)

lbl3 = Label(wrapper3, text="Item2")
lbl3.grid(row=2,column=0,padx=5,pady=3)
ent3 = Entry(wrapper3,textvariable=varitem2)
ent3.grid(row=2,column=1,padx=5,pady=3)

lbl4 = Label(wrapper3, text="Item3")
lbl4.grid(row=3,column=0,padx=5,pady=3)
ent4 = Entry(wrapper3,textvariable=varitem3)
ent4.grid(row=3,column=1,padx=5,pady=3)

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
