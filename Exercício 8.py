try:
    n = int(input("Digite um número inteiro positivo: "))

    if n <= 0:
        print("Por favor, insira um número inteiro positivo.")
    else:
        soma = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0:
                soma += i
        print(f"A soma dos números de 1 a {n} divisíveis por 3 ou 5 é {soma}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
