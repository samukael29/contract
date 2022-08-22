from abc import update_abstractmethods
from cProfile import label
from operator import truediv
from re import search
import sqlite3
from tarfile import PAX_FIELDS
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from turtle import clear
import Sqlite

def update(tabela):
    trv.delete(*trv.get_children())
    for i in tabela:
        trv.insert('','end',values=i)


def clear():
    tabela = Sqlite.listar()
    update(tabela)

def search():
    tabela = Sqlite.buscar(varnome.get())    
    # tabela = Sqlite.buscar(ent.get())
    update(tabela)

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    varnome.set(item['values'][0])
    varitem1.set(item['values'][1])
    varitem2.set(item['values'][2])
    varitem3.set(item['values'][3])


def update_customer():
    if messagebox.askyesno("Confirmar","Deseja realmente alterar?"):
        Sqlite.update_registro(varnome.get(),varitem1.get(),varitem2.get(),varitem3.get())
        clear()
    else:
        return True

def add_new():
    Sqlite.criar_novo_registro(varnome.get(),varitem1.get(),varitem2.get(),varitem3.get())
    clear()

def delete_customer():
    if messagebox.askyesno("Confirmar a deleção?", "Tem certeza que deseja excluir?"):
        Sqlite.apagar(varnome.get())
        clear()
    else:
        return True







root = Tk()
varnome = StringVar()
varitem1 = StringVar()
varitem2 = StringVar()
varitem3 = StringVar()


wrapper1 = ttk.Labelframe(root, text="Customer List")
wrapper2 = ttk.Labelframe(root, text="Search")
wrapper3 = ttk.Labelframe(root, text="Customer Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

trv = ttk.Treeview(wrapper1,columns=(1,2,3,4),show="headings",height="6")
trv.pack()

# trv.heading(1,text="ID")
trv.heading(1,text="Nome")
trv.heading(2,text="Item1")
trv.heading(3,text="Item2")
trv.heading(4,text="Item3")

trv.bind('<Double 1>',getrow)



#Listar registros
tabela = Sqlite.listar()
update(tabela)

#Procura
lblsearch = Label(wrapper2,text="Search")
lblsearch.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2,textvariable=varnome)
ent.pack(side=tk.LEFT,padx=6)
btn = Button(wrapper2, text="Search", command=search)
btn.pack(side=tk.LEFT,padx=6)
cbtn = Button(wrapper2, text="Clear", command=clear)
cbtn.pack(side=tk.LEFT,padx=6)

#User data selection
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

up_btn = Button(wrapper3, text="Update", command=update_customer)
add_btn = Button(wrapper3, text="Add New", command=add_new)
delete_btn = Button(wrapper3, text="Delete", command=delete_customer)

add_btn.grid(row=4,column=0,padx=5,pady=3)
up_btn.grid(row=4,column=1,padx=5,pady=3)
delete_btn.grid(row=4,column=3,padx=5,pady=3)

root.title("My Application")
root.geometry("800x700")
root.mainloop()
