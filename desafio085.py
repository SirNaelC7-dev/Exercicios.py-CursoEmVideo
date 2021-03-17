nums = list()
pares = []
impares = []
for i in range(0,6):
	num = int(input(f'Digite o {i+1}º número: '))
	if num % 2 == 0:
		pares.append(num)
	else:
		impares.append(num)
pares.sort()
impares.sort()
nums.append(pares[:])
nums.append(impares[:])

print(nums)
