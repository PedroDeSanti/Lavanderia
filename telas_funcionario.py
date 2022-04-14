from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

from telas_cliente import *

con = mysql.connect(host="localhost", user='root', password='MySQLP@55W0rd', database='projetobd')

# janela = Tk()

def tela_funcionario(janela):
    # global janela
    janela.destroy()
    janela = Tk() 
    label = Label(janela, text='Insira seus Dados')
    label.pack()
    janela.geometry("600x600+300+50")
    
    x_column = 120
    y_base = 100
    y_line = [y_base, y_base*2, y_base*3, y_base*4]
    fonte=('Arial', 18)
    
    botao_cadastrar_cliente = Button(janela, text='Cadastrar Cliente', font = fonte, command=lambda:tela_criar_cadastro(janela))
    botao_cadastrar_cliente.place(x=x_column,y=y_line[0])
    
    botao_criar_pedido = Button(janela, text='Criar Pedido', font = fonte, command=lambda:tela_fazer_pedido(janela))
    botao_criar_pedido.place(x=x_column,y=y_line[1])

    botao_consultar_pedido = Button(janela, text='Consultar Pedido', font = fonte, command=lambda:tela_consulta(janela))
    botao_consultar_pedido.place(x=x_column,y=y_line[2])

    botao_atualizar_pedido = Button(janela, text='Atualizar Pedido', font = fonte, command=lambda:tela_consulta(janela))
    botao_atualizar_pedido.place(x=x_column,y=y_line[3])

    janela.mainloop()

    
def tela_criar_cadastro(janela):
    # global janela
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
    
    dic_dados = {}
    dic_dados["email"] = email_field
    dic_dados["tel"] = tel_field
    dic_dados["cpf"] = cpf_field
    dic_dados["endereco"] = endereco_field
    dic_dados["nome"] = nome_field
    dic_dados["user"] = user_field
    dic_dados["senha"] = senha_field
    dic_dados["cfmsenha"] = cfmsenha_field

    seus_pedidos = Button(janela, text='Criar!',command=lambda:verifica_dados_cadastrais(dic_dados))
    seus_pedidos.place(x=275,y=500)


    janela.mainloop()

# NÃO NECESSITA MAIS DE ALTERAÇÃO
def verifica_dados_cadastrais(dic_dados):
    # for i in dic_dados:
    #     print(dic_dados[i].get())
    mensagem = ""
    
    email = str(dic_dados["email"].get())
    tel = str(dic_dados["tel"].get())
    cpf =str(dic_dados["cpf"].get())
    endereco = str(dic_dados["endereco"].get())
    nome = str(dic_dados["nome"].get())
    user = str(dic_dados["user"].get())
    senha = str(dic_dados["senha"].get())
    cfmsenha = str(dic_dados["cfmsenha"].get())

    # verifica o email
    if (len(email.split("@")) != 2) or email == "":
        mensagem += "Verifique seu email!\n"
    # verifica o telefone
    if (len(tel) > 11) or (not tel.isdecimal()) or tel == "":
        mensagem += "Verifique seu telefone!\n"
    # verifica o cpf
    if (len(cpf) > 11) or (not cpf.isdecimal()) or cpf == "":
        mensagem += "Verifique seu CPF!\n"
    # verifica o endereco
    if len(endereco) > 30 or endereco == "":
        mensagem += "Verifique seu endereço!\n"
    # verifica o nome
    if not all((chr.isalpha() or chr.isspace()) for chr in nome) or nome == "":
        mensagem += "Verifique seu nome!\n"
    # verifica o user
    if len(user) > 20 or user == "":
        mensagem += "Verifique seu usuário!\n"
    # verifica o senha
    if len(senha) > 20 or senha == "":
        mensagem += "Verifique sua senha!\n"
    # verifica o senha
    if senha != cfmsenha:
        mensagem += "Senhas não batem!\n"
    # se há problema, mostra um popup
    if mensagem != "":
        MessageBox.showinfo("Erros!", mensagem)
    else:
    # Insere no banco de dados
        cursor = con.cursor()
        cursor.execute("insert into cliente values("+cpf+",'"+nome+"','"+endereco+"',"+tel+",'"+email+"','"+user+"','"+senha+"');")
        cursor.execute("commit")
        MessageBox.showinfo("Criação de Usuário Realizada!", "Usuário "+user+" foi criado com sucesso!")


def tela_consulta(janela):
    # global janela
    janela.destroy()
    janela = Tk() 
    label = Label(janela, text='Consulta')
    label.pack()
    janela.geometry("600x600+300+50")

    insira_login = Label(janela, text='Nome do cliente', font=('bold',10))
    insira_login.place(x=60,y=30)

    e_insira_login = Entry()
    e_insira_login.place(x=60, y=60, width=200, height=25)
    botao_consulta_nome = Button(janela, text='Consultar', height=1, width=10 ,command=lambda:tela_lista_pedidos_cliente(janela, e_insira_login))
    botao_consulta_nome.place(x=260,y=60)

    insira_senha = Label(janela, text='ID do pedido', font=('bold',10))
    insira_senha.place(x=60,y=140)
    
    e_insira_senha = Entry()
    e_insira_senha.place(x=60, y=170, width=200, height=25)
    botao_consulta_id = Button(janela, text='Consultar', height= 1, width=10,command=lambda:acessa_tela_correspondente(janela))
    botao_consulta_id.place(x=260,y=170)

    janela.mainloop()


def tela_lista_pedidos_cliente(janela, nome_usuario):
    lista_pedidos = []
    nome_usuario = "\""+nome_usuario+"\""
    cursor = con.cursor()
    cursor.execute("select CPF from Cliente where nome="+nome_usuario+";")
    CPF = cursor.fetchall()[0][0]
    # print(CPF)
    cursor.execute("select * from pedido where CPF="+str(CPF))
    rows = cursor.fetchall()
    # print(rows)
    
    for row in rows:
        lista_pedidos.append(row)

    janela.destroy()
    janela = Tk() 
    label = Label(janela, text='Pedidos do cliente')
    label.pack()
    janela.geometry("600x600+300+50")

    main_frame = Frame(janela)
    main_frame.pack(fill = BOTH, expand = 1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill =BOTH, expand = 1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill = Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window = second_frame, anchor = "nw")
    frame =  Frame(second_frame)
    e0 = Label(frame, text = "ID_Pedido", font=('bold',12), width = "10")
    e0.pack(side=LEFT)
    e1 = Label(frame, text = "CPF", font=('bold',12), width = "10")
    e1.pack(side=LEFT)
    e2 = Label(frame, text = "Data", font=('bold',12), width = "10")
    e2.pack(side=LEFT)
    e3 = Label(frame, text = "Estado", font=('bold',12), width = "10")
    e3.pack(side=LEFT)
    frame.pack()

    for pedido in lista_pedidos:
        frame =  Frame(second_frame)
        e0 = Label(frame, text = str(pedido[0]), font=('bold',10), width = "10")
        e0.pack(side=LEFT)
        e1 = Label(frame, text = str(pedido[1]), font=('bold',10), width = "10")
        e1.pack(side=LEFT)
        e2 = Label(frame, text = str(pedido[2]), font=('bold',10), width = "10")
        e2.pack(side=LEFT)
        e3 = Label(frame, text = str(pedido[3]), font=('bold',10), width = "10")
        e3.pack(side=LEFT)
        botao_consulta = Button(frame, text='Consultar', font=('bold',10), command=lambda:tela_lista_pedido_id(janela, pedido))
        botao_consulta.pack(side=LEFT)
        frame.pack()
        i += 1
        
    janela.mainloop()


def tela_lista_pedido_id(janela, pedido_infs):
    janela.destroy()
    janela = Tk() 
    janela.geometry("600x600+300+50")
    label = Label(janela, text="Informações do pedido "+str(pedido_infs[0]))
    label.place(x = 200, y = 50)

    CPF = pedido_infs[1]

    cursor = con.cursor()
    cursor.execute("select nome from Cliente where CPF="+str(CPF)+";")
    nome_cliente = cursor.fetchall()[0][0]
    print("nome_cliente = ", nome_cliente)
                    
    # cursor.execute("select ID_item from item where ID_pedido="+str(pedido_infs[0])+";")
    print(pedido_infs[0])
    cursor.execute("select ID_item from item where ID_pedido=10485;")
    itens = cursor.fetchall()
    print("itens = ",itens)

    xi = 150
    yi = 100

    base = ["Cliente", "Data do Pedido", "Data para Entrega", "Estado", "Itens"]
    
    # i = 0

    # aux_b = str(base[i])
    # aux_d = str(pedido_infs[i+1])
    # auxlb = Label (janela, text = aux_b, font=("bold", 13))
    # auxld = Label (janela, text = aux_d, font=("Arial", 13))
    # auxlb.place(x = xi, y = yi)       
    # auxld.place(x = xi + 150, y = yi)
    # yi += 30   

    i = 0

    aux_b = str(base[i])
    aux_d = str(pedido_infs[i+1])
    auxlb = Label (janela, text = "Cliente", font=("bold", 13))
    auxld = Label (janela, text = nome_cliente, font=("Arial", 13))
    auxlb.place(x = xi, y = yi)       
    auxld.place(x = xi + 150, y = yi)
    yi += 30   

    auxlb = Label (janela, text = "Data do Pedido", font=("bold", 13))
    auxld = Label (janela, text = pedido_infs[2], font=("Arial", 13))
    auxlb.place(x = xi, y = yi)       
    auxld.place(x = xi + 150, y = yi)
    yi += 30  

    # cursor.execute("select ID_item from item where ID_pedido="+str(pedido_infs[0]))
    # itens = cursor.fetchall()
    auxlb = Label (janela, text = "Data para Entrega", font=("bold", 13))
    auxld = Label (janela, text = nome_cliente, font=("Arial", 13))
    auxlb.place(x = xi, y = yi)       
    auxld.place(x = xi + 150, y = yi)
    yi += 30  

    auxlb = Label (janela, text = "Estado", font=("bold", 13))
    auxld = Label (janela, text = pedido_infs[3], font=("Arial", 13))
    auxlb.place(x = xi, y = yi)       
    auxld.place(x = xi + 150, y = yi)
    yi += 30  

    auxlb = Label (janela, text = "Itens:", font=("bold", 13))
    auxlb.place(x = xi, y = yi)     

    for item in itens:
        auxld = Label (janela, text = item, font=("Arial", 13))
        auxld.place(x = xi + 150, y = yi)
        yi += 30  


    # for i in range(len(pedido_infs)): 
    #     aux_b = str(base[i])
    #     aux_d = str(pedido_infs[i+1])
    #     auxlb = Label (janela, text = aux_b, font=("bold", 13))
    #     auxld = Label (janela, text = aux_d, font=("Arial", 13))
    #     auxlb.place(x = xi, y = yi)       
    #     auxld.place(x = xi + 150, y = yi)
    #     yi += 30   
    janela.mainloop()


def tela_fazer_pedido(janela):
    # global janela
    janela.destroy()
    janela = Tk() 
    label = Label(janela, text='Insira seus Dados')
    label.pack()
    janela.geometry("600x600+300+50")
    
    lavagem_opt = ["à seco", "à molhado", "com vanish"]
    lavagem = ttk.Combobox(janela, values = lavagem_opt)
    lavagem.set("Selecione a Lavagem")
    lavagem.place(x = 250, y = 300)
    fonte=('Arial', 18)
    
    peca_opt = ["camiseta", "cueca", "calca","tapete"]
    peca = ttk.Combobox(janela, values = peca_opt)
    peca.set("Selecione a Lavagem")
    peca.place(x = 250, y = 350)


    botao_adiconar_id = Button(janela, text='Adicionar Item', height= 1, font = fonte, command=lambda:acessa_tela_correspondente(janela))
    botao_adiconar_id.place(x=250,y=400)
    
    botao_fazer_pedido = Button(janela, text='Fazer Pedido', height= 1, font = fonte, command=lambda:acessa_tela_correspondente(janela))
    botao_fazer_pedido.place(x=250,y=450)
    
    janela.mainloop()



def acessa_tela_correspondente(janela):
    pass