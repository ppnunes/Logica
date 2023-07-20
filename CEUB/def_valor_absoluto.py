def valor_absoluto (n):
    if n > 0:
        return n
    else:
        return n*(-1)

if __name__ =='__main__':

    n = int(input("Digite um valor: "))
    print(valor_absoluto(n))