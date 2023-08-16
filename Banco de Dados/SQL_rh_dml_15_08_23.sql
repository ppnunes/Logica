-- listar as informações da tabela tb_funcionario

select * from tb_funcionario;


select * from tb_funcionario
where cd_setor = 2;
-- seleciona as linhas onde o valor de cd_setor é 2

select * from tb_funcionario
where cd_cargo = 1;
-- lista as linhas da tb_funcionario onde cd_cargo = 1

delete tb_cargo
where cd_cargo = 1;
-- fere a restrição referencial, não foi excluída

delete tb_setor
where cd_setor = 1;
-- fere a restrição referencial

update tb_funcionario
set salario = 6000
where matricula = 1;
-- altera o salario do funcionario cuja matricula é 1