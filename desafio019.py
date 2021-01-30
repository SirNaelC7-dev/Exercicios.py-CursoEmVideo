from random import choice
ap1=input('Digite o nome do primeiro aluno: ')
ap2=input('Digite o nome do segundo aluno: ')
ap3=input('Digite o nome do terceiro aluno: ')
ap4=input('Digite o nome do quarto aluno: ')
lista = [ap1,ap2,ap3,ap4]
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
