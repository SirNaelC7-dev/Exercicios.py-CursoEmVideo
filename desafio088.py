from random import randint
palpite = []
palpites = []
qjogos = int(input('Quantos palpites de jogos deseja gerar?')) 
while qjogos != 0:
	cont=0
	while True:
		n = randint(1, 60)
		if n not in palpite:
			palpite.append(n)
			cont += 1
			if cont >= 6:
				break
	palpites.append(palpite[:])
	palpite.clear()
	qjogos-=1
	
print(palpites)
