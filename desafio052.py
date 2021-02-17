num=int(input('Digite um número para checar se é primo: '))
numdivisores=0
for p in range(1,num+1):
	if num%p==0:
		numdivisores+=1
if numdivisores==2:
	print('O número digitado é PRIMO')
else:
	print('O número digitado NÃO é PRIMO')
