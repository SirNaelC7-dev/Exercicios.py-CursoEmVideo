pessoas = list()
pessoa = dict()
somai = media = 0
while True:
	pessoa.clear()
	pessoa['nome'] = str(input('Nome: '))
	pessoa['idade'] = int(input('Idade: '))
	somai+=pessoa['idade']
	while True:
		pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
		if pessoa['sexo'] in 'MF':
			break
		print('ERRO, Atribua somente M/F')
	pessoas.append(pessoa.copy())
	opcao = str(input('Deseja adicionar mais pessoas[S/N]?')).upper()[0]
	if opcao in 'N':
		break
	media = somai/ len(pessoas)
print(f'{len(pessoas)} foram cadastradas')
print(f'{media} é a média de idade do grupo ')
for p in range(0,len(pessoas)):
	if pessoas[2] == 'F':
		print(p)
	

