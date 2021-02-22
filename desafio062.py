print('Gerador de PA\n')
ptermo=int(input('Digite o primeiro termo da PA: '))
razao=int(input('Digite a razão da PA: '))
termo=ptermo
cont=1
total=0
mais=10
while mais!=0:
	total+=mais
	while cont<=total:
		print('{} ->'.format(termo),end='')
		termo+=razao
		cont+=1
	print('PAUSA')
	mais=int(input('Quantos termos à mais deseja exibir?'))	
print('FIM') 
