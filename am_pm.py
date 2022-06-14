# Programa que converte do formato 24h para o formato de 12h

def hora(h):
    if (h != 24) & (h % 12 == 0):
        return h
    else:
        return h % 12


def imprimi(h, m):
    horas = (10 <= h < 12)
    minutos = m < 10
    print(f"horas = {horas} | minutos = {minutos}")

    if ((h < 10) & (m < 10)) | (h == 24) & (m < 10):
        print(f"0{hora(h)}:0{m} A.M.")
    elif (h < 10) & (m >= 10) | (h == 24):
        print(f"0{hora(h)}:{m} A.M.")
    elif (10 <= h < 12) & (m < 10):
        print(f"{hora(h)}:0{m} A.M.")
    elif (10 <= h < 12) & (m >= 10):
        print(f"{hora(h)}:{m} A.M.")
    elif (12 < h < 22) & (m < 10):
        print(f"0{hora(h)}:0{m} P.M.")
    elif (12 < h < 22):
        print(f"0{hora(h)}:{m} P.M.")
    elif m < 10:
        print(f"{hora(h)}:0{m} P.M.")
    else:
        print(f"{hora(h)}:{m} P.M.")


print("\nCONVERSÃO DO FORMATO 24h PARA O DE 12h\n")
opc = 's'
while opc == 's' or opc == 'S':
    time = input("\nInforme as horas que deseja converter: ")
    try:
        hor = int(time[0]+time[1])
        minut = int(time[3]+time[4])
        imprimi(hor, minut)
    except ValueError:
        print("\nFormato de horas inválido!")
    opc = input("\nDeseja converter mais uma vez? S = Sim / N = Não\n")
