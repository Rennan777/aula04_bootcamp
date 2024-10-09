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

#Exercícios intermediários e mais avançados 6-15

#Dada uma lista de emails, remover todos os duplicados.
emails = ["pI8U7@example.com", "pI8U6@example.com", "pI8U1@example.com",
          "pI8U7@example.com", "pI8U2@example.com", "pI8A6@example.com",
          "pI8U8@example.com", "pI8U1@example.com", "pI8U6@example.com"]

nova_lista: list = []
for item in emails:
    if item not in nova_lista:
        nova_lista.append(item)

print(nova_lista)


#Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades: list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

maiores18: list = []
for idade in idades:
    if idade >= 18:
        maiores18.append(idade)

print(maiores18)

#Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
pessoas: dict = [
    {
        'nome': 'João',
        'idade': 25
    },
    {
        'nome': 'Maria',
        'idade': 30
    },
    {
        'nome': 'Pedro',
        'idade': 20
    },
    {
        'nome': 'Ana',
        'idade': 35
    }
]

pessoas_ordenado: dict = sorted(pessoas, key=lambda x: x['nome'])
for i in pessoas_ordenado:
    for c, v in i.items():
        print(f'{c}: {v}')
    print()

#Dado um conjunto de números, calcular a média.

numeros: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0
for num in numeros:
    soma += num

media = soma / len(numeros)

print(media)

#Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

numeros: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par: list = []
impar: list = []

for num in numeros:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'lista de pares: {par}')
print(f'lista de ímpares: {impar}')

#Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
produtos: list = [
    {
        "nome": "caneta",
        "preco": 1.99
    },
    {
        "nome": "lapis",
        "preco": 1.99
    },
    {
        "nome": "borracha",
        "preco": 1.99
    }
]

for produto in produtos:
    if produto["nome"] == "caneta":
        produto["preco"] = 2.99

print(produtos)

#Dados dois dicionários, fundi-los em um único dicionário.

dicionario_01: dict = {"nome1": "joão","idade1": 20}

dicionario_02: dict = {"nome2": "pedro","idade2": 19}

dicionario_03: dict = {**dicionario_01,**dicionario_02}

print(dicionario_03)

#Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque: dict = {
    "tomate": 10,
    "alface": 5,
    "batata": 20,
    "feijao": 0
}

mais_de_zero: dict = {}

for i, v in estoque.items():
    if v > 0:
        mais_de_zero[i] = v

print(mais_de_zero)


#Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario: dict = {
    "chave_01": "valor_01",
    "chave_02": "valor_02",
    "chave_03": "valor_03",
    "chave_04": "valor_04"
}

chaves: list = []
valores: list = []

for c, v in dicionario.items():
    chaves.append(c)
    valores.append(v)

print(f'lista de chaves: {chaves}')
print(f'lista de valores: {valores}')

#Dada uma string, contar a frequência de cada caractere usando um dicionário.

string: str = "banana"
contagem: dict = {}

for letra in string:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

print(contagem)

