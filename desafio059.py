opcao=0
while opcao!=5:
	num1=int(input('Digite um número: '))
	num2=int(input('Digite um número: '))
	print('[1] - Somar \n[2] - Multiplicar \n[3] - Maior \n[4] - Novos Números \n[5] - Encerrar')
	opcao=int(input('Qual operação deseja realizar? '))
	if opcao == 1:
		print('Soma = {}'.format(num1+num2))
	if opcao == 2:
		print('Multiplicação = {}'.format(num1*num2))
	if opcao == 3:
		if num1>num2:
			print('O número maior é: {}'.format(num1))
		else:
			print('O número maior é: {}'.format(num2))
	if opcao == 4:
		opcao=0
	if opcao == 5:
		opcao=5
