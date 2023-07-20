n = int(input("Insira a quantidade de alunos:"))
soma = ct = 0

for i in range (1, n+1, 1):
    i = float(input("Insira as notas:"))
    ct += 1
    soma += i
    media = soma / ct
print(f"Média da turma: {media:.2f}")               # para imprimir a media com duas casas decimais