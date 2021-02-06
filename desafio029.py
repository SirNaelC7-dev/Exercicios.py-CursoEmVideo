velocidade=int(input('Digite sua velocidade em Km/h:\n'))
if velocidade>80:
	print('Você foi multado')
	print('O valor da sua multa é: R${},00'.format((velocidade-80)*7))
else:
	print('Você não excedeu o limite de velocidade')
