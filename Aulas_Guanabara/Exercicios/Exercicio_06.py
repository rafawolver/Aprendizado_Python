# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Me diga um valor: '))
n2 = n1*2
n3 = n1*3
n4 = n1**(1/2)
print('Em relação ao numero {}, posso lhe informar que: \n Seu dobro é: {} \n Seu triplo é: {} \n E sua raiz quadrada é: {}'. format(n1, n2, n3, n4))