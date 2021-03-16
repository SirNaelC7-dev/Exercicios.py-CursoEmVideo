dados = []
aux = []
maiorp = menorp = 0
while True:
	aux.append(str(input('Nome: ')))
	aux.append(float(input('Peso: ')))
	if len(dados) == 0:
		menorp = maiorp = aux[1]
	else:
		if aux[1] < menorp:
			menorp = aux[1]
		if aux[1] > maiorp:
			maiorp = aux[1]
	dados.append(aux[:])
	aux.clear()
	opcao = str(input('Deseja continuar?[S/N]'))
	if opcao in 'Nn':
		break
print('--'*30)	
print(f'{len(dados)} pessoas foram cadastradas')
print('--'*30)	
print('As pessoas com o maior peso cadastrado foram:')
for n in dados:
	if n[1] == maiorp:
		print(f'[{n[0]}]')

print('--'*30)	
print('As pessoas com o menor peso cadastrado foram:')
for n in dados:
	if n[1] == menorp:
		print(f'[{n[0]}]')	
	
