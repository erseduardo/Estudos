n1 = float(input('Digte a 1º nota: '))
n2 = float(input('Digte a 2º nota: '))
n3 = float(input('Digte a 3º nota: '))
n4 = float(input('Digte a 4º nota: '))
media = (n1 + n2 + n3 + n4) / 4

if media >= 7.0:
        print('Sua média foi {}, Você foi APROVADO'.format(media))
elif media > 5.0 <= 6.9:
    print('Sua média foi {}, Você está em RECUPERAÇÃO'.format(media))
else:
    print('Sua média foi {}, Você está REPROVADO'.format(media))