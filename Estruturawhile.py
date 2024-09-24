sexo = str(input('Digite seu sexo: '
             '[M] para masculino'
             '[F] para feminino '))

while sexo not in 'MFmf':
    sexo = str(input('Dados invalidos: por favor digite novamente ')).strip().upper()[0]
print('{} Sexo registrado com sucesso'.format(sexo))