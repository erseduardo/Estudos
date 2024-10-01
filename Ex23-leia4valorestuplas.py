num = (int(input('Digite um numéro: ')),
        int(input('Digite um numéro: ')),
        int(input('Digite um numéro: ')),
        int(input('Digite um numéro: ')))
print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 está na posição {num.index(3)+1}')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')

for n in num:
    if n % 2 == 0:
        print(f'valor par {n} ',end='')
