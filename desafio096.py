def area():
	print('CALCULE A AREA DO SEU TERRENO')
	print('_' * 25)
	c = float(input('Cumprimento(m): '))
	l = float(input('Largura(m): '))
	a = c*l
	print('A área do seu terreno é de {:.2f} metros quadrados'.format(a))
	
area()
