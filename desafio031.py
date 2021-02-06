kmviagem=int(input('Digite a distância da sua viagem em Km para calcular o valor da passagem: '))
if kmviagem<=200:
	print('O preço da passagem é: R${:.2f}'.format(kmviagem*0.50))
else:
	print('O preço da passagem é: R${:.2f}'.format(kmviagem*0.45))
