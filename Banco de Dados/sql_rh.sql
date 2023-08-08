--cria o banco de dados bd_rh
create database bd_rh;
--utiliza o banco de dados bd_rh
use bd_rh;
--cria tabela cargo
create table tb_cargo
	(cd_cargo int not null primary key,
    cargo char(30));
create table tb_setor
	(cd_setor int not null primary key,
    setor char(30));
create table tb_funcionario
	(matricula int not null primary key,
	funcionario char(50),
	cd_setor int,
	cd_cargo int,
	salario decimal(12,2));
-- cria relacionamento entre as tabelas funcionario e cargo	
alter table tb_funcionario
	add constraint fk_setor foreign key (cd_setor)
		references tb_setor (cd_setor);
--cria relacionamento entre as tabelas funcionario e cargo
alter table tb_funcionario
	add constraint fk_cargo  foreign key (cd_cargo)
		references tb_cargo (cd_cargo);