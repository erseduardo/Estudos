n = int(input('Digite um número: '))
print('Escolha uma das bases para converter:'
      '[1] = para binário '
      '[2] = para octal'
      '[3] = para hexadecimal')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(n, bin(opcao)))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(n,oct(opcao)))
elif opcao == 3:
    print('{} convertido para hexadecimal e igual a {}'.format(n, hex(opcao)))
else:
    print('Você digitou uma opcão invalida: ')