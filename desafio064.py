n=s=qd=0
while n!=999:
	n=int(input('Digite um número: '))
	s+=n
	qd+=1
s-=999
qd-=1
print('A soma dos números digitados = {}, {} números foram digitados'.format(s,qd))
