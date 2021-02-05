fr=str(input('Digite sua frase:\n')).strip().upper()
print('Sua frase possui {} letras A'.format(fr.count('A')))
print('A posição da primeira letra A fica no espaço: {}'.format(fr.find('A')+1))
print('A posição da última letra A fica no espaço: {}'.format(fr.rfind('A')+1))


