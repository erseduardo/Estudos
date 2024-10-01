listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-'*40)

for posicao in range(0, len(listagem)): #o range vai da posição 0 até o final da lista(listagem)
    if posicao % 2 == 0:                #se posicao for par, então ele aparecerá os nomes; produto sempre na posição impar
        print(f'{listagem[posicao]:.<30}',end='')
    else:
        print(f'R$ {listagem[posicao]:5.2f}')
print('-'*40)