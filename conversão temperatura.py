from time import sleep


def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[0;31mERRO!! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(f'\033[1m{txt}\033[m'.center(50))
    print(linha())


def CtoF(num):  # celsius para fahrenheit
    f = num * 1.8 + 32
    return f


def FtoC(num):  # fahrenheit para celsius
    c = (num - 32) / 1.8
    return c


def CtoK(num):  # celsius para kelvin
    k = num + 273.15
    return k


def KtoC(num):  # kelvin para celsius
    c = num - 273.15
    return c


def menu(lista):
    cabecalho('CONVERSÃO DE TEMPERATURA')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c} - \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[1;32mSua Opção: \033[m')
    print(linha())
    return opc


while True:
    resposta = menu(['Celsius para Fahrenheit', 'Fahrenheit para Celsius', 'Celsius para Kelvin',
                     'Kelvin para Celsius', 'Finalizar Programa'])
    if resposta == 1:
        n = float(input('\033[1;32mQual a temperatura: \033[m'))
        cabecalho('Convertendo Celsius para Fahrenheit...')
        sleep(1)
        cabecalho(f'    \033[31m{n}°C = {CtoF(n):.2f}F\033[m')
        sleep(2)
    if resposta == 2:
        n = float(input('\033[1;32mQual a temperatura: \033[m'))
        cabecalho('Convertendo Fahrenheit para Celsius...')
        sleep(1)
        cabecalho(f'    \033[31m{n}F = {FtoC(n):.2f}°C\033[m')
        sleep(2)
    if resposta == 3:
        n = float(input('\033[1;32mQual a temperatura: \033[m'))
        cabecalho('Convertendo Celsius para Kelvin...')
        sleep(1)
        cabecalho(f'    \033[31m{n}°C = {CtoK(n):.2f}K\033[m')
        sleep(2)
    if resposta == 4:
        n = float(input('\033[1;32mQual a temperatura: \033[m'))
        cabecalho('Convertendo Kelvin para Celsius...')
        sleep(1)
        cabecalho(f'    \033[31m{n}K = {KtoC(n):.2f}°C\033[m')
        sleep(2)
    if resposta == 5:
        cabecalho('FINALIZANDO O PROGRAMA...')
        sleep(1)
        break
    if resposta > 5 or resposta < 1:
        print('\033[31mERRO! DIGITE UMA OPÇÃO VÁLIDA\033[m')
        sleep(1)

cabecalho('VOLTE SEMPRE')




