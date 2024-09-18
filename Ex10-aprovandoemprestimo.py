casa = float(input('Digite o valor da casa R$ '))
salario = float(input('Digite o seu salario R$ '))
ano = int(input('Digite em quantos anos vai pagar: '))
prestacao = casa / (ano * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, ano), end='')
print('a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo Aprovado')
else:
    print('Emprestimo Negado')

