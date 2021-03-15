expressao = str(input('Digite a expressão:'))
pilha = list()
for carac in expressao:
	if carac == '(':
		pilha.append('(')
	elif carac == ')':
		if len(pilha) > 0:
			pilha.pop()
		else:
			pilha.append(')')
			break
if len(pilha) == 0:
	print('Sua expressão está válida')
else:
	print('Sua expressão está inválida')
