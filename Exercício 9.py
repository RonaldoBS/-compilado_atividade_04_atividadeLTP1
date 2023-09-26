try:
    comprimento = float(input("Digite o comprimento do retângulo: "))
    largura = float(input("Digite a largura do retângulo: "))

    if comprimento <= 0 or largura <= 0:
        print("Por favor, insira dimensões válidas maiores que zero.")
    else:
        area = comprimento * largura
        perimetro = 2 * (comprimento + largura)
        print(f"A área do retângulo é {area:.2f} unidades quadradas.")
        print(f"O perímetro do retângulo é {perimetro:.2f} unidades.")
except ValueError:
    print("Por favor, insira dimensões válidas (números).")
