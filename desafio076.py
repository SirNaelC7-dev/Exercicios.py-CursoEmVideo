prod = ('produto 1', 1,
		'Produto 2', 2, 
		'Produto 3', 3, 
		'Produto 4', 4, 
		'Produto 5', 5, 
		'Produto 6', 6)
print('-'*40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-'*40)
for pos in range(0, len(prod)):
	if pos%2==0:
		print(f'{prod[pos]:.<30}', end='')
	else:
		print(f'{prod[pos]:>7.2f}')
print('-'*40)
