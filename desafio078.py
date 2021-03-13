lista=[]
for i in range(0,5):
	lista.append([int(input(f'Digite o {i+1}º número: '))])
posmenor = 0
posmaior = 0
menornum = lista[0]
maiornum = lista[0]

for j in range(0, len(lista)):
	if menornum > lista[j]:
		menornum = lista[j]
		posmenor = j
	if maiornum < lista[j]:
		maiornum = lista[j]
		posmaior = j
print(f'O {menornum} é o menor número e está na posição: {posmenor}')
print(f'O {maiornum} é o maior número e está na posição: {posmaior}')	
