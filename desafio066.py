n=s=c=0#número,soma,contador
while True:
	n=int(input('Digite um número: '))
	if n==999:
		break
	s+=n
	c+=1
print('{} números foram digitados, a soma dos números é {}'.format(c,s))
	
