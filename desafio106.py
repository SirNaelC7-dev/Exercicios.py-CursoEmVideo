def pyHelp(msg):
	while True:
		m = 'SISTEMA DE AJUDA PyHELP'
		print('_'* len(msg))
		print(m)
		print('_'* len(msg))
		fb = str(input(msg)).strip().lower()
		print(f'Acessando o manual: {fb}')
		print(help(fb))
		if fb == 'fim':
			break
		
f = pyHelp('Função ou Biblioteca > ')
