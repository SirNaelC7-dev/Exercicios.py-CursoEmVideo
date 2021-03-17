line1 = []
line2 = []
line3 = []
matrix = [line1,
		  line2, 
		  line3]
for i in range(0, 3):
	for j in range(0, 3):
		if i == 0:
			line1.append(int(input(f'Posição{[i],[j]}: ')))
		elif i == 1:
			line2.append(int(input(f'Posição{[i],[j]}: ')))
		elif i == 2:
			line3.append(int(input(f'Posição{[i],[j]}: ')))

print(matrix)	
