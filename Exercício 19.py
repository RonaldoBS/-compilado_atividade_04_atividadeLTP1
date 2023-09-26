def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)


def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        imprimir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1 ou 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1
        else:
            print("Essa posição já foi escolhida. Tente novamente.")
            continue

        if jogadas >= 5:
        # Verifique se há um vencedor após a 5ª jogada
        # Implementar as regras de vitória aqui

        if jogadas == 9:
            # Empate
            imprimir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"


if __name__ == "__main__":
    jogar_jogo_da_velha()
