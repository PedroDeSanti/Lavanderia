from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from telas_funcionario import *



con = mysql.connect(host="localhost", user='root', password='Pontofrio-1', database='projetobd')

# janela = Tk() 

# AINDA PRECISA SER FEITA
def tela_de_cliente(janela):
    
    #global janela
    janela.destroy()
    janela = Tk()
    janela.geometry("600x600+300+50")
    janela.title("Tela de Cliente")
    label = Label(janela, text='Tela de Cliente')
    label.pack() 

    seus_pedidos = Button(janela, text='Seus pedidos',command=lambda: tela_de_listar_pedidos_cliente)
    seus_pedidos.place(x=100,y=150)
    fazer_pedido_cliente = Button(janela, text='Fazer pedido',command=lambda: tela_de_fazer_pedido_cliente)
    fazer_pedido_cliente.place(x=180,y=300)

    janela.mainloop()

# AINDA PRECISA SER FEITA
def tela_de_listar_pedidos_cliente(janela):
    
    #global janela
    janela.destroy()
    janela = Tk()
    janela.geometry("600x600+300+50")
    global abcd
    abcd = "Tla de Pedidos"
    janela.title(str(abcd))
    label = Label(janela, text=str(abcd))
    label.pack() 
    vlist = ["Option1", "Option2", "Option3",
          "Option4", "Option5"]
 
    Combo = ttk.Combobox(janela, values = vlist)
    Combo.set("Pick an Option")
    Combo.pack(padx = 5, pady = 5)
    
    pass

# SERÁ FEITA?
def tela_de_fazer_pedido_cliente(janela):
    # global janela
    janela.destroy()
    janela = Tk()
    janela.geometry("600x600+300+50")
    global nomeTela
    nomeTela = "Faça um pedido"
    janela.title(nomeTela)
    label = Label(janela, text=str(abcd))
    label.pack() 
    lista_roupas = ["Camisa", "Calça", "Cueca",
          "Shorts", "Sutiã", "Terno"]
 
    SelecionaRoupa = ttk.Combobox(janela, values = lista_roupas)
    SelecionaRoupa.set("Escolha o tipo de roupa que será cadastrado no pedido")
    SelecionaRoupa.pack(padx = 5, pady = 5)
    pass