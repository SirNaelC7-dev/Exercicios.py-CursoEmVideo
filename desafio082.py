nums = list()
pares = list()
impares = list()
opcao = 'S'
pos = 0
while True:
	n = int(input('Digite um número:'))
	nums.append(n)
	opcao = str(input('Deseja continuar?[S/N]')).strip().upper()
	if opcao == 'N':		
		while pos < len(nums):
			if nums[pos] % 2 == 0:
				pares.append(nums[pos])
			else:
				impares.append(nums[pos])
			pos+=1	
		break
nums.sort()
pares.sort()
impares.sort()
print(f'Os números digitados foram:\n{nums}')
print('--'*30)
print(f'Os números pares foram:\n{pares}')
print('--'*30)
print(f'Os números ímpares foram:\n{impares}')
