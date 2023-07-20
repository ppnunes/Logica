def mostra_msg():
    print("Bem-vindo ao def do python.")

def mostra_msg_2(msg):
    print(msg)

if __name__ == '__main__':                      # atalho: mai e aperta tab
    print("Msg antes de chamar a função.")
    mostra_msg()
    print("Msg depois de chamar a função.")
    mostra_msg_2("inhóim")
    msg = input("Digite outra mensagem: ")
    mostra_msg_2(msg)

