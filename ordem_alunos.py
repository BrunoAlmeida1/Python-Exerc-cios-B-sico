# Programa que cadastra alunos e depois imprime a lista de alunos por ordem alfabética e dividida por gênero

def imprimir(lista, masc=[], fem=[]):
    for s in lista:
        if s['sexo'] == 'Feminino':
            fem.append(s)
        else:
            masc.append(s)
    print('\n\t*****Lista de Alunas*****\n')
    for dicio in fem:
        for chave in dicio.keys():
            print(f'   {chave} ', end='    |')
        break
    print()
    for dicio in fem:
        for valor in dicio.values():
            print(f'  {valor}   ', end=' ')
        print('')
    print('\n\n\t*****Lista de Alunos*****\n')
    for dicio in masc:
        for chave in dicio.keys():
            print(f'   {chave} ', end='    |')
        break
    print()
    for dicio in masc:
        for valor in dicio.values():
            print(f'  {valor}    ', end=' ')
        print('')
    print('\n')
    print('~'*40)


dados = dict()
lista = []

while True:
    print("*********CADASTRO DE ALUNOS**********\n")
    dados['nome'] = input(
        "Digite o nome do novo aluno ou SAIR para finalizar: ").title()
    if dados['nome'].lower() == 'sair':
        break

    while True:
        print('~'*40)
        sexo = input("\nDigite 1 para masculino ou 2 para feminino: ")

        if sexo == '1':
            dados['sexo'] = "Masculino"
            break
        elif sexo == '2':
            dados['sexo'] = "Feminino"
            break
        else:
            print("Entrada Inválida! Digite 1 ou 2")

    while True:
        print('~'*40)
        try:
            idade = int(input('Informe a idade: '))
            if type(idade) == int:
                idade = str(idade)
                dados['idade'] = idade
                break
        except ValueError:
            print("Entrada Inválida! Digite um número")

    lista.append(dados.copy())

list_alf = sorted(lista, key=lambda n: n['nome'])

imprimir(list_alf)
