def raiz_quadrada_aproximada(n):
    if n < 0:
        return "Número deve ser positivo"
    if n == 0:
        return 0
    limite_inferior = 0
    limite_superior = n
    raiz_aproximada = (limite_inferior + limite_superior) / 2.0
    precisao = 0.001
    while abs(raiz_aproximada ** 2 - n) > precisao:
        if raiz_aproximada ** 2 < n:
            limite_inferior = raiz_aproximada
        else:
            limite_superior = raiz_aproximada
        raiz_aproximada = (limite_inferior + limite_superior) / 2.0
    return raiz_aproximada

try:
    numero = int(input("Digite um número inteiro positivo: "))

    if numero < 0:
        print("Por favor, insira um número inteiro positivo.")
    else:
        resultado = raiz_quadrada_aproximada(numero)
        print(f"A raiz quadrada aproximada de {numero} é aproximadamente {resultado:.3f}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
