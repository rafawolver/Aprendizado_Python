# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = int(input('Me diga qual nota você tirou em Matemática: '))
n2 = int(input('Me diga qual nota você tirou em Portugues: '))
s = n1+n2
r = s/2
print('A sua media de notas em relação a Matemática e Portugues é {}!'.format(r))