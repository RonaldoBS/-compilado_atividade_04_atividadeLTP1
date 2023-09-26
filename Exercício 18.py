import random

numero_aleatorio = random.randint(1, 9)

tentativas = 0

while True:
    palpite = int(input("Adivinhe o número (entre 1 e 9): "))
    tentativas += 1

    if palpite == numero_aleatorio:
        print(f"Parabéns! Você adivinhou o número {numero_aleatorio} em {tentativas} tentativa(s).")
        break
    elif palpite < numero_aleatorio:
        print("O número é maior que seu palpite. Tente novamente.")
    else:
        print("O número é menor que seu palpite. Tente novamente.")
