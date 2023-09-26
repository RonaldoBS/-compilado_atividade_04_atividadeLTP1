limite_inferior = int(input("Digite o limite inferior: "))
limite_superior = int(input("Digite o limite superior: "))

print(f"Números pares entre {limite_inferior} e {limite_superior}:")
for numero in range(limite_inferior, limite_superior + 1):
    if numero % 2 == 0:
        print(numero)
