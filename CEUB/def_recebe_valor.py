def mostra_valor(valor):
    print("Valor recebido: ", valor)

if __name__ == '__main__':
    print("Msg antes da função")
    mostra_valor(1)
    mostra_valor(1.5)
    mostra_valor(-1)
    print("Msg depois da função")
    valor = input("Digite um valor inteiro: ")
    mostra_valor(valor)