num=int(input('Digite um número para fatorar: '))
contador=num
vfin=1
print('Calculando {}!: '.format(num),end='')
while contador > 0:
	print('{}'.format(contador), end='')
	print(' x ' if contador>1 else ' = ', end ='')
	vfin*=contador
	contador-=1 
print(vfin)
