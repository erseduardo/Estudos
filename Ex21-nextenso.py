from bdb import Breakpoint

extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
           'onze','doze','treze','quatorze ou catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

#numero = int(input('Digite um número entre 0 e 20: '))
#print(extenso[numero])

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(extenso[num])
        break
    print('Tente novamente: ',end='')
