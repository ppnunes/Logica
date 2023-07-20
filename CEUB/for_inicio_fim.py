m = int(input("Digite o início:"))
n = int(input("Digite o fim:"))
ct = 0
soma = 0

if n == m:
    print("Os valores são iguais.")

if n > m:                                       # se o numero de inicio for menor que o do fim
    for i in range(m, n + 1, 1):
        ct += 1
        soma += i
        print(i)

else:                                           # se o numero de inicio for menor que o do fim
    for i in range(m, n-1, -1):                 # n-1 para que o for imprima o valor digitado e pare no próximo (que é um número menor no caso do decrescente)
        ct += 1
        soma += i
        print(i)

print("\nQtd de números:", ct, "\nSoma:", soma)