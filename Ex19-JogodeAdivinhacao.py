from random import randint
from time import sleep

computador = randint(0, 5)
print('=-=' *20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar..')
print('=-=' *20)
jogador = int(input('Em que número pensei: '))
print('Processando...')
sleep(0.10)
cont = 0
acertou = False

while not acertou:
        jogador = int(input('Você não acertou, tente novamente! '))
        cont += 1
        if jogador == computador:
            acertou = True
        else:
            if jogador < computador:
                print('Mais...tente novamente. ')
            elif jogador > computador:
                print('Menos... tente novamente. ')

print('Você acertou!! com {} tantas tentativas'.format(cont))