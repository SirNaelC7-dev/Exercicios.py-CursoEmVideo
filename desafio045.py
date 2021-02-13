from random import choice
jokenpo=['Pedra', 'Papel', 'Tesoura']
print('Vamos jogar JOKENPÔ! \n')
escolhamaq=choice(jokenpo)
escolhahum=input('Pedra, Papel ou Tesoura? ').capitalize().strip()
if escolhahum==escolhamaq:
	print('O desafiante e a máquina empataram!')
	print('A máquina jogou: {}'.format(escolhamaq))
	print('O desafiante jogou: {}'.format(escolhahum))
	
elif escolhahum=='Pedra' and escolhamaq=='Tesoura' or escolhahum=='Papel' and escolhamaq=='Pedra' or escolhahum=='Pedra' and escolhamaq=='Tesoura':
	print('O desafiante venceu a máquina! ')
	print('A máquina jogou: {}'.format(escolhamaq))
	print('O desafiante jogou: {}'.format(escolhahum))

elif escolhamaq=='Pedra' and escolhahum=='Tesoura' or escolhamaq=='Papel' and escolhahum=='Pedra' or escolhamaq=='Pedra' and escolhahum=='Tesoura':
	print('A máquina venceu o desafiante! ')
	print('A máquina jogou: {}'.format(escolhamaq))
	print('O desafiante jogou: {}'.format(escolhahum))
