def maior(*nums):
	cont = maior = 0
	print(f'Analisando os Valores:{nums}')
	for n in nums:
		if cont == 0:
			maior = n
		else:
			if n > maior:
				maior = n
		cont+=1
	
	print(f'O maior valor dos dados informados foi: {maior}')
	print('__'*30)

maior(2,7,0,5,2,100,8,6,7)
maior(3,4,7,55,3,89,43,46,342)
