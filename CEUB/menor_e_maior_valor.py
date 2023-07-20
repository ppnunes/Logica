menor_valor = float('inf')              # ou menor_valor = 99999999
maior_valor = float('-inf')            # ou maior_valor = -99999999
ct = 0
soma = 0

print("Digite -1 para sair")
while True:
    valor = float(input("Insira um valor:\n"))

    if valor == -1:
        break
    if valor < menor_valor:             # compara o num digitado com o menor valor e atualiza a variavel menor valor
        menor_valor = valor
    if valor > maior_valor:               # compara o num digitado com o maior valor e atualiza a variavel maior valor
        maior_valor = valor

    ct = ct + 1
    soma = soma + valor

if ct == 0:
    print("Não foi digitado nenhum número válido.")
else:
    print("O menor valor é: ", menor_valor, " e o maior valor é ", maior_valor,
              "\nA quantidade de valores digitados é: ", ct, "\nA soma dos valores digitados é: ", soma)




