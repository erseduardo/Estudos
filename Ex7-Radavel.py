velocidade = float(input('Qual a velocidade do veiculo: '))

if velocidade <=80:
    print('Sua velocidade foi {}km, está dentro da velocidade permitida'.format(velocidade))
else:
    multa = 7 * (velocidade - 80)
    print('Sua velocidade foi {}kms, você foi multado em R${:.2f}'.format(velocidade, multa))