ct = 0
soma = 0
while True:
    nota = float(input("Digite as notas:\n"))
    if nota == -1:
        break
    soma = soma + nota
    ct = ct + 1
    media = soma/ct

print(f"A média da turma é  {media:.2f}", "e a quanidade de alunos é ", ct)
