def contar_letras_nome(texto):
    nome = "seunome"
    texto = texto.lower()
    nome = nome.lower()
    contador = 0
    for letra in texto:
        if letra in nome:
            contador += 1
    return contador
texto = input("Digite um texto: ")
quantidade = contar_letras_nome(texto)
print(f"O texto contém {quantidade} letras que compõem o seu nome.")
