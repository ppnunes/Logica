print("Sequência binários")

for b1 in range (0,2):
    for b2 in range (0,2):
        for b3 in range (0,2):
            valor_decimal = b1 * 2**2 + b2 * 2**1 + b3 * 2**0
            print(valor_decimal,"-", b1, b2, b3, sep='')           # print(f"{b1}{b2}{b3}")

