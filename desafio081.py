nums = list()
c = 0
while True:
	n = int(input('Digite um número: '))
	nums.append(n)
	opcao = str(input('Deseja continuar?[S/N]')).upper().strip()
	c+=1
	if opcao == 'N':
		break	
nums.sort(reverse = True)
print(f'{c} números foram digitados')
print(f'A lista em ordem decrescente:\n{nums}')
if 5 in nums:
	print('O valor 5 foi digitado e está presente na lista!')
else:
	print('O número 5 não foi digitado!')
