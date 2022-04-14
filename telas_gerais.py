from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

from telas_cliente import *
from telas_funcionario import *

con = mysql.connect(host="localhost", user='root', password='MySQLP@55W0rd', database='projetobd')


def tela_login():

    global janela
    janela.destroy()
    janela = Tk()
    janela.geometry("600x600+300+50")
    janela.title("Tela de Login")
    label = Label(janela, text='Tela de Login')
    label.pack() 


    insira_login = Label(janela, text='Insira seu Login', font=('bold',10))
    insira_login.place(x=20,y=30)
    e_insira_login = Entry()
    e_insira_login.place(x=20, y=60)

    insira_senha = Label(janela, text='Insira sua Senha', font=('bold',10))
    insira_senha.place(x=20,y=90)
    e_insira_senha = Entry()
    e_insira_senha.place(x=20, y=120)

    botao_acessar = Button(janela, text='Acessar',command=lambda:acessa_tela_correspondente(e_insira_login, e_insira_senha, janela))
    botao_acessar.place(x=100,y=150)

    criar_cadastro = Label(janela, text='Não tem conta? Crie uma', font=('bold',10))
    criar_cadastro.place(x=20,y=300)
    botao_criar_cadastro = Button(janela, text='AQUI',command= lambda: tela_criar_cadastro(janela))
    botao_criar_cadastro.place(x=180,y=300)
    
    teixte = Button(janela, text='TEIXTE',command=lambda:tela_consulta(janela))
    teixte.place(x=100, y=500)
    
    teixte2 = Button(janela, text='TEIXTE2',command=lambda:tela_de_listar_pedidos_cliente(janela))
    teixte2.place(x=150, y=550)
    
    teixte3 = Button(janela, text='TEIXTE3',command=lambda:tela_lista_pedidos_cliente(janela, "Gabriel Zambelli"))
    teixte3.place(x=50, y=550)

    param = ["0123","Oswaldoz","10/10/12","17/10/12","Finalizado","6"]

    teixte4 = Button(janela, text='FUNCIONÁRIO DO MÊS',command=lambda:tela_lista_pedido_id(janela,param))
    teixte4.place(x=300, y=500)


    janela.mainloop()




def acessa_tela_correspondente(login, senha, janela):
    '''Verifica se o login e senha se encontram no BD, e, se sim, leva o usuário à correspondente (cliente ou funcionário)'''
    # verifica se o login se encontra no BD
    cursor = con.cursor()
    comandoSQL = "select login, senha from cliente where login = '"+str(login.get())+"'"
    comandoSQL += "union "
    comandoSQL += "select login, senha from funcionario where login = '"+str(login.get())+"';"
    cursor.execute(comandoSQL)
    rows = cursor.fetchall()
    check_senha = 0
    if len(rows) == 0:
        MessageBox.showinfo("Erro!", "Verifique seu login!")
    else:
        for row in rows:
            if senha.get() == row[1]:
                check_senha = 1
                break
        if check_senha == 1:
            comandoSQL = "select exists(select * from cliente where login = '"+str(login.get())+"' and senha = '"+str(senha.get())+"');"
            cursor.execute(comandoSQL)
            if_cliente = cursor.fetchall()[0][0]
            if if_cliente:
                tela_de_cliente(janela)
            else:
                tela_funcionario(janela)
        else:
            MessageBox.showinfo("Erro!", "Verifique sua senha!")

janela = Tk() 
tela_login()