# 1.	Desenvolva uma função que recebe uma mensagem e um número, ela mostra a mensagem e o número e não retorna nada.
# A função main chama a função passando os dois argumentos.

def msg_num(msg, num):
    print(msg, num)

if __name__ == '__main__':
    msg = str(input("Digite uma mensagem: "))
    num = int(input("Digite um número: "))
    msg_num(msg,num)


#2.	Implemente uma função que recebe dois valores e retorna a multiplicação deles. A função main chama essa função duas vezes. Use inputs.

def multiplica(n1, n2):
    produto = n1 * n2
    return produto

if __name__ == '__main__':
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite um número: "))
    multiplica(num1, num2)
    num3 = float(input("Digite um número: "))
    num4 = float(input("Digite um número: "))
    multiplica(num3,num4)
    print(multiplica(num1, num2),multiplica(num3,num4) )