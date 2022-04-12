saldo = 0
def menu():
    print('MENU')
    print('''[1]Abrir Conta
[2]Realizar Depósito
[3]Realizar Saque
[4]Aplicar Juros
[5]Simular Empréstimo
[6]Extrato
[7]Sair''')
    item = input('Selecione a opção desejada: ')
    return item


def opcao_1():
    print('Opção escolhida: Abrir Conta')
    nome = input('Informe seu nome: ')
    saldoInicial = int(input('Saldo inicial: '))
    saldo = saldo + saldoInicial
    print('Saldo atual de {}'.format(saldo))

    return nome, saldo


def opcao_2():
    print('Opção escolhida: Realizar depósito')
    valor = int(input('Valor do depósito: '))
    if valor < 1:
        print('ação inválida!')
    else:
        print('Depósito realizado')

def opcao_3():
    print('Opção escolhida: Realizar Saque')
    saque = int(input('Valor do saque: '))
    if saque <= 0:
        print('ação inválida!')
    elif saldo < saque:
        print('Saldo insuficiente')

def opcao_4():
    print('Opção escolhida: Aplicar Juros')
    juros = int(input('Taxa de juros: '))
    if juros <= 0:
        print('A taxa deve ser maior que zero.')

def opcao_5():
    print('Opção escolhida: Simular Empréstimo')
    emprestimo = int(input('Valor do empréstimo: '))
    jurosMensal = int(input('Juros mensal: '))
    prcelas = int(input('Quantidade de parcelas: '))

def opcao_6():
    print('Opção escolhida: Extrato')


escolha = ''
while(escolha != '7'):
    escolha = menu()
    if escolha == '1':
        opcao_1()
    elif escolha == '2':
        opcao_2()
    elif escolha == '3':
        opcao_3()
    elif escolha == '4':
        opcao_4()
    elif escolha == '5':
        opcao_5()
    elif escolha == '6':
        opcao_6()
    elif escolha == '7':
        print('Saindo...')
    else:
        print('Opção desconhecida!')

