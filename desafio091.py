from random import randint
from operator import itemgetter
from time import sleep
resultados = {'jogador_1': randint(1, 6),
			  'jogador_2': randint(1, 6),
			  'jogador_3': randint(1, 6),
			  'jogador_4': randint(1, 6)}
rank = dict()	  
print('          Valores Sorteados\n'+'__'*20)			  
for k, v in resultados.items():
	print(f'{k} tem pontuação {v} no dado')
	sleep(2)
rank = sorted(resultados.items(), key=itemgetter(1), reverse = True)
print('__'*20)
for i, v in enumerate(rank):
	print(f'{i+1} lugar: {v[0]} com {v[1]}.')
