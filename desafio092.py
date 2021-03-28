from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome:'))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho: '))
if dados['ctps'] != 0:
	dados['ano_de_contratacao'] = int(input('Ano de Contratação: '))
	dados['salario'] = float(input('Salário: '))
	dados['aposentadoria'] = dados['idade'] + ((dados['ano_de_contratacao'] + 35) - datetime.now().year)
print('__'*20)
for i, j in dados.items():
	print(f'O {i} tem valor {j}')
