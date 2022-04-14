create table Administra (
	ID_Pedido int(5),
	CPF int(11),
	primary key (ID_Pedido, CPF));
	 
create table Cliente (
	CPF int(11) primary key,
	nome varchar(30),
	endereco varchar(40),
	telefone int(11),
	email varchar(30),
	login varchar(20),
	senha varchar(20));
	  
create table Funcionario (
	CPF int(11) primary key,
	nome varchar(30),
	endereco varchar(40),
	telefone int(11),
	email varchar(30),
	login varchar(20),
	senha varchar(20),
	cargo varchar(15));

create table item (
	ID_item int(3),
	ID_pedido int(5),
	ID_tipoLavagem int(3),
	estado varchar(15),
	primary key (ID_item, Id_pedido));

create table pedido (
	ID_pedido int(5),
	CPF int(11),
	dataPedido date,
	estado varchar(15),
	primary key (ID_pedido, CPF));

create table TipoLavagem (
	ID_TipoLavagem int(3) primary key,
	nome varchar(20),
	preco decimal(6,2),
	tempo int(2));
	 