listanums = list()
while True:
	n = int(input('Digite o número: '))
	if n not in listanums:
		listanums.append(n)
		print('Valor adicionado a lista!')
	else:
		print('Valor duplicado, não foi adicionado.')
	opcao = str(input('Quer continuar adicionando?[S/N]'))
	if opcao in 'Nn':
		break
print('--'*30)
listanums.sort()
print('Os valores digitados foram: \n{}'.format(listanums))
