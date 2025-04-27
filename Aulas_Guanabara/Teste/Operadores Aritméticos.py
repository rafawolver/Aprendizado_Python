## nome = input('Qual e o seu nome? ')
## print('Prazer em te conhecer {:20}!'.format(nome))

## nome = input('Qual e o seu nome? ')
## print('Prazer em te conhecer {:>20}!'.format(nome))

## nome = input('Qual e o seu nome? ')
## print('Prazer em te conhecer {:<20}!'.format(nome))

## nome = input('Qual e o seu nome? ')
## print('Prazer em te conhecer {:^20}!'.format(nome))

## nome = input('Qual e o seu nome? ')
## print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
rd = n1%n2
sub = n1-n2
p = n1**n2
print('A soma vale {},\n a multiplicação vale {},\n a divisão vale {:.3f} '.format(s, m, d), end='>>> ') ## (,end='') Junta o print com o debaixo! (\n) Quebra a linha
print ('a divisão inteira vale {}, o resto da divisão vale {}, a subtração vale {}, a potencia é {}'.format(di, rd, sub, p))
