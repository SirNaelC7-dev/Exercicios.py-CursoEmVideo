palavras=('programar', 'treinar', 'competir', 'desafio',
'competiçoes', 'evoluir', 'estudar', 'praticar','python')
for a in palavras:
	print(f'\nNa palavra {a.upper()} tem as vogais: ', end='')
	for vogais in a:
		if vogais in 'aeiou':
			print(vogais.upper(),end=' ')
			
			
		
	
