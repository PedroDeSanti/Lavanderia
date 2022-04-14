insert into administra
values
	(1, 111),
	(5,	555),
    (10999,	555),
    (5,	111),
    (1,	222),
    (10, 444);

insert into cliente
values 
	(111, 'Gabriel Zambelli', 'rua abc 123', 12345678, 'gzs@gmail.com', 'gabOLindo', '#ForaJohan'),
	(222, 'João Degelo', 'rua def 456', 87654321, 'jdg@usp.br', 'jaoOPerfeito', '#FPGA melhor projeto'),
	(333, 'Pedro de Santi', 'rua ghi 789', 12344321, 'pedro@hotmail.com.br', 'pedroDoRole', 'HojeANoiteEuVou'),
	(444, 'Vinicius Lopes', 'rua jkl 0', 98766789, 'vcl@yahoo.com.br', 'ViniDoSohuer', 'souMtoPerfeito'),
	(123, 'Pedrao', 'rua ghi 789', 12344322, 'pedro@pedro.com', 'pedro', 'pedro1');
	
insert into funcionario
values 
	(111, 'Gabriel', 'rua abc 123', 12345678, 'gab@tarcisius.com.br', 'gabriel', '#ForaJohan', 'recepcionista'),
	(222, 'Jao', 'rua def 456', 87654321, 'jao@balbertino.com.br', 'jao', '#FPGA melhor projeto', 'admin'),
    (444, 'Vinicius', 'rua jkl 0', 98766789, 'vini@RISCOLOVER.com.br', 'Vini', 'souMtoPerfeito', 'lavador'),
	(555, 'Jorge Rady', 'nos nossos corações', 40028922, 'oMelhor@Professor.com.br', 'Jorge', 'profPerfeito', 'admin'),
    (123, 'Pedrao', 'rua ghi 789', 12344322, 'pedro@pedro.com', 'pedro', 'pedro3', 'admin');
	
insert into Item
values
	(1, 1, 1, 'concluido'),
    (3, 5, 2, 'secando'),
    (2, 10, 3, 'lavando'),
    (5, 10999, 4, 'concluido');
    
	
insert into pedido
values
	(00001, 111, '2022-03-18', 'concluido'),
    (00010, 222, '2022-04-01', 'pronto'),
    (00005, 444, '1997-12-20', 'lavando'),
    (10999, 333, '2022-04-18', 'secando');

insert into TipoLavagem
values
	(1, 'lavagem a seco', 10.00, 2),
    (2, 'lavagem sem lavar', 999.99, 15),
    (3, 'hidratação', 1.00, 3),
    (4, 'só no paninho', 123.94, 83);
