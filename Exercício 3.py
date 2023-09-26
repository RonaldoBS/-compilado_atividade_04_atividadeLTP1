numero = int(input("Digite um número inteiro: "))

print(f"Divisores de {numero}:")

for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        print(divisor)
