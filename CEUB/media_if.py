nota1 = float(input("Digite a primeira nota:\n"))
nota2 = float(input("Digite a seguda nota:\n"))

media = (nota1 + nota2)/2

if media >= 5:
    print("Média {:.2f}" .format(media), "Aluno aprovado")

else:
    print("Média {:.2f}" .format(media), "Aluno reprovado")

