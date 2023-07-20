# 1.	Elabore o programa que gere a sequência do dobro dos números naturais até 10 na
# ordem crescente. Mostre também a soma da sequência gerada.

print("Dobro dos números")
soma = 0
for i in range (0,10+1,1):
    soma += (i*2)
    print(i*2)
print("A soma é:", soma)