#Refatorar nosso código usando Dicionário, Type Hint e Funcões.

BONUS_2024 = 1000
funcionarios: list = []

#funcao coleta nome
def coleta_nome():
    nome_valido: bool = False
    while not nome_valido:
        try:
            nome: str = input("Digite seu nome: ")
            if len(nome) == 0:
                raise ValueError("O nome não pode estar vazio.")
            if any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            else:
                print("Nome válido:", nome)
                nome_valido = True
        except ValueError as e:
            print(e)
        return nome

#funcao coleta salario
def coleta_salario():
    salario_valido = False
    while not salario_valido:
        try:
            salario = float(input("Qual seu salario? "))
            if salario < 0:
                raise ValueError("Salário inválido. digite apenas valores positivos.")
            else:
                print("Salário válido:", salario)
                salario_valido = True
        except ValueError:
            print("Salário inválido. digite apenas numeros.")
    return salario


#funcao coleta bonus percent
def coleta_bonus_percent():

    bonus_percent_valido = False
    while not bonus_percent_valido:
        try:
            bonus_percent = float(input("Qual o valor do bonus recebido? "))
            if bonus_percent < 0:
                print("Bonus inválido. digite apenas valores positivos.")
            else:
                print("Bonus válido:", bonus_percent)
                bonus_percent_valido = True
        except ValueError:
            print("Bonus inválido. digite apenas numeros.")
    return bonus_percent

#funcao salva dados do funcionario em um dict, na lista de funcionarios
def cadastra_funcionario():
    nome = coleta_nome()
    salario = coleta_salario()
    bonus_percent = coleta_bonus_percent()
    total_bonus = (salario * bonus_percent) + BONUS_2024
    return {"nome": nome, "salario": salario, "bonus_percent": bonus_percent, "total_bonus": total_bonus}


novo_funcionario: dict = cadastra_funcionario()

funcionarios.append(novo_funcionario)

print(funcionarios)
