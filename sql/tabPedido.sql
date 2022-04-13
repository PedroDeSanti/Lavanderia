create table pedido
	(ID_pedido int(5),
     CPF int(11),
     dataPedido date,
     estado varchar(15),
     primary key (ID_pedido, CPF));