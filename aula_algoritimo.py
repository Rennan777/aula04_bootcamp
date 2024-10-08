lista_de_numeros: list = [40, 50, 60, 70, 0, -408, 1, 50]

def ordena_lista_de_numeros(numeros: list) -> list:
    nova_lista_de_numeros: list = numeros.copy()

    for i in range (len(nova_lista_de_numeros)):
        for j in range(i + 1, len(nova_lista_de_numeros)):
            if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = nova_lista_de_numeros[j], nova_lista_de_numeros[i]
    return nova_lista_de_numeros

nova_lista = ordena_lista_de_numeros(lista_de_numeros)
print(nova_lista)

# nova_lista = sorted(lista_de_numeros)
# print(nova_lista)

# lista_de_numeros.sort()
# print(lista_de_numeros)