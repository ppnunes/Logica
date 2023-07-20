def f_soma (v1, v2):
    return v1+v2

def f_subtracao (v1, v2):
    return v1-v2

if __name__ == '__main__':

    v1 = int(input("Digite um valor: "))
    v2 = int(input("Digite outro valor: "))
    func = int(input("Para somar digite 1, para subtrair digite 0:"))
    if func == 1:
        print("Soma: ", f_soma(v1, v2))
    else:
        print("Subtração: ", f_subtracao(v1, v2))

