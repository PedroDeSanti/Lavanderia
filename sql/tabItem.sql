create table item
	(ID_item int(3),
     ID_pedido int(5),
     ID_tipoLavagem int(3),
     estado varchar(15),
     primary key (ID_item, Id_pedido));