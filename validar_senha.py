# Programa que simula um registrador de senhas que exige um número mínimo e máximo de caracteres, além de outras características para senha

def validar(texto, min, max):
    for tentativa in range(4):
        if tentativa < 3:
            print(f'{tentativa + 1}ª tentativa')
        else:
            return False
        print('~'*30)
        psw = input(texto)
        print()
        if len(psw) < min or len(psw) > max:
            print('Quantidade de caracteres inválida!\n')
        else:
            for n in range(len(psw)):
                if psw[n] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                    for n in range(len(psw)):
                        if psw[n] not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0') and psw[n] == psw[n].lower():
                            for n in range(len(psw)):
                                if psw[n] not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0') and psw[n] == psw[n].upper():
                                    return psw
            else:
                print(
                    'Sua senha precisa mesclar números com letras maiúsculas e minúsculas.')


senha = ('Digite uma senha com no mínino 8 e no máximo 12 caracteres,\n'
         'com letras maiúsculas, minúsculas e números:\n')
password = validar(senha, 8, 12)

if password:
    print('\nSua senha foi salva com sucesso.')
    print('~'*30)
else:
    print('Número máximo de tentativas excedidas.\n'
          'Tente novamente amanhã.')
    print('~'*30)
