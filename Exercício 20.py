def palavras_maiusculas(texto):
    palavras = texto.split()
    palavras_maiusculas = [palavra for palavra in palavras if palavra[0].isupper()]
    return " ".join(palavras_maiusculas)

def palavras_vogais(texto):
    palavras = texto.split()
    palavras_vogais = [palavra for palavra in palavras if palavra[-1].lower() in 'aeiou']
    return " ".join(palavras_vogais)

def palavras_mais_de_5_letras(texto):
    palavras = texto.split()
    palavras_mais_de_5 = [palavra for palavra in palavras if len(palavra) > 5]
    return " ".join(palavras_mais_de_5)

def inverter_palavras(texto):
    palavras = texto.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    return " ".join(palavras_invertidas)

texto = input("Digite uma string contendo várias palavras: ")

print("Palavras que começam com letra maiúscula:")
print(palavras_maiusculas(texto))

print("Palavras que terminam com uma vogal:")
print(palavras_vogais(texto))

print("Palavras com mais de 5 letras:")
print(palavras_mais_de_5_letras(texto))

print("Inverso de cada palavra:")
print(inverter_palavras(texto))
