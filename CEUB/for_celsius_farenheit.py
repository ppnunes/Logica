print("  Farenheit| Celsius")
soma = 0
for f in range (45, 81, 1):
    c = 5*(f-32)/9
    soma += f
    print(f"{f:8.2f}°F |  {c:.2f}°C")  # o 8 na formula 'f:8.2f dá 8 espaços antes de f
print("Soma valores °F:", soma)