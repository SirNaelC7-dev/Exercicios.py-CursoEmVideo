from datetime import date
today=date.today()
cont=0
cont1=0
for pessoas in range(1,8):
	pessoas=int(input('Digite seu ano de nascimento: '))
	if (pessoas-today.year)<-20:
		cont+=1
	else:
		cont1+=1
print('{} pessoas atingiram a maioridade'.format(cont))
print('{} pessoas não atingiram a maioridade'.format(cont1))
		


