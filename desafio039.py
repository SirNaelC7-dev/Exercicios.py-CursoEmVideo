from datetime import datetime
now=datetime.now()
anonasc=int(input('Digite seu ano de nascimento: '))
if now.year-anonasc==18:
	print('Você tem a idade obrigatória para se apresentar ao exército')
elif now.year-anonasc<18:
	print('Você não tem a idade obrigatória para se apresentar ao exército')
	print('Só será obrigatório após {} anos'.format((now.year-anonasc)-18))
else:
	print('Sua idade excedeu a idade obrigatória para se apresentar')
	print('Você deveria ter se apresentado há {} anos atrás'.format(abs((now.year-anonasc)-18)))

