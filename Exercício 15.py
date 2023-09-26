def fibonacci(n):
    a, b = 0, 1
    fib_lista = []
    for _ in range(n):
        fib_lista.append(a)
        a, b = b, a + b
    return fib_lista

try:
    n = int(input("Quantos números de Fibonacci você deseja ver? "))

    if n <= 0:
        print("Por favor, insira um número inteiro positivo.")
    else:
        numeros_fibonacci = fibonacci(n)
        print("Números de Fibonacci:")
        print(", ".join(map(str, numeros_fibonacci)))
except ValueError:
    print("Por favor, insira um número inteiro válido.")
