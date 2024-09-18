from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Jogador qual a sua jogada: '))
print('-='*11)
print('COMPUTADOR JOGOU {}'.format(itens[computador]))
print('JOGADOR JOGOU {}'.format(itens[jogador]))
print('-='*11)


if computador == 0:
    if jogador == 0:
        print('JOGO EMPATADO')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('JOGADOR PERDEU')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:
    if jogador == 0:
        print('JOGADOR PERDEU')
    elif jogador == 1:
        print('JOGO EMPATADO')
    elif jogador == 2:
        print('JOGADOR GANHOU ')
    else:
        print('JOGADA INVALIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('JOGADOR PERDEU')
    elif jogador == 2:
        print('JOGADOR PERDEU')
    else:
        print('JOGADA INVALIDA')