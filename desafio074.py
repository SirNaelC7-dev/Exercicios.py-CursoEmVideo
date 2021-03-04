from random import randint
menornum = 0
maiornum = 0
alnums = [0, 0 ,0 ,0 ,0]

for a in range(0,5):
	aleat = randint(0,10)
	alnums[a] = aleat
menornum = alnums[0]
maiornum = alnums[0] 

for b in range(1, len(alnums)):
	if menornum > alnums[b]:
		menornum = alnums[b]
	if maiornum < alnums[b]:
		maiornum = alnums[b]
		
print(f'Os números gerados foram: {alnums}')
print(f'O maior número gerado foi:{maiornum}')
print(f'O menor número gerado foi:{menornum} ')
