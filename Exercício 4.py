def eh_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    else:
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                return False
        return True

numero = int(input("Digite um número inteiro: "))

print(f"Divisores primos de {numero}:")
for divisor in range(1, numero + 1):
    if numero % divisor == 0 and eh_primo(divisor):
        print(divisor)
