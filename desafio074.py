from random import randint
alnums=(randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
menornum = alnums[0]
maiornum = alnums[0]

for n in range(0, len(alnums)):
	if menornum > alnums[n]:
		menornum = alnums[n]
	if maiornum < alnums[n]:
		maiornum = alnums[n]
		
print(f'Os números gerados foram: {alnums}')

print(f'O maior número gerado foi: {maiornum}')
print(f'O menor número gerado foi: {menornum} ')

print(f'O maior número gerado foi: {max(alnums)}')
print(f'O menor número gerado foi: {min(alnums)} ')

