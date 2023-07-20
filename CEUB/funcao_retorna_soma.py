def retorna_soma (v1, v2):
    soma = v1+v2
    return soma

if __name__ == '__main__':

    valor1 = int(input("Digite um valor:"))
    valor2 = int(input("Digite outro valor:"))

    retorna_soma(valor1, valor2)

    print("Soma: ", retorna_soma(valor1, valor2))

    retorna_soma(2.1, 3.3)

    print("Soma: ", retorna_soma(2.1, 3.3))
