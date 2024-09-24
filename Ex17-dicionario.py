dicionario = {'nome': 'ana', 'idade': 25, 'cidade': 'brasilia'} #nome seguido ":" significa que é uma chave, e ana é um valor da chave

for chave, valor in dicionario.items(): #.itens retorna uma visualização dos pares chave-valor
    print('{} : {}'.format(chave, valor))