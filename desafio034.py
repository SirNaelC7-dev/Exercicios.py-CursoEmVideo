salario=float(input('Digite seu salário: '))
if salario<=1250:
	print('Seu salário reajustado = {}'.format(((salario/100)*15)+salario))
elif salario>1250:
	print('Seu salário reajustado = {}'.format(((salario/100)*10)+salario))
