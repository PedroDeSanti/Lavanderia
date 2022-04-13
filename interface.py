from tkinter import *
from tkinter import ttk

janela = Tk() 

abcd = '0'
def criar_usuario():
    global janela
    janela.destroy()
    janela = Tk() 
    label = Label(janela, text='Criar Usuario')
    label.pack()
    janela.geometry("600x600+300+50")
    menu_bt = Button(janela, text='Voltar/Menur',command=tela_login)
    menu_bt.pack()

def editar_usuario():
    global janela
    janela.destroy()
    janela = Tk() 
    label = Label(janela, text='Editar Usuario')
    label.pack()
    janela.geometry("600x600+300+50")
    menu_bt = Button(janela, text='Voltar/Menur',command=tela_login)
    menu_bt.pack()

def tela_de_cliente():
    
    global janela
    janela.destroy()
    janela = Tk()
    janela.geometry("600x600+300+50")
    janela.title("Tela de Cliente")
    label = Label(janela, text='Tela de Cliente')
    label.pack() 

    seus_pedidos = Button(janela, text='Seus pedidos',command=tela_de_listar_pedidos_cliente)
    fazer_pedido_cliente = Button(janela, text='Fazer pedido',command=tela_de_fazer_pedido_cliente)

    seus_pedidos.place(x=100,y=150)
    fazer_pedido_cliente.place(x=180,y=300)

    janela.mainloop()

def tela_de_listar_pedidos_cliente():
    
    global janela
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

def tela_de_fazer_pedido_cliente():
    pass

def tela_login():
    
    global janela
    janela.destroy()
    janela = Tk()
    janela.geometry("600x600+300+50")
    janela.title("Menu Principal")
    label = Label(janela, text='Menu Principal')
    label.pack() 


    insira_login = Label(janela, text='Insira seu Login', font=('bold',10))
    insira_login.place(x=20,y=30)

    e_insira_login = Entry()
    e_insira_login.place(x=20, y=60)

    insira_senha = Label(janela, text='Insira sua Senha', font=('bold',10))
    insira_senha.place(x=20,y=90)

    e_insira_senha = Entry()
    e_insira_senha.place(x=20, y=120)

    criar_cadastro = Label(janela, text='Não tem conta? Crie uma', font=('bold',10))
    criar_cadastro.place(x=20,y=300)

    botao_acessar = Button(janela, text='Acessar',command=acessa_tela_correspondente)
    botao_criar_cadastro = Button(janela, text='AQUI',command=tela_criar_cadastro)

    teixte = Button(janela, text='TEIXTE',command=tela_consulta)
    teixte.place(x=100, y=500)
    
    teixte2 = Button(janela, text='TEIXTE2',command=tela_de_listar_pedidos_cliente)
    teixte2.place(x=150, y=550)

    botao_acessar.place(x=100,y=150)
    botao_criar_cadastro.place(x=180,y=300)

    janela.mainloop()


def tela_criar_cadastro():
    global janela
    janela.destroy()
    janela = Tk() 
    label = Label(janela, text='Insira seus Dados')
    label.pack()
    janela.geometry("600x600+300+50")
    
    left_column = 20
    right_column = 320
    y_base = 120
    fonte=('Arial', 18)
    
    email_text = Label(janela, text="Endereço de E-mail")
    email_text.place(x=left_column,y=y_base+30)
    email_field = Entry(font=fonte)
    email_field.place(x=left_column,y=y_base+70)

    tel_text = Label(janela, text="Telefone")
    tel_text.place(x=left_column,y=y_base+110)
    tel_field = Entry(font=fonte)
    tel_field.place(x=left_column,y=y_base+150)

    cpf_text = Label(janela, text="CPF")
    cpf_text.place(x=left_column,y=y_base+190)
    cpf_field = Entry(font=fonte)
    cpf_field.place(x=left_column,y=y_base+230)

    endereco_text = Label(janela, text="Endereço")
    endereco_text.place(x=left_column,y=y_base+270)
    endereco_field = Entry(font=fonte)
    endereco_field.place(x=left_column,y=y_base+310)

    nome_text = Label(janela, text="Nome")
    nome_text.place(x=right_column,y=y_base+30)
    nome_field = Entry(font=fonte)
    nome_field.place(x=right_column,y=y_base+70)

    user_text = Label(janela, text="Nome de Usuario")
    user_text.place(x=right_column,y=y_base+110)
    user_field = Entry(font=fonte)
    user_field.place(x=right_column,y=y_base+150)

    senha_text = Label(janela, text="Senha")
    senha_text.place(x=right_column,y=y_base+190)
    senha_field = Entry(font=fonte)
    senha_field.place(x=right_column,y=y_base+230)

    cfmsenha_text = Label(janela, text="Confirme sua senha")
    cfmsenha_text.place(x=right_column,y=y_base+270)
    cfmsenha_field = Entry(font=fonte)
    cfmsenha_field.place(x=right_column,y=y_base+310)
    
    janela.mainloop()

    #teste = Button(janela, text='AQUI',command=)

def acessa_tela_correspondente():
    "Leva o usuário à tela de cliente ou funcionário (a depender do login e senha)"
    pass

def tela_consulta():
    global janela
    janela.destroy()
    janela = Tk() 
    label = Label(janela, text='Consulta')
    label.pack()
    janela.geometry("600x600+300+50")

    insira_login = Label(janela, text='Nome do cliente', font=('bold',10))
    insira_login.place(x=60,y=30)

    e_insira_login = Entry()
    e_insira_login.place(x=60, y=60, width=200, height=25)
    botao_consulta_nome = Button(janela, text='Consultar', height=1, width=10 ,command=acessa_tela_correspondente)
    botao_consulta_nome.place(x=260,y=60)

    insira_senha = Label(janela, text='ID do pedido', font=('bold',10))
    insira_senha.place(x=60,y=140)
    
    e_insira_senha = Entry()
    e_insira_senha.place(x=60, y=170, width=200, height=25)
    botao_consulta_id = Button(janela, text='Consultar', height= 1, width=10,command=tela_criar_cadastro)
    botao_consulta_id.place(x=260,y=170)




    janela.mainloop()


tela_login()