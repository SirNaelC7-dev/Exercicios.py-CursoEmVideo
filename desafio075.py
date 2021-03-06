num = (int(input('Digite o 1º número: ')),
       int(input('Digite o 2º número: ')),
       int(input('Digite o 3º número: ')),
       int(input('Digite o 4º número: ')))
print('Você digitou os valores: {}'.format(num))
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
	print(f'O valor 3 apareceu na posição: {num.index(3)+1}')
else:
	print('O número 3 não foi digitado')
print('Os valores pares digitados foram', end'')
for n in num:
	if n%2==0:
		print(n, end='')
