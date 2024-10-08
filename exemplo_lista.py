produto: str = "caneta"
produto_2: str = "caderno"
produto_3: str = "lapis"

produtos: list = []

produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)

print(produtos)

produtos.remove("lapis")
produtos.pop()

print(produtos)


numeros: list = []
numeros.extend(range(0,5))
print(numeros)