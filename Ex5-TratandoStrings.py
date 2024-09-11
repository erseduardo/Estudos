nome = input('Digite seu nome completo: ')
print('Seu nome em maisculo: {}'.format(nome.upper()))
print('Seu nome em minusculo: {}'.format(nome.lower()))#letras minusculas
print('Seu nome tem {} letras'.format(len(nome)
                                      - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome e {}, ele tem {} letras'
      .format(separa[0], len(separa[0])))

#separa está retirando so espaços e colocando em uma lista.
#separa[0] esta selecionando o 1º nome, e o len fazendo a contagem.
