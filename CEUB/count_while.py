# é preciso usar : após o while
# é preciso indentar

ct = 0
soma = 0
print("Digite -1 para sair")

while True:
    num = int(input("Digite um número:\n"))
    if num  == -1:
        break
    ct = ct + 1
    soma = soma + num



print("Quantidade de números: ", ct, "\nSoma dos valores: ", soma)