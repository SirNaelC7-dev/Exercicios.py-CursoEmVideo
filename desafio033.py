num1=int(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))
num3=int(input('Digite o terceiro número: '))
if num1<num2<num3:
	print('A ordem crescente = {}, {}, {} '.format(num1, num2, num3))
	print('O menor número é o {}'.format(num1))
	print('O maior número é o {}'.format(num3))
elif num1<num3<num2:
	print('A ordem crescente = {}, {}, {} '.format(num1, num3, num2))
	print('O menor número é o {}'.format(num1))
	print('O maior número é o {}'.format(num2))
elif num2<num1<num3:
	print('A ordem crescente = {}, {}, {} '.format(num2, num1, num3))
	print('O menor número é o {}'.format(num2))
	print('O maior número é o {}'.format(num3))
elif num2<num3<num1:
	print('A ordem crescente = {}, {}, {} '.format(num2, num3, num1))
	print('O menor número é o {}'.format(num2))
	print('O maior número é o {}'.format(num1))
elif num3<num1<num2:
	print('A ordem crescente = {}, {}, {} '.format(num3, num1, num2))
	print('O menor número é o {}'.format(num3))
	print('O maior número é o {}'.format(num2))
elif num3<num2<num1:
	print('A ordem crescente = {}, {}, {} '.format(num3, num2, num1))
	print('O menor número é o {}'.format(num3))
	print('O maior número é o {}'.format(num1))
		

		
