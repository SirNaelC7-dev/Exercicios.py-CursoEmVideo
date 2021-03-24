boletim = list()
while True:
	nome = str(input('Nome: '))
	nota1 = float(input('1º Nota: '))
	nota2 = float(input('2º Nota: '))
	media = (nota1+nota2)/2
	boletim.append([nome,[nota1, nota2],media])
	opcao = str(input('Deseja continuar?[S/N] '))
	if opcao in 'Nn':
		break
print('_' *50)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>10}')
print('_' *50)				
for i, a in enumerate(boletim):
	print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
	
while True:
	escolha = int(input('Deseja exibir notas dd qual aluno(999 finaliza)? '))
	if escolha == 999:
		print('Finalizando...')
		break
	if escolha<=len(boletim)-1:
		print(f'Notas de {boletim[escolha][0]} são {boletim[escolha][1]}')
print('Finalizado')
