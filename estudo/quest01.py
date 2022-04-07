limite_1 = int(input('Informe um número positivo: '))
limite_2 = int(input('Informe o segundo número: '))
multiplicador = int(input('Informe o terceiro número: '))

while limite_1 <= limite_2 and limite_1 > 0 and limite_2 > 0:
    if limite_1 % multiplicador == 0:
        print(limite_1)
    limite_1 = limite_1 + 1

    print('Finalizado.')
else:
    print('Informe números positivos.')
