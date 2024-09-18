from datetime import date
nascimento = int(input('Digite seu ano de nascimento: '))
ano = date.today().year - nascimento

if ano == 18:
    print('Você tem {} anos é Hora de se Alistar!'.format(ano))
elif ano <= 16:
    print('Você tem {} anos é Ainda não é o tempo de se Alistar'.format(ano))
    saldo = 18 - ano
    print('Falta {} ano para você se alistar'.format(saldo))
elif ano == 17:
    print('Você tem {} anos é Ainda falta 1 ano para você se alistar'.format(ano))
else:
    print('Você tem {} anos é Passou o tempo de alistamento'.format(ano))
    saldo = ano - 18
    print('Você passou do tempo {} anos'.format(saldo))
