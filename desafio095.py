time = list()
jogador = dict()
while True:
	jogador.clear()
	jogador['nome'] = str(input('Nome: '))
	jogador['qpartidas'] = int(input('Quantidade de partidas jogadas: '))

	jogador['tgols'] = 0
	for p in range(1, jogador['qpartidas']+1):
		gols = int(input(f'Gols feitos na {p}° partida: '))
		jogador['tgols'] += gols
	jogador['aprov'] = jogador['tgols']/jogador['qpartidas']
	time.append(jogador.copy())
	opcao = str(input('Deseja adicionar mais jogadores[S/N]'))
	if opcao in 'Nn':
		break
for j in time:
	print(j)
