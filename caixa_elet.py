# Programa que apartir do valor informado, calcula o menor número de cédulas possíveis a serem sacadas

valor = int(
    input("Informe o valor a ser sacado\nMínimo R$ 10,00 / Máximo R$ 600,00: "))

while valor < 10 or valor > 600:
    valor = int(
        input("\nValor Inválido!\nDigite um valor maior que 10 e menor que 600: \n"))
print("\n")

if valor >= 100:
    cedulas = valor // 100
    print(f"Notas de 100 = {cedulas}")
    valor = valor % 100
if valor >= 50:
    cedulas = valor // 50
    print(f"Notas de 50 = {cedulas}")
    valor = valor % 50
if valor >= 20:
    cedulas = valor // 20
    print(f"Notas de 20 = {cedulas}")
    valor = valor % 20
if valor >= 10:
    cedulas = valor // 10
    print(f"Notas de 10 = {cedulas}")
    valor = valor % 10
if valor >= 5:
    cedulas = valor // 5
    print(f"Notas de 5 = {cedulas}")
    valor = valor % 5
if valor >= 1:
    cedulas = valor // 1
    print(f"Notas de 1 = {cedulas}")
    valor = valor % 1
