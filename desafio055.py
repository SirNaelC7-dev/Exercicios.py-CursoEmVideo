pmenor=200
pmaior=0
for peso in range(1,6):
	peso=float(input('Digite o peso da {}° pessoa: '.format(peso)))
	if peso>pmaior:
		pmaior=peso
	elif pmenor>peso:
		pmenor=peso
		
print('O maior peso inserido foi: {}'.format(pmaior))
print('O menor peso inserido foi: {}'.format(pmenor))
