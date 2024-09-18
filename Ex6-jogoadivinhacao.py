from random import randint
from time import sleep

computado = randint(0, 5) #faz o computador pensar
print('=-=' *20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar..')
print('=-=' *20)
usuario = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)

if usuario == computado:
    print('Parabens você acertou!!! ')
else:
    print('Eu ganhei! Eu pensei no número {} e você {}'.format(computado, usuario))











