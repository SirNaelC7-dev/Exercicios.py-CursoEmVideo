num=int(input('Digite um número inteiro para converter: '))
print('''OPÇÕES:
1 - base 2
2 - base 8
3 - base 16
''')

opcao=int(input('Base Escolhida?'))
if opcao==1:
	print('O número convertido para binário = {}'.format(bin(num)))
elif opcao==2:
	print('O número convertido para octal = {}'.format(oct(num)))
elif opcao==3:
	print('O número convertido para hexadecimal = {}'.format(hex(num)))
