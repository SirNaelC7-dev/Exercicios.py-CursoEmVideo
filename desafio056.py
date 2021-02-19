nomehv=''
idadehv=0
mm20=0
somaidade=0
for p in range(1,5):
	print('------ {}° Pessoa ------'.format(p))
	nome=str(input('NOME: ')).strip()
	idade=int(input('IDADE: '))
	sexo=str(input('SEXO [M/F]: ')).strip()
	somaidade+=idade
	if p==1 and sexo in 'Mm':
		nomehv=nome
		idadehv=idade
	if sexo in 'Mm' and idade>idadehv:
		idadehv=idade
		nomehv=nome
	if sexo in 'Ff' and idade<20:
		mm20+=1
medidade=somaidade / 4
print('A média de idade do grupo é de {} anos'.format(medidade))
print('O homem mais velho tem {} anos e se chama {}'.format(idadehv,nomehv))
print('No grupo são {} mulheres com menos de 20 anos'.format(mm20))



