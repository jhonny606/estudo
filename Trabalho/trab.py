import random

jogadorUm = input('Informe o nome do jogador 1:')
jogadorDois = input('Informe o nome do jogador 2:')

def traços():
    print('=' * 60)

traços()

def dadoCasa(numeroCasa):
        
    jogarNovamente = random.randint(1, 6)

    if jogarNovamente == 1:
        numeroCasa = numeroCasa + 1
        print('Avance uma casa. Sua casa atual é {}'.format(numeroCasa))
        return numeroCasa
    elif jogarNovamente == 2:
        numeroCasa = numeroCasa + 2
        print('Avance duas casas. Sua casa atual é {}'.format(numeroCasa))
        return numeroCasa
    elif jogarNovamente == 3:
        numeroCasa = numeroCasa - 1
        print('Volte uma casa. Sua casa atual é {}.'.format(numeroCasa))
        return numeroCasa
    elif jogarNovamente == 4:
        numeroCasa = numeroCasa + 4
        print('Avance 4 casas. Sua casa atual é {}'.format(numeroCasa))
        return numeroCasa
    elif jogarNovamente == 5:
        numeroCasa = numeroCasa + 5
        print('Avance 5 casas. Sua casa atual é {}'.format(numeroCasa))
        return numeroCasa
    elif jogarNovamente == 6:
        numeroCasa = numeroCasa - numeroCasa
        print('Você perdeu, volte ao inicio. Casa atual é {}'.format(numeroCasa))
        return numeroCasa
    else:
        print('O jogo quebrou kk')
    return jogarNovamente, numeroCasa

#=====================================================================#
#=====================================================================#
#=====================================================================#

def morreCasa(numeroJogador):
        
    print('Você Morreu. Jogador {} perdeu.'.format(numeroJogador))

    return numeroJogador

#=====================================================================#

def terFilhosCasa(numeroJogador):
    print('Você teve filho! Jogando dado...')
    dadoCasa(6)
    print(dadoCasa)

    return numeroJogador, dadoCasa()

#=====================================================================#

def formaturaCasa(numeroJogador):
    print('Você se formou!')

    return numeroJogador, dadoCasa(5)

#=====================================================================#

def desafioMatematicoCasa(numeroJogador):

    return numeroJogador

#=====================================================================#

def rodarDados(nJogador):
    numeroCasa = 0
    rodarDado = random.randint(1, 6)
    print('{}, Avance {} casas'.format(nJogador, rodarDado))
    numeroCasa = numeroCasa + rodarDado
    print('Sua casa atual é {}'.format(numeroCasa))
    if numeroCasa == 1 or numeroCasa == 3 or numeroCasa == 10 or numeroCasa == 17:
        dadoCasa(1)
    elif numeroCasa == 2 or numeroCasa == 8 or numeroCasa == 18:
        morreCasa(1)
    elif numeroCasa == 4 or numeroCasa == 11 or numeroCasa == 19:
        desafioMatematicoCasa(1)
    elif numeroCasa == 5:
        formaturaCasa(1)
    elif numeroCasa == 6 or numeroCasa == 9 or numeroCasa == 13:
        terFilhosCasa(1)
    elif numeroCasa == 7:
        casarCasa(1)
    elif numeroCasa == 12:
        divorciarCasa(1)
    elif numeroCasa == 14:
        loteriaCasa(1)
    elif numeroCasa == 15:
        ficarFamosoCasa(1)
    elif numeroCasa == 16:
        casarNovamenteCasa(1)
    elif numeroCasa == 20:
            voltarCasas(1)   
    return rodarDado, numeroCasa

rodarDados(jogadorUm)

def dadoCasa(numeroCasa):
        
    jogarNovamente = random.randint(1, 6)

    if jogarNovamente == 1:
        numeroCasa = numeroCasa + 1
        print('Avance uma casa.')
    elif jogarNovamente == 3:
        numeroCasa = numeroCasa - 1
        print('Volte uma casa. Sua casa atual é {}.'.format(numeroCasa))
    elif jogarNovamente == 6:
        numeroCasa = numeroCasa - numeroCasa
        print('Você perdeu, volte ao inicio.')    
    else:
        print('O jogo quebrou kk')
    return jogarNovamente, numeroCasa



def morreCasa(numeroJogador):
        
    print(numeroJogador)

    return numeroJogador

def desafioMatematicoCasa(numeroJogador):

    return numeroJogador

def formaturaCasa(numeroJogador):

    return numeroJogador

def terFilhosCasa(numeroJogador):

    return numeroJogador

def casarCasa(numeroJogador):
    
    return numeroJogador

def ficarFamosoCasa(numeroJogador):

    return numeroJogador

def divorciarCasa(numeroJogador):

    return numeroJogador

def loteriaCasa(numeroJogador):
    
    return numeroJogador

def casarNovamenteCasa(numeroJogador):

    return numeroJogador

def voltarCasas(numeroJogador):

    return numeroJogador
