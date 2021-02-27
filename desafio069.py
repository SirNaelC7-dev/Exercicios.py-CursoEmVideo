sexo = ''
idade = 0
opcao = 'Ss'
mdd = hc = mm = 0#maiores de dezoito, homens cadastrados, mulheres com menos de 20 anos
while opcao in 'Ss':
	idade = int(input('Digite sua idade: '))
	sexo = str(input('Digite seu sexo[M/F]: ')).upper().strip()
	if idade > 18:
		mdd += 1
	if sexo == 'M':
		hc += 1
	if sexo == 'F' and idade<20:
		mm+=1
	opcao=str(input('Deseja continuar?[Ss/Nn]'))
print('{} pessoas são maiores de 18 anos\n{} homens foram cadastrados\n{} mulheres tem menos que 20 anos'.format(mdd,hc,mm))	
