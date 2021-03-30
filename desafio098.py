from time import sleep
def contador(inicio, fim, passo):
	if inicio < fim:
		print(f'Contagem Crescente: {inicio} -> {fim-1} : {passo}')
		print('_'*35)
		for i in range(inicio, fim, passo):
			sleep(1)
			print(i)
		print('_'*35)
	if inicio > fim:
		print(f'Contagem Decrescente: {inicio} -> {fim} : {passo}')
		print('_'*35)
		for i in range(inicio, fim, -passo):
			sleep(1)
			print(i)
		print('_'*35)
			
contador(1, 11, 1)
contador(10, 0, 2)

