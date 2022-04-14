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
	(05027479943, 'Gabriel Zambelli', 'rua piva 123'	, 912345678, 'gzs@gmail.com'		, 'gabrielZ'	, '#ForaJohan'		),
	(26484032674, 'João Degelo'		, 'rua traipu 456'	, 987654321, 'jdg@usp.br'			, 'jaoPerfeito'	, '#FPGA'			),
	(04782034793, 'Pedro de Santi'	, 'av pompeia 789'	, 912344321, 'pedro@hotmail.com.br'	, 'pedroDoRole'	, 'HojeANoiteEuVou'	),
	(38907430293, 'Vinicius Lopes'	, 'av jbl 3100'		, 957894578, 'vinicius13@yahoo.com.br', 'ViniDoSohuer', 'souMtoPerfeito'	),
	(93240957389, 'Hugh Gicohc'		, 'rua matao 0'		, 928766789, 'hgpt@outlook.com.br'	, 'HGK8080'		, 'heyheyImhere'	),
	(73925098732, 'Amon Gus'		, 'beco do batman 0', 987346589, 'gusamon@gmail.com.br'	, 'GusAmon30'	, '5U5amogus'		),
	(23784980234, 'Paul Atejan'		, 'av jabaquara 30'	, 987546769, 'pajero1983@usp.br'	, 'peterPK'		, 'parkerMeuHeroi'	),
	(72893490875, 'Tomas'			, 'av pres juscelino 57', 932324589, 'tmz@vhdl.com.br'	, 'Thomax2'		, 'toto3030'		),
	(28903748934, 'Jorge Rady', 'nos nossos corações', 40028922, 'oMelhor@Professor.com.br', 'jorgerady', 'Jorge'),
	(90823749837, 'Pedrao'			, 'rua cataguases 82', 912738940, 'pedro@pedro.com'		, 'pedro'		, 'pedro1'			);
	
insert into funcionario
values 
	(05027479943, 'Gabriel'	, 'rua piva 123'	, 912345678, 'gzs@gmail.com'			, 'gabriel', '#gabriel', 'recepcionista'),
	(26484032674, 'Jao'		, 'rua traipu 456'	, 87654321, 'jdg@usp.br'				, 'jao', 'jaojaojao', 'admin'),
    (38907430293, 'Vinicius', 'av jbl 3100'		, 98766789, 'vinicius13@yahoo.com.br', 'Vini', '1234', 'lavador'),
	(28903748934, 'Jorge Rady', 'nos nossos corações', 40028922, 'oMelhor@Professor.com.br', 'JorgeS2', 'profPerfeito', 'admin'),
    (90823749837, 'Pedrao'	, 'rua cataguases 82', 12344322, 'pedro@pedro.com'			, 'pedro', 'pedro3', 'admin');
	
insert into Item
values
    (1, 2, 1, 'lavando'),
    (2, 2, 1, 'lavando'),
    (3, 2, 1, 'lavando'),
    (3, 2, 1, 'lavando'),
    (4, 2, 1, 'lavando'),
    (5, 2, 1, 'lavando'),
    (6, 2, 1, 'lavando'),
    (6, 2, 1, 'lavando'),
    (7, 2, 1, 'lavando'),
    (8, 2, 1, 'lavando'),
    (9, 2, 1, 'lavando'),
	(1, 1, 1, 'concluido'),
    (3, 5, 2, 'secando'),
    (2, 10, 3, 'lavando'),
    (5, 10999, 4, 'concluido');
    
insert into roupas
values
    (1, 'Camiseta'),
    (2, 'Camisa'),
    (3, 'Calça'),
    (4, 'Bermuda'),
    (5, 'Shorts'),
    (6, 'Cueca'),
    (7, 'Calcinha'),
    (8, 'Meia'),
    (9, 'Moletom'),
    (10, 'Luvas'),
    (11, 'Gorro');


insert into pedido
values
	(54982, 05027479943, '2022-03-17', 'concluido'),
    (38920, 38907430293, '2021-03-26', 'pronto'),
    (31018, 04782034793, '2021-04-04', 'lavando'),
    (01940, 93240957389, '2022-04-01', 'pronto'),
    (21048, 26484032674, '2019-11-30', 'lavando'),
    (99178, 26484032674, '2021-03-28', 'concluido'),
    (00102, 72893490875, '2022-12-06', 'pronto'),
    (38540, 05027479943, '2020-04-16', 'lavando'),
    (39230, 93240957389, '2020-05-22', 'pronto'),
    (18450, 04782034793, '2018-12-30', 'lavando'),
    (18133, 90823749837, '2020-02-17', 'concluido'),
    (68545, 28903748934, '2023-03-24', 'pronto'),
    (21803, 26484032674, '2020-07-17', 'lavando'),
    (10384, 28903748934, '2021-04-22', 'pronto'),
    (10485, 05027479943, '2017-12-07', 'lavando'),
    (17032, 73925098732, '2020-03-02', 'concluido'),
    (10472, 90823749837, '2021-08-26', 'pronto'),
    (19372, 38907430293, '2022-06-11', 'lavando'),
    (18492, 28903748934, '2020-06-30', 'pronto'),
    (10740, 38907430293, '2021-12-21', 'lavando'),
    (00182, 28903748934, '2020-01-16', 'concluido'),
    (09270, 90823749837, '2022-07-15', 'pronto'),
    (00012, 05027479943, '2022-04-02', 'lavando'),
    (19047, 23784980234, '2022-10-30', 'pronto'),
    (19730, 04782034793, '2021-12-29', 'lavando'),
    (27093, 23784980234, '2019-11-16', 'secando');

insert into TipoLavagem
values
	(1, 'lavagem normal', 6.00, 1),
	(2, 'lavagem a seco', 10.00, 2),
    (3, 'lavagem sem lavar', 999.99, 15),
    (4, 'hidratação', 1.00, 3),
    (5, 'só no paninho', 123.94, 83);
