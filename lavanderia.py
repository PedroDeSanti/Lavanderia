from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from datetime import datetime
import pandas as pd

con = mysql.connect(host="localhost", user='degelo', password='Casasbahia-1', database='projetobd')

# IMPLEMENTADA
def tela_login(janela):
    font1 = ("Arial", 15)
    font2 = ("Arial", 18)
    xi = 100
    ybase = 50
    # global janela
    janela.destroy()
    janela = Tk()
    janela['background'] = "#d1ffed"
    janela.geometry("600x600+300+50")
    janela.title("Tela de Login")
    label = Label(janela, text='Tela de Login',font = font2, bg="#d1ffed")
    label.place(x = xi, y=ybase) 

    insira_login = Label(janela, text='Insira seu Login', font=font1, bg="#d1ffed")
    insira_login.place(x=xi,y=ybase+50)
    e_insira_login = Entry(font=font2)
    e_insira_login.place(x=xi, y=ybase+80)

    insira_senha = Label(janela, text='Insira sua Senha', font=font1, bg="#d1ffed")
    insira_senha.place(x=xi,y=ybase+130)
    e_insira_senha = Entry(font=font2)
    e_insira_senha.place(x=xi, y=ybase+160)

    botao_acessar = Button(janela, text='Acessar', font=font2, bg="#00b56e", fg="white", command=lambda:acessa_tela_correspondente(e_insira_login, e_insira_senha, janela))
    botao_acessar.place(x=xi,y=ybase+210)

    criar_cadastro = Label(janela, text='Não tem conta?', font=font1, bg="#d1ffed")
    criar_cadastro.place(x=xi,y=ybase+280)
    botao_criar_cadastro = Button(janela, text='Cadastrar', font=font1, fg="#00b56e", bg="white", command= lambda: tela_criar_cadastro(janela, 0))
    botao_criar_cadastro.place(x=xi,y=ybase+330)

    janela.mainloop()

# IMPLEMENTADA
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
                cursor.execute("select nome from Cliente where login='"+str(login.get())+"';")
                nome_usuario = cursor.fetchall()[0]
                tela_de_cliente(janela, str(nome_usuario[0]))
            else:
                tela_funcionario(janela)
        else:
            MessageBox.showinfo("Erro!", "Verifique sua senha!")

# IMPLEMENTADA
def tela_de_cliente(janela, nome_usuario):
    
    #global janela
    janela.destroy()
    janela = Tk()
    janela['background'] = "#d1ffed"
    janela.geometry("600x600+300+50")
    janela.title("Tela de Cliente")
    label = Label(janela, text='Tela de Cliente', bg="#d1ffed", font= ("Arial", 12))
    label.pack() 

    seus_pedidos = Button(janela, text='Seus pedidos', bg="#00b56e", fg="white", font= ("Arial", 18), command=lambda: tela_lista_pedidos_cliente(janela, nome_usuario, 0))
    seus_pedidos.place(x=250,y=150)
    # fazer_pedido_cliente = Button(janela, text='Fazer pedido',command=lambda: tela_de_fazer_pedido_cliente)
    # fazer_pedido_cliente.place(x=250,y=300)
    voltar = Button(janela, text='Voltar', bg="white", font= ("Arial", 18), fg="#00b56e", command=lambda: tela_login(janela))
    voltar.place(x=250,y=500)

    janela.mainloop()

# IMPLEMENTADA
def tela_funcionario(janela):
    x_column = 120
    y_base = 100
    # global janela
    janela.destroy()
    janela = Tk()
    janela['background'] = "#d1ffed"
    label = Label(janela, text='Escolha uma opcao', bg = "#d1ffed")
    label.place(x = x_column, y = int(y_base/2))
    janela.geometry("600x600+300+50")
    
    y_line = [y_base, y_base*2, y_base*3, y_base*4]
    fonte=('Arial', 18)
    
    botao_cadastrar_cliente = Button(janela, text='Cadastrar Cliente', bg="#00b56e", fg="white", font = fonte, command=lambda:tela_criar_cadastro(janela, 1))
    botao_cadastrar_cliente.place(x=x_column,y=y_line[0])
    
    botao_criar_pedido = Button(janela, text='Criar Pedido', bg="#00b56e", fg="white", font = fonte, command=lambda:tela_fazer_pedido(janela))
    botao_criar_pedido.place(x=x_column,y=y_line[1])

    botao_consultar_pedido = Button(janela, text='Consultar Pedido', bg="#00b56e", fg="white", font = fonte, command=lambda:tela_consulta(janela))
    botao_consultar_pedido.place(x=x_column,y=y_line[2])

    botao_atualizar_pedido = Button(janela, text='Atualizar Pedido', bg="#00b56e", fg="white", font = fonte, command=lambda:tela_atualiza(janela))
    botao_atualizar_pedido.place(x=x_column,y=y_line[3])
    
    voltar = Button(janela, text='Voltar', bg="white", fg="#00b56e", command=lambda: tela_login(janela))
    voltar.place(x=x_column,y=500)

    janela.mainloop()

# IMPLEMENTADA
def tela_criar_cadastro(janela, valor):
    left_column = 20
    right_column = 320
    y_base = 120
    fonte=('Arial', 18)
    fonte2=('Arial', 15)

    # global janela
    janela.destroy()
    janela = Tk()
    janela['background'] = "#d1ffed"
    label = Label(janela, text='Insira seus Dados', bg="#d1ffed", font= fonte2)
    label.place(x = left_column, y = 50)
    janela.geometry("600x600+300+50")
    
    
    email_text = Label(janela, text="Endereço de E-mail", bg="#d1ffed", font= fonte2)
    email_text.place(x=left_column,y=y_base+30)
    email_field = Entry(janela, font=fonte)
    email_field.place(x=left_column,y=y_base+70)

    tel_text = Label(janela, text="Telefone", bg="#d1ffed", font= fonte2)
    tel_text.place(x=left_column,y=y_base+110)
    tel_field = Entry(janela, font=fonte)
    tel_field.place(x=left_column,y=y_base+150)

    cpf_text = Label(janela, text="CPF", bg="#d1ffed", font= fonte2)
    cpf_text.place(x=left_column,y=y_base+190)
    cpf_field = Entry(janela, font=fonte)
    cpf_field.place(x=left_column,y=y_base+230)

    endereco_text = Label(janela, text="Endereço", bg="#d1ffed", font= fonte2)
    endereco_text.place(x=left_column,y=y_base+270)
    endereco_field = Entry(janela, font=fonte)
    endereco_field.place(x=left_column,y=y_base+310)

    nome_text = Label(janela, text="Nome", bg="#d1ffed", font= fonte2)
    nome_text.place(x=right_column,y=y_base+30)
    nome_field = Entry(janela, font=fonte)
    nome_field.place(x=right_column,y=y_base+70)

    user_text = Label(janela, text="Nome de Usuario", bg="#d1ffed", font= fonte2)
    user_text.place(x=right_column,y=y_base+110)
    user_field = Entry(janela, font=fonte)
    user_field.place(x=right_column,y=y_base+150)

    senha_text = Label(janela, text="Senha", bg="#d1ffed", font= fonte2)
    senha_text.place(x=right_column,y=y_base+190)
    senha_field = Entry(janela, font=fonte)
    senha_field.place(x=right_column,y=y_base+230)

    cfmsenha_text = Label(janela, text="Confirme sua senha", bg="#d1ffed", font= fonte2)
    cfmsenha_text.place(x=right_column,y=y_base+270)
    cfmsenha_field = Entry(janela, font=fonte)
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

    seus_pedidos = Button(janela, text='Criar!', font=("Arial", 16), bg="#00b56e", fg="white", command=lambda:verifica_dados_cadastrais(janela ,dic_dados, valor))
    seus_pedidos.place(x=right_column,y=500)
    if valor == 0:
        voltar = Button(janela, text='Voltar', font=("Arial", 16), fg="#00b56e", bg="white", command=lambda: tela_login(janela))
        voltar.place(x=left_column,y=500)
    else:
        voltar = Button(janela, text='Voltar', font=("Arial", 16), fg="#00b56e", bg="white", command=lambda: tela_funcionario(janela))
        voltar.place(x=left_column,y=500)


    janela.mainloop()

# IMPLEMENTADA
def verifica_dados_cadastrais(janela, dic_dados, valor):
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
        if valor == 1:
            tela_funcionario(janela)
        else:
            tela_login(janela)

# IMPLEMENTADA
def tela_consulta(janela):
    fonte = ("Arial", 15)
    # global janela
    janela.destroy()
    janela = Tk()
    janela['background'] = "#d1ffed"
    label = Label(janela, text='Consulta', font = fonte, bg="#d1ffed")
    label.pack()
    janela.geometry("600x600+300+50")

    insira_login = Label(janela, text='Nome do cliente', font=fonte, bg="#d1ffed")
    insira_login.place(x=60,y=30)

    e_insira_login = Entry(font = ("Arial", 12))
    e_insira_login.place(x=60, y=60, width=200, height=25)
    botao_consulta_nome = Button(janela, text='Consultar', height=1, width=10, fg="white", bg="#00b56e", command=lambda:tela_lista_pedidos_cliente(janela, e_insira_login.get(), 1))
    botao_consulta_nome.place(x=260,y=60)

    insira_senha = Label(janela, text='ID do pedido', font=fonte, bg="#d1ffed") # "#font = ("Arial", 20)"
    insira_senha.place(x=60,y=140)
    
    e_insira_senha = Entry(font = ("Arial", 12))
    e_insira_senha.place(x=60, y=170, width=200, height=25)
    botao_consulta_id = Button(janela, text='Consultar', height= 1, width=10, fg="white", bg="#00b56e",command=lambda:tela_lista_pedido_id(janela, e_insira_senha.get(), 1))
    botao_consulta_id.place(x=260,y=170)
    
    voltar = Button(janela, text='Voltar', font = fonte, bg="white", fg="#00b56e", command=lambda: tela_funcionario(janela))
    voltar.place(x=250,y=500)

    janela.mainloop()

# IMPLEMENTADA
def tela_lista_pedidos_cliente(janela, nome_usuario, valor_acesso):
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
    janela['background'] = "#d1ffed"
    label = Label(janela, text='Pedidos do cliente', bg="#d1ffed")
    label.pack()
    janela.geometry("600x600+300+50")

    main_frame = Frame(janela)
    main_frame['background'] = "#d1ffed"
    main_frame.pack(fill = BOTH, expand = 1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill =BOTH, expand = 1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill = Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set, bg="#d1ffed")
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    my_canvas['background'] = "#d1ffed"

    second_frame = Frame(my_canvas)
    second_frame['background'] = "#d1ffed"

    my_canvas.create_window((0,0), window = second_frame, anchor = "nw")
    frame =  Frame(second_frame)
    frame['background'] = "#d1ffed"
    
    e0 = Label(frame, text = "ID_Pedido", font=('bold',10), width = "14", bg="#d1ffed")
    e0.pack(side=LEFT)
    e0['background'] = "#d1ffed"
    e1 = Label(frame, text = "CPF", font=('bold',10), width = "14", bg="#d1ffed")
    e1.pack(side=LEFT)
    e1['background'] = "#d1ffed"
    e2 = Label(frame, text = "Data", font=('bold',10), width = "14", bg="#d1ffed")
    e2.pack(side=LEFT)
    e2['background'] = "#d1ffed"
    e3 = Label(frame, text = "Estado", font=('bold',10), width = "14", bg="#d1ffed")
    e3.pack(side=LEFT)
    e3['background'] = "#d1ffed"
    e4 = Label(frame, text = "", font=('bold',10), width = "14", bg="#d1ffed")
    e4.pack(side=LEFT)
    e4['background'] = "#d1ffed"
    frame.pack()

    # botao_consulta = []
    # i = 0
    for pedido in lista_pedidos:
        frame =  Frame(second_frame)
        frame['background'] = "#d1ffed"
        e0 = Label(frame, text = str(pedido[0]), font=('bold',10), width = "14", bg="#d1ffed")
        e0.pack(side=LEFT)
        e1 = Label(frame, text = str(pedido[1]), font=('bold',10), width = "14", bg="#d1ffed")
        e1.pack(side=LEFT)
        e2 = Label(frame, text = str(pedido[2]), font=('bold',10), width = "14", bg="#d1ffed")
        e2.pack(side=LEFT)
        e3 = Label(frame, text = str(pedido[3]), font=('bold',10), width = "14", bg="#d1ffed")
        e3.pack(side=LEFT)
        botao_consulta = Button(frame, text='Consultar', font=('bold',10), bg="#00b56e", fg="white", command=lambda x=pedido[0]:tela_lista_pedido_id(janela, x, valor_acesso))
        # botao_consulta.append(botao)
        botao_consulta.pack(side=LEFT)
        # botao_consulta = Button(frame, text='Consultar', font=('bold',10), command=lambda:tela_lista_pedido_id(janela, pedido[0]))
        # botao_consulta.pack(side=LEFT)
        frame.pack()
        
        # i += 1
    if valor_acesso == 1:
        voltar = Button(janela, text='Voltar', fg="#00b56e", bg="white",font = ("Arial", 18),command=lambda: tela_funcionario(janela))
        voltar.place(x=250,y=500)
    else:
        voltar = Button(janela, text='Voltar', fg="#00b56e", bg="white",font = ("Arial", 18),command=lambda: tela_de_cliente(janela, nome_usuario))
        voltar.place(x=250,y=500)
        
    janela.mainloop()

# IMPLEMENTADA
def tela_lista_pedido_id(janela, pedido_id, valor_acesso):
    print(pedido_id)

    janela.destroy()
    janela = Tk()
    janela['background'] = "#d1ffed"
    janela.geometry("600x600+300+50")
    label = Label(janela, text="Informações do pedido "+str(pedido_id), bg="#d1ffed")
    label.place(x = 200, y = 50)

    cursor = con.cursor()
    cursor.execute("select * from Pedido where ID_pedido="+str(pedido_id)+";")
    pedido_infs = cursor.fetchall()[0]
    
    CPF = pedido_infs[1]

    cursor = con.cursor()
    cursor.execute("select nome from Cliente where CPF="+str(CPF)+";")
    nome_cliente = cursor.fetchall()[0][0]
    print("nome_cliente = ", nome_cliente)
                    
    cursor.execute("select ID_item from item where ID_pedido="+str(pedido_id)+";")

    itens = cursor.fetchall()

    xi = 150
    yi = 100

    base = ["Cliente", "Data do Pedido", "Data para Entrega", "Estado", "Itens"]
    if valor_acesso == 2 or valor_acesso == 1:
        voltar = Button(janela, text='Voltar', fg="#00b56e", bg="white",font = ("Arial", 18),command=lambda: tela_consulta(janela))
        voltar.place(x=250,y=500)
    else:
        voltar = Button(janela, text='Voltar', fg="#00b56e", bg="white",font = ("Arial", 18),command=lambda: tela_login(janela))
        voltar.place(x=250,y=500)

    i = 0

    aux_b = str(base[i])
    aux_d = str(pedido_infs[i+1])
    auxlb = Label (janela, text = "Cliente", font=("bold", 13), bg="#d1ffed")
    auxld = Label (janela, text = nome_cliente, font=("Arial", 13),  bg="#d1ffed")
    auxlb.place(x = xi, y = yi)       
    auxld.place(x = xi + 150, y = yi)
    yi += 30   

    auxlb = Label (janela, text = "Data do Pedido", font=("bold", 13), bg="#d1ffed")
    auxld = Label (janela, text = pedido_infs[2], font=("Arial", 13), bg="#d1ffed")
    auxlb.place(x = xi, y = yi)       
    auxld.place(x = xi + 150, y = yi)
    yi += 30  

    lavagens = []
    for item in itens:
        cursor.execute("select ID_tipoLavagem from item where ID_pedido="+str(pedido_id)+" and ID_item="+str(item[0])+";")
        lavagem = cursor.fetchall()
        lavagens.append(lavagem[0][0])
 
    tempos = []
    for lava in lavagens:
        cursor.execute("select tempo from TipoLavagem where ID_TipoLavagem="+str(lava)+";")
        tempo = cursor.fetchall()
        tempos.append(tempo[0])

    maior_tempo = max(tempos)
    
    data = pedido_infs[2]
    
    data_final = data + pd.DateOffset(days = maior_tempo[0])
    print(data_final)
    str_data_final = data_final.strftime("%Y-%m-%d")
    # 2022-03-17
  
    auxlb = Label (janela, text = "Data para Entrega", font=("bold", 13), bg="#d1ffed")
    auxld = Label (janela, text = str_data_final, font=("Arial", 13), bg="#d1ffed")
    auxlb.place(x = xi, y = yi)       
    auxld.place(x = xi + 150, y = yi)
    yi += 30  

    auxlb = Label (janela, text = "Estado", font=("bold", 13), bg="#d1ffed")
    auxld = Label (janela, text = pedido_infs[3], font=("Arial", 13), bg="#d1ffed")
    auxlb.place(x = xi, y = yi)       
    auxld.place(x = xi + 150, y = yi)
    yi += 30  

    auxlb = Label (janela, text = "Itens:", font=("bold", 13), bg="#d1ffed")
    auxlb.place(x = xi, y = yi)     

    for item in itens:
        peca = item[0]
        cursor.execute("select peca_nome from roupas where ID_item="+str(peca)+";")
        roupa = cursor.fetchall()[0][0]
        auxld = Label (janela, text = roupa, font=("Arial", 13), bg="#d1ffed")
        auxld.place(x = xi + 150, y = yi)
        yi += 30 
    
    janela.mainloop()

# IMPLEMENTADA
def tela_fazer_pedido(janela):
    # global janela
    janela.destroy()
    janela = Tk()
    janela['background'] = "#d1ffed"
    janela['background'] = "#d1ffed"
    janela.geometry("600x600+300+50")
    fonte=('Arial', 18)
    xi = 200

    cpf_text = Label(janela, text="CPF", font = ("Arial", 16), background="#d1ffed")
    cpf_text.place(x=xi,y=100)
    cpf_field = Entry(font=fonte)
    cpf_field.place(x=xi,y=150)
    
    peca_opt = ["Camiseta", "Camisa", "Calca", "Bermuda", "Shorts", "Cueca", "Calcinha", "Meia", "Moletom", "Luvas", "Gorro"]
    peca = ttk.Combobox(janela, values = peca_opt, state='readonly', font = fonte)
    peca.set("Selecione o Item")
    peca.place(x = xi, y = 200)

    lavagem_opt = ["lavagem normal","lavagem a seco", "lavagem sem lavar", "hidratacao", "so no paninho"]
    lavagem = ttk.Combobox(janela, values = lavagem_opt, state='readonly', font = fonte)
    lavagem.set("Selecione a Lavagem")
    lavagem.place(x = xi, y = 250)
    
    matriz_itens = []
    botao_adiconar_id = Button(janela, text='Adicionar Item', height= 1, font = fonte, bg="#00b56e", fg="white", command=lambda :adiciona_item(peca, lavagem, matriz_itens))
    botao_adiconar_id.place(x=xi,y=300)
    
    botao_fazer_pedido = Button(janela, text='Criar Pedido', height= 1, font = fonte, bg="#00b56e", fg="white", command=lambda:cria_pedido(cpf_field, matriz_itens))
    botao_fazer_pedido.place(x=xi, y=400)

    voltar = Button(janela, text='Voltar', font = fonte, bg="#b53600", fg="white", command=lambda: tela_funcionario(janela))
    voltar.place(x=xi-100,y=400)
    
    janela.mainloop()

# IMPLEMENTADA
def adiciona_item(peca, lavagem, matriz):
    # Captura campos
    nome_item = peca.get()
    print(nome_item, peca.current())
    nome_lavagem = lavagem.get()
    print(nome_lavagem, lavagem.current())
    
    # Acesso ao banco
    cursor = con.cursor()
    cursor.execute("Select id_item from roupas where peca_nome='"+str(nome_item)+"';")
    id_item = cursor.fetchall()[0][0]
    print(id_item)

    cursor = con.cursor()
    cursor.execute("Select id_tipolavagem from TipoLavagem where nome='"+str(nome_lavagem)+"';")
    id_lavagem = cursor.fetchall()[0][0]
    print(id_lavagem)
    
    matriz.append([id_item, id_lavagem, "em processo"])
    print(matriz)
    MessageBox.showinfo("Alerta!", "Item Adicionado com Sucesso!") 

# IMPLEMENTADA
def cria_pedido(cpf, matriz_itens):
    # verifica se o cpf esta no bd
    cursor = con.cursor()
    verifica_cpf = "select exists(select * from cliente where cpf = '"+str(cpf.get())+"');"
    # gera pedido id (for i in range(1000): if i nao esta no bd, esse é o id)
    cursor.execute(verifica_cpf)
    if_cliente = cursor.fetchall()[0][0]
    if if_cliente:
        for id in range(1000):
            verifica_idpedido = "select exists(select * from pedido where id_pedido = "+str(id)+");"
            cursor.execute(verifica_idpedido)
            if_idpedido = cursor.fetchall()[0][0]
            if not if_idpedido:
                break
        print("o id escolhido foi",id)

        cursor = con.cursor()
        
        cria_pedido = "insert into pedido values("+str(id)+","+str(cpf.get())+", '2022-04-14', 'em processo');"

        cursor.execute(cria_pedido)
        cursor.execute("commit")

        for i in range(len(matriz_itens)):
            cursor = con.cursor()
            cursor.execute("insert into item values("+str(matriz_itens[i][0])+", "+str(id)+","+str(matriz_itens[i][1])+",'"+matriz_itens[i][2]+"');")
            cursor.execute("commit")
            MessageBox.showinfo("Alerta!", "Pedido Criado com Sucesso!")        
    else:
        MessageBox.showinfo("Erros!", "CPF inválido!")
    
# IMPLEMENTADA
def tela_atualiza(janela):
    # global janela
    janela.destroy()
    janela = Tk()
    janela['background'] = "#d1ffed"
    label = Label(janela, text='Atualizar Dados do Cliente', bg="#d1ffed", font=("Arial", 16))
    label.pack()
    janela.geometry("600x600+300+50")

    insira_login = Label(janela, text='Nome do cliente', font=('bold',10), bg="#d1ffed")
    insira_login.place(x=60,y=30)

    e_insira_login = Entry()
    e_insira_login.place(x=60, y=60, width=200, height=25)
    botao_consulta_nome = Button(janela, text='Consultar', bg="#00b56e", fg="white", height=1, width=10 ,command=lambda:tela_lista_pedidos_cliente_atualiza(janela, e_insira_login.get()))
    botao_consulta_nome.place(x=260,y=60)

    insira_senha = Label(janela, text='ID do pedido', font=('bold',10), bg="#d1ffed")
    insira_senha.place(x=60,y=140)
    
    e_insira_senha = Entry()
    e_insira_senha.place(x=60, y=170, width=200, height=25)
    botao_consulta_id = Button(janela, text='Consultar', height= 1, width=10, bg="#00b56e", fg="white",command=lambda:tela_lista_pedido_id_atualiza(janela, e_insira_senha.get()))
    botao_consulta_id.place(x=260,y=170)

    voltar = Button(janela, text='Voltar', fg="#00b56e", bg="white",command=lambda: tela_funcionario(janela))
    voltar.place(x=250,y=500)

    janela.mainloop()

# IMPLEMENTADA
def tela_lista_pedidos_cliente_atualiza(janela, nome_usuario):
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
    janela['background'] = "#d1ffed"
    label = Label(janela, text='Atualizar Pedidos do cliente', bg="#d1ffed")
    label.pack()
    janela.geometry("600x600+300+50")

    main_frame = Frame(janela)
    main_frame.pack(fill = BOTH, expand = 1)
    main_frame['background'] = "#d1ffed"

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill =BOTH, expand = 1)
    my_canvas['background'] = "#d1ffed"

    my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_canvas.yview)
    my_scrollbar.pack(side=LEFT, fill = Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)
    second_frame['background'] = "#d1ffed"

    my_canvas.create_window((0,0), window = second_frame, anchor = "nw")
    frame =  Frame(second_frame)
    frame['background'] = "#d1ffed"
    e0 = Label(frame, text = "ID_Pedido", font=('bold',10), width = "13")
    e0['background'] = "#d1ffed"
    e0.pack(side=LEFT)
    e1 = Label(frame, text = "CPF", font=('bold',10), width = "13")
    e1.pack(side=LEFT)
    e1['background'] = "#d1ffed"
    e2 = Label(frame, text = "Data", font=('bold',10), width = "13")
    e2.pack(side=LEFT)
    e2['background'] = "#d1ffed"
    e3 = Label(frame, text = "Estado", font=('bold',10), width = "13")
    e3.pack(side=LEFT)
    e3['background'] = "#d1ffed"
    e4 = Label(frame, text = "", font=('bold',10), width = "13")
    e4.pack(side=LEFT)
    e4['background'] = "#d1ffed"
    frame.pack()
    frame['background'] = "#d1ffed"


    for pedido in lista_pedidos:
        frame =  Frame(second_frame)
        frame['background'] = "#d1ffed"
        e0 = Label(frame, text = str(pedido[0]), font=('bold',10), width = "13")
        e0.pack(side=LEFT)
        e0['background'] = "#d1ffed"
        e1 = Label(frame, text = str(pedido[1]), font=('bold',10), width = "13")
        e1.pack(side=LEFT)
        e1['background'] = "#d1ffed"
        e2 = Label(frame, text = str(pedido[2]), font=('bold',10), width = "13")
        e2.pack(side=LEFT)
        e2['background'] = "#d1ffed"
        e3 = Label(frame, text = str(pedido[3]), font=('bold',10), width = "13")
        e3.pack(side=LEFT)
        e3['background'] = "#d1ffed"
        botao_consulta = Button(frame, text='Atualizar', bg="#00b56e", fg="white", font=('bold',10), command=lambda x=pedido[0]:tela_lista_pedido_id_atualiza(janela, x))
        botao_consulta.pack(side=LEFT)
        
        frame.pack()
        frame['background'] = "#d1ffed"
    voltar = Button(janela, text='Voltar', fg="#00b56e", bg="white", font = ("Arial", 18) ,command=lambda: tela_atualiza(janela))
    voltar.place(x=250,y=500)
                
    janela.mainloop()

# IMPLEMENTADA
def tela_lista_pedido_id_atualiza(janela, pedido_id):
    janela.destroy()
    janela = Tk()
    janela['background'] = "#d1ffed"
    janela.geometry("600x600+300+50")
    label = Label(janela, text="Atualização de Informações do Pedido "+str(pedido_id), font = ("Arial", 20))
    label["background"] = "#d1ffed"
    label.place(x = 25, y = 50)
    
    cursor = con.cursor()
    cursor.execute("select * from Pedido where ID_pedido="+str(pedido_id)+";")
    pedido_infs = cursor.fetchall()[0]
    
    lavagem_opt = ["lavando","secando", "pronto", "concluido"]
    lavagem = ttk.Combobox(janela, values = lavagem_opt, font = ("Arial", 15))
    lavagem.set("Selecione o estado")
    lavagem.place(x = 150, y = 350)
    fonte=('Arial', 18)

    botao_adiconar_id = Button(janela, text='Atualizar o estado', bg = "#00b56e", height= 1, font = fonte, command=lambda:atualiza_estado_pedido(pedido_infs, lavagem.get()))
    botao_adiconar_id.place(x=150,y=400)
    
    voltar = Button(janela, text='Voltar',command=lambda: tela_atualiza(janela))
    voltar.place(x=250,y=500)
    
    janela.mainloop()


def atualiza_estado_pedido(pedido_inf, novo_estado):
    
    print("ID_pedido"+str(pedido_inf[0]))
    print("novo_estado"+novo_estado)

    cursor = con.cursor()
    cursor.execute("UPDATE Pedido SET estado = "+"\""+ novo_estado+"\""+" WHERE ID_pedido="+str(pedido_inf[0])+";")
    cursor.execute("commit")

    MessageBox.showinfo("Alerta!", "Item Atualizado com Sucesso!") 
    return 

def fechar_janela(janela):
    janela.destroy()


janela = Tk()
janela['background'] = "#d1ffed"
tela_login(janela)