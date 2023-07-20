def maximo (n1, n2):
    if n2 > n1:
        maior = n2
    else:
        maior = n1
    return maior

if __name__ == "__main__":

    n1 = float(input("Digite um valor: "))
    n2 = float(input("Digite outro valor: "))

    maximo(n1, n2)

    print("Maior valor : ", maximo(n1, n2))