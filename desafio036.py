pcasa=float(input('Digite o preço da casa: '))
salario=float(input('Digite seu salário: '))
tpg=int(input('Em quantos anos pretende pagar? '))
prestacao=pcasa/(tpg*12)
print('O valor da prestação = {:.2f}'.format(prestacao))
if prestacao > ((salario/100)*30)+salario:
	print('Seu empréstimo foi reprovado!')
else:
	print('Seu empréstimo será aprovado!')


