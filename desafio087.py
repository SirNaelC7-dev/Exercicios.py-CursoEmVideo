matrix = [[0, 0, 0],
		  [0, 0, 0],
		  [0, 0, 0]]
soma = somatc = maiorv = 0
for i in range(0, 3):
	for j in range(0, 3):
		 matrix[i][j] = int(input(f'Posição[{i}][{j}]:'))
		 if matrix[i][j] % 2 == 0:
			 soma += matrix[i][j]
for j in range(0, 3):
	for k in range(2, 3):
		somatc += matrix[j][k]

for l in range(1, 2):
	for m in range(0, 3):
		if matrix[l][m] > maiorv:
			maiorv = matrix[l][m]

print(matrix)	
print(f'A soma dos elementos pares na matrix é: {soma}')
print(f'A soma dos elementos da terceira coluna é: {somatc}')
print(f'O maior valor da segunda linha é: {maiorv}')
