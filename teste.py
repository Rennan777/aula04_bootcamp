#Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65},
#calcule o preço total da lista de compras.


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
