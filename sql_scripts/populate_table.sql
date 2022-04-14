
# use db_imobiliaria;

-- Inserting data onto tables for simple testing

insert into tbl_inquilinos (nome, data_nasc) values 
('Santos Dumont', '1873-07-20'),
('Berta Lutz', '1894-08-02'),
('Nilton Gonçalves', '1933-12-09');

insert into tbl_proprietarios (nome, data_nasc) values 
('Pedro Cabral', '1953-07-26'),
('Ivone Lara', '1921-04-13');

insert into tbl_imoveis (id_imovel, logradouro, CEP, cidade, bairro, id_proprietario) values 
(520,'Av. Prof. Abraão de Morais 10100','04123001', 'São Paulo', 'Bosque da Saúde',2),
(521,'Av. Barão de Oliveira Castro 40','03122262', 'Rio de Janeiro', 'Horto',2),
(522,'Av. do Cursino, 2400','04123001', '04151010', 'Bosque da Saúde',1);

insert into tbl_alugueis (id_aluguel,id_inquilino,id_imovel) values 
('1001',1,521),
('1002',2,522),
('1003',3,520);

select count(id_imovel) from tbl_imoveis where id_proprietario=2;



select * from tbl_imoveis;
