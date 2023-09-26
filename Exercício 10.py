try:
    n = int(input("Digite um número inteiro positivo: "))

    if n <= 0:
        print("Por favor, insira um número inteiro positivo.")
    else:
        quadrados = {}  # Dicionário para armazenar os pares (i, i*i)
        for i in range(1, n + 1):
            quadrados[i] = i * i

        print("Quadrados dos números inteiros positivos:")
        for i, quadrado in quadrados.items():
            print(f"{i}: {quadrado}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
