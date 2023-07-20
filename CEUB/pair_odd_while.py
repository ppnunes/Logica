ct = 0
soma = 0
print("Digite 0 para sair")
while True:
    num = (int(input("Digite um número:\n")))
    if num == 0:
        break
    resto = num % 2
    if resto == 0:
        soma = soma + num
        ct = ct + 1
if ct != 0:
    media = soma / ct
    print("Média: ", media)
else:
    print("Não pode dividir por zero.")