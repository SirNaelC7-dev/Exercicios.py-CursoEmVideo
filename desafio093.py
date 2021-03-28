ger = dict()
ger['nome'] = str(input('Nome: '))
ger['qpartidas'] = int(input('Partidas Jogadas: '))
ger['tgols'] = 0
for i in range(1, ger['qpartidas']+1):
	ger['golsp'] = int(input(f'Gols feitos na {i}º partida: '))
	ger['tgols'] += ger['golsp']
ger['aproveitamento'] = ger['tgols'] / ger['qpartidas']    

del(ger['golsp'])
for i, j in ger.items():
	print(f'{i} {j}')
