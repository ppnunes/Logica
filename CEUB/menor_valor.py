menor_valor = 99999999
ct = 0
soma = 0
print("Digite 0 para sair")
while True:
    valor = float(input("Insira um valor:\n"))
    soma = soma + valor
    if valor == 0:
        break
    if valor < menor_valor:
        menor_valor = valor
    ct = ct + 1

if ct == 0:
    print("Não foi digitado nenhum número.")

else:
    print("O menor valor é: ", menor_valor)
    print("A quantidade de números digitados é ", ct)
    print("A soma dos números digitados é ", soma)


