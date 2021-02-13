from math import pow
peso=float(input('Insira sua massa corpórea: '))
altura=float(input('Insira sua altura em metros: '))
qaltura=pow(altura,2)
imc=peso/qaltura
if imc<18.5:
	print('Você está abaixo do peso!')
elif imc>18.5 and imc<=25:
	print('Peso ideal')
elif imc>25 and imc<=30:
	print('Sobrepeso')
elif imc>30 and imc<=40:
	print('Obesidade')
else:
	print('Obesidade mórbida')
