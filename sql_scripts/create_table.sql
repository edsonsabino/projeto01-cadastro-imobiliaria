 create database db_imobiliaria;
 use db_imobiliaria;

-- Creating tables

create table if not exists tbl_inquilinos (
 id int auto_increment primary key,
 nome varchar(50), 
 data_nasc date
 );
create table if not exists tbl_proprietarios (
 id int auto_increment primary key,
 nome varchar(50), 
 data_nasc date
 );
create table if not exists tbl_imoveis(

id_imovel int primary key,
logradouro varchar(50),
CEP varchar (8),
bairro varchar(40),
cidade varchar(40),
id_proprietario int,

constraint PropImovel_fkey foreign key (id_proprietario) 
	references tbl_proprietarios(id)
 );
 create table if not exists tbl_alugueis(

id_aluguel int primary key,
id_imovel int,
id_inquilino int,

constraint InquiAluguel_fkey foreign key (id_inquilino) references tbl_inquilinos(id),
constraint ImovAluguel_fkey foreign key (id_imovel) references tbl_imoveis(id_imovel)
 );
