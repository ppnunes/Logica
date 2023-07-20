print("Para sair, digite 0")
ctf = 0
ctm = 0
menor = 99999999
maior = -99999999
cta = 0
soma_a = 0

while True:
    alt = float(input("Digite a altura:\n"))
    if alt == 0:
        break
    gen = input("Insira [F] para feminino ou [M] para masculino:")
    if gen == "F":
        ctf += 1  # ctf = ctf + 1

    if gen == "M":
        ctm +=1

    if alt > maior:
        maior = alt

    if alt < menor:
        menor = alt

    cta += 1
    soma_a = soma_a + alt
    media_a = soma_a / cta


print("Maior: ", maior, "Menor: ", menor, "Masc: ", ctm, "Fem: ", ctf, "Média das alturas: ", media_a)