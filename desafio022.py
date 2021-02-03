nome=str(input('Digite seu nome completo: '))
print('Letras Maiúsculas: {}\n Letras Minúsculas: {}\nQtd. Letras Sem Espaços: {}\n'.format(nome.upper(),nome.lower(),len(nome.replace(' ',''))))
