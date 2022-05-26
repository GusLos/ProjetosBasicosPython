import random as ran
# from xmlrpc.client import boolean

def criar_baralho():
    """
    Função cria um baralho.

    Return: Dicionario de baralho:\n
                -primeira chave é o naipe(str).\n
                -segunda chave é o nome da carta(str).\n
                -valor é o valor da carta (int) segundo BlackJack.
    """
    espadas = {'as': 1, '2': 2, '3': 3, '4':4 ,'5':5 , '6':6 , '7':7 , '8': 8, '9': 9, '10': 10, 'valetes': 10, 'damas': 10, 'reis': 10}
    paus = {'as': 1, '2': 2, '3': 3, '4':4 ,'5':5 , '6':6 , '7':7 , '8': 8, '9': 9, '10': 10, 'valetes': 10, 'damas': 10, 'reis': 10}
    copas = {'as': 1, '2': 2, '3': 3, '4':4 ,'5':5 , '6':6 , '7':7 , '8': 8, '9': 9, '10': 10, 'valetes': 10, 'damas': 10, 'reis': 10}
    ouro = {'as': 1, '2': 2, '3': 3, '4':4 ,'5':5 , '6':6 , '7':7 , '8': 8, '9': 9, '10': 10, 'valetes': 10, 'damas': 10, 'reis': 10}
    baralho = {'espadas': espadas, 'paus': paus, 'copas': copas, 'ouro': ouro}
    return baralho

def distribuir_cartas(baralho, num_cartas):
    mao = {}                                                  # Inicializa mão
    naipes = list(baralho.keys())
    for x in range(num_cartas):
        naipe = ran.choice(naipes)
        carta = ran.choice(list(baralho[naipe].keys()))
        if naipe in mao:
            mao[naipe][carta] = baralho[naipe].pop(carta)
        elif not naipe in mao:
            mao[naipe] = {}
            mao[naipe][carta] = baralho[naipe].pop(carta)
        else:                                                 
            print('\n\nErro em atribuir carta na mao.\n')
            return {'erro':'erro'}
        for naipe in naipes:
            if not baralho[naipe]:                            # Verificar se chave naipe em dic baralho esá vazio.
                baralho.pop(naipe)
        naipes = list(baralho.keys())
    return mao


baralho = criar_baralho()

mao = distribuir_cartas(baralho, 7)

print(mao)