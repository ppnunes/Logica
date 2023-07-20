# Exercicio 1

import math

r = float(input("Insira o raio:\n"))

v = 4/3 * math.pi * r**3

print("O volume da esfera é: ", v)



# Exercício 2

ct_par = 0
ct_impar = 0
soma_par = 0
soma_impar = 0
print("Para sair, digite 0.")

while True:
    num = int(input("insira um valor:\n"))
    if num == 0:
        break
    else:
        if num % 2 == 0:
            ct_par += 1
            soma_par += num
            media_par = soma_par / ct_par

        if num % 2 != 0:
            ct_impar += 1
            soma_impar += num
            media_impar = soma_impar / ct_impar

print("A média dos números pares é:", media_par, " e a média dos numeros ímpares é: ", media_impar)