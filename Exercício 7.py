try:
    n = int(input("Digite um número inteiro positivo: "))

    if n <= 0:
        print("Por favor, insira um número inteiro positivo.")
    else:
        soma = 0
        for i in range(1, n + 1):
            soma += i
        print(f"A soma de todos os números de 1 a {n} é {soma}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
