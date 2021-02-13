precop=float(input('Insira o preço do produto: '))
print('''Formas de Pagamento:
1 - À vista: Espécie/Cheque
2 - Parcelado no Cartão de Crédito
''')
opcao=int(input('Qual a forma de pagamento? '))
if opcao==1:
	print('O preço do produto de acordo com a forma de pagamento é: {:.2f} R$'.format(((precop/100)*10)-precop))
elif opcao==2:
	qparcelas=int(input('Em quantas vezes deseja dividir o preço do produto? '))
	if qparcelas==1:
		print('O preço do produto é: {:.2f} R$'.format(((precop/100)*5)-precop))
	elif qparcelas==2:
		print('O preço do produto é: {:.2f} R$'.format(precop))
	elif qparcelas==3:
		print('O preço do produto é: {:.2f} R$'.format(((precop/100)*20)+precop))
	else:
		print('O preço do produto é: {:.2f} R$'.format(((precop/100)*20)+precop))

