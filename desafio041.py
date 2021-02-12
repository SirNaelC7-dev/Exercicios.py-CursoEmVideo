idade=int(input('Digite sua idade: '))
if idade<=9:
	print('Você pertence a categoria MIRIM! ')
elif idade>9 and idade<=14:
	print('Você pertence a categoria INFANTIL! ')
elif idade>14 and idade<=19:
	print('Você pertence a categoria JÚNIOR! ')
elif idade==20:
	print('Você pertence a categoria SÊNIOR! ')
else:
	print('Você pertence a categoria MASTER! ')
