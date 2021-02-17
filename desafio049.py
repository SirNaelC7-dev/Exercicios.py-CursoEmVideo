qtabuada=int(input('Qual tabuada você quer? '))
for tabuada in range(1,10):
	operacao=qtabuada*tabuada
	print('{} x {} = {}'.format(qtabuada, tabuada, operacao))
