import math

try:
    raio = float(input("Digite o raio da esfera em metros: "))

    if raio <= 0:
        print("Por favor, insira um raio válido maior que zero.")
    else:
        volume_litros = (4 / 3) * math.pi * raio ** 3 * 1000  # Multiplica por 1000 para converter para litros
        print(f"O volume da esfera é {volume_litros:.2f} litros")
except ValueError:
    print("Por favor, insira um valor válido para o raio (número).")
