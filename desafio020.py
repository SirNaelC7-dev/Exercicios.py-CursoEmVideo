from random import shuffle
pa1=input('Primeiro aluno: ')
pa2=input('Segundo aluno: ')
pa3=input('Terceiro aluno: ')
pa4=input('Quarto aluno: ')
lista=[pa1,pa2,pa3,pa4]
shuffle(lista)
print('A ordem da lista será:')
print(lista)
