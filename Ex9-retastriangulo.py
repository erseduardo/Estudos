print('Preciso de 3 valores para verificar se forma um triangulo')

r1 = int(input('Digite o primeiro valor da linha: '))
r2 = int(input('Digite o segundo valor da linha: '))
r3 = int(input('Digite o terceiro valor da linha: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: #sempre irei escolher um foco ex. r1. então r1 é menor que r2 e r1
#é menor que r3, então se forma um triangulo.

    print('Pode-se forma um triangulo')
else:
    print('Não se forma um triangulo')