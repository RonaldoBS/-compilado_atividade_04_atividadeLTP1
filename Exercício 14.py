try:
    numero = int(input("Digite um número inteiro positivo: "))

    if numero <= 0:
        print("Por favor, insira um número inteiro positivo.")
    else:
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
