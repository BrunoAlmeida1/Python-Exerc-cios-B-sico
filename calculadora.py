# Programa que simula uma calculadorae que além de dar o resultado do cálculo informa se o número é negativo ou positivo, par ou ímpar e inteiro ou decimal

erro = 1
print("="*60)
while erro == 1:
    erro = 0
    try:
        num1 = float(input("Digite o primeiro número a ser calculado: "))
    except ValueError:
        print("\nErro! Digite um número\n")
        erro = 1
erro = 1
while erro == 1:
    erro = 0
    oper = input("\nDigite uma das operações (+, -, *, /): ")
    if oper not in ('+', '-', '*', '/'):
        print("\nOperação Inválida!\nTente novamente\n")
        erro = 1
erro = 1
while erro == 1:
    erro = 0
    try:
        num2 = float(input("\nDigite o segundo número a ser calculado: "))
    except ValueError:
        print("\nErro! Você deve digitar um número\n")
        erro = 1

if oper == '+':
    resul = num1 + num2
elif oper == '-':
    resul = num1 - num2
elif oper == '*':
    resul = num1 * num2
elif oper == '/':
    resul = num1 / num2

oper = input(
    "\nDigite uma das operações (+, -, *, /) ou = para obter o resultado: ")
while(oper != '='):
    while oper not in ('+', '-', '*', '/'):
        print("\nOperação Inválida!\nTente novamente\n")
        oper = input("Digite uma das operações (+, -, *, /): ")
    erro = 1
    while(erro == 1):
        erro = 0
        try:
            num1 = float(input("Digite outro número a ser calculado: "))
        except ValueError:
            print("\nErro! Digite um número\n")
            erro = 1
    if oper == '+':
        resul += num1
    elif oper == '-':
        resul -= num1
    elif oper == '*':
        resul *= num1
    elif oper == '/':
        resul /= num1
    oper = input(
        "Digite uma das operações (+, -, *, /) ou = para obter o resultado: ")

if resul % 2 == 0:
    par_imp = "par"
else:
    par_imp = "impar"

if resul > 0:
    neg_pos = "positivo"
else:
    neg_pos = "negativo"

if resul == round(resul):
    int_dec = "inteiro"
else:
    int_dec = "decimal"

if resul == 0:
    print("\nResultado = 0\n")
elif int_dec == "decimal":
    print(f"\nResultado = {resul}\nNúmero {neg_pos} e {int_dec}.\n")
else:
    print(f"\nResultado = {resul}\nNúmero {par_imp}, {neg_pos} e {int_dec}.\n")
