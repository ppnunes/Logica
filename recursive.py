# Define uma função de cálculo do fatorial para um número n inteiro.
def factorial(n: int):
    # Se o número fornecido é menor ou igual a 1, o fatorial é 1. Retorna 1.
    if n <= 1:
        return 1
    # Caso contrário (se for maior que 1), chama a função recursivamente até chegar ao valor final do fatorial.
    else:
        # Multiplica o valor atual pelo fatorial do próximo número em ordem decrescente até chegar a 1.
        return factorial(n-1)*n

def test_factorial():
    # Test edge cases where n is 0 or 1
    assert factorial(0) == 1
    assert factorial(1) == 1

    # Test case where n is a positive integer
    assert factorial(5) == 120
    
    # Test case where n is a negative integer
    assert factorial(-3) == None

    # Test case where n is a float value
    assert factorial(2.5) == None

    

if __name__ == "__main__":
    print(factorial(5))
    test_factorial()