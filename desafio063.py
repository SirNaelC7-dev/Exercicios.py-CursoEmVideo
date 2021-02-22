a, b=0, 1
print('Sequência de Fibonacci')
print('-'*22)
qtd=int(input('Quantos termos da sequência deseja exibir? '))
while qtd>0:
	print(a, end=' ')
	a, b=b, a+b
	qtd-=1
print('FIM')
