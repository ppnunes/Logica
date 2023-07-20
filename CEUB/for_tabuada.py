print("Tabuada")
print("Para sair, digite -1.")
ct = 0

while True:
    a = int(input("\nQual número você quer multiplicar?"))
    if a == -1:
        break
    for i in range(1, 10 + 1):
        print(f"{i} * {a} =  {i * a:2} ")
    ct += 1

print(f"Número de tabuadas: {ct}")



