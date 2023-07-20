print("Dado 1 - Dado 2")
ct = 0
for dado in range(1,6+1):
    for dado2 in range (1,6+1):
        print(dado, " - ", dado2)
        ct += 1

print("Quantidade de combinações:", ct)