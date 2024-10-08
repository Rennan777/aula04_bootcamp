import csv

caminho: str = "exemplo.csv"

arquivo_csv: list = []

with open(caminho, "r") as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)