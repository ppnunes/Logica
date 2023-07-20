def calc_dobro(p_valor):
    dobro = p_valor*2
    return dobro

def calcula_triplo(p_valor):
    triplo = p_valor*3
    return triplo

if __name__ == '__main__':
    valor = int(input("Valor: "))
    calc_dobro(valor)
    calcula_triplo(valor)
    print("Valor retornado pela função dobro: ", calc_dobro(valor), "\nValor retornado pela função triplo: ", calcula_triplo(valor))