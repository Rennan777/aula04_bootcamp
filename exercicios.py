#Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
lista_numeros: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in lista_numeros:
    num = numero ** 2
    print(f'{numero} elevado ao quadrado é {num}')

#Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
linguagens: list = ["Python", "Java", "C++", "JavaScript"]

print(linguagens)

linguagens.remove("C++")
linguagens.append("Ruby")

print(linguagens)

#Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro_01: dict = {
    "titulo": "livro_01",
    "autor": "autor_01",
    "ano_publicacao": 2022
}

for c, v in livro_01.items():
    print(f"{c}: {v}")

#Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
entrada: str = "banana"

dicionario: dict = {}

for letra in entrada:
    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1

for c, v in dicionario.items():
    print(f"letra {c}: {v}")

#Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
lista_frutas: list = ["maçã", "banana", "cereja"]

dict_frutas: dict = {
        "maçã": 0.45,
        "banana": 0.30,
        "cereja": 0.65
        }
total_compras: float = 0
for item in lista_frutas:
    total_compras += dict_frutas[item]
print(f'total da compra: {total_compras}')