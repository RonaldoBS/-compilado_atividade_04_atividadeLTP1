resultado = []
for numero in range(2000, 3201):
    if numero % 7 == 0 and numero % 5 != 0:
        resultado.append(numero)
print(", ".join(map(str, resultado)))
