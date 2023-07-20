gender = int(input("Digite seu gênero [1] Feminino ou [2] Masculino:"))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

if gender == 1:
    peso_ideal = (62.1 * altura) - 44.7

else :
    peso_ideal = (72.7 * altura) - 58

print("Peso ideal = {} kg" .format(peso_ideal))