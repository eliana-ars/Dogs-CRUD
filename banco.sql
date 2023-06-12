create database cadastro;
use cadastro;

create table cadastrar(
código varchar (50) not null primary key,
peso varchar (50) not null,
datas date not null,
idade varchar (11) not null,
especie varchar (11) not null,
descricao varchar (50) not null
);

select * from cadastrar;