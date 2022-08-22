import requests
from  tkinter import ttk
from tkinter import *
import Sqlite

    
janela = Tk()

janela.title("Inserir novos bens")


def inserir_dados():
    nome = texto_nome.get()
    item1 = texto_item1.get()
    item2 = texto_item2.get()
    item3 = texto_item3.get()
    Sqlite.criar_novo_registro(nome,item1,item2, item3)
    limpar_tela()

def popular_tree():
    tabela = Sqlite.listar()
    i = 0
    for linha in tabela:
        tree.insert('',i,text="",values=(linha[0],linha[1],linha[2],linha[3]))
        i = i+1
    tree.pack()




def limpar_tela():
    texto_nome.delete(0,"end")
    texto_item1.delete(0,"end")
    texto_item2.delete(0,"end")
    texto_item3.delete(0,"end")
    texto_resposta['text'] = "Dados inseridos com sucesso"

def limpar_tabela():
    Sqlite.limpar_tabela()

def sair_tela():
    janela.destroy()

texto = Label(janela, text="Insira os bens")
texto.grid(column=1, row=0, padx=10, pady=10)

label_nome = Label(janela, text="Nome")
label_nome.grid(column=0, row=1, padx=10, pady=10)

texto_nome = Entry(janela, text="")
texto_nome.grid(column=1, row=1, padx=10, pady=10)

label_item1 = Label(janela, text="Item1")
label_item1.grid(column=0, row=2, padx=10, pady=10)

texto_item1 = Entry(janela, text="")
texto_item1.grid(column=1, row=2, padx=10, pady=10)

label_item2 = Label(janela, text="Item2")
label_item2.grid(column=0, row=3, padx=10, pady=10)

texto_item2 = Entry(janela, text="")
texto_item2.grid(column=1, row=3, padx=10, pady=10)

label_item3 = Label(janela, text="Item3")
label_item3.grid(column=0, row=4, padx=10, pady=10)

texto_item3 = Entry(janela, text="")
texto_item3.grid(column=1, row=4, padx=10, pady=10)

botao_salvar = Button(janela, text="Salvar", command=inserir_dados)
botao_salvar.grid(column=0, row=5, padx=10, pady=10)

botao_sair = Button(janela, text="Sair", command=sair_tela)
botao_sair.grid(column=1, row=5, padx=10, pady=10)

botao_limpar_tabela = Button(janela, text="Limpar banco", command=limpar_tabela)
botao_limpar_tabela.grid(column=2, row=5, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=1, row=6, padx=10, pady=10)

tree = ttk.Treeview(janela)

#Definir colunas
tree['columns'] = ("Nome", "Item1", "Item2", "Item3")

#formatar colunas
tree.column("#0",width=120,minwidth=25)
tree.column("Nome",anchor=W, width=120)
tree.column("Item1",anchor=CENTER, width=120)
tree.column("Item2",anchor=CENTER, width=120)
tree.column("Item3",anchor=CENTER, width=120)

#crear heading
tree.heading("#0", text="label", anchor=W)
tree.heading("Nome", text="Nome", anchor=W)
tree.heading("Item1", text="Item1", anchor=W)
tree.heading("Item2", text="Item2", anchor=W)
tree.heading("Item3", text="Item3", anchor=W)

#adicionar informações
popular_tree()


janela.mainloop()

    
