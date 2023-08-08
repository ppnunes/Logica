--cria o banco de dados bd_rh_noite
create database bd_rh_noite;

-- usa o banco de dados bd_rh_noite
use bd_rh_noite;

-- cria tabela tb_cargo
create table tb_cargo(
	cd_cargo int not null primary key,
	cargo char(30));

-- cria tabela tb_setor
create table tb_setor(
	cd_setor int not null primary key,
	setor char(30));

-- cria tabela tb_funcionario
create table tb_funcionario(
	matricula int not null primary key,
	funcionario char (50),
	dt_nascimento date,
	cd_setor int,
	cd_cargo int,
	salario decimal(12,2));

-- cria relacionamento entre tabelas funcionario e cargo
alter table tb_funcionario
add constraint fk_cargo foreign key (cd_cargo)
references tb_cargo (cd_cargo);

-- cria relacionamento entre tb_funcionario e tb_setor
alter table tb_funcionario
add constraint fk_setor foreign key (cd_setor)
references tb_setor (cd_setor);