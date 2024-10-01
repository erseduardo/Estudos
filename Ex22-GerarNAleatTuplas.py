from random import randint
n_aleatorio = (randint(0, 10), randint(0, 10),
               randint(0, 10), randint(0, 10), randint(0, 10) )

print(f'Os valores sorteados foram: {n_aleatorio}')
print(f'O maior valor sorteado foi {max(n_aleatorio)}')
print(f'O menor valor sorteado foi {min(n_aleatorio)}')