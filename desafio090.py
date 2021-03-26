dados = {}
resultado = []
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input('Média: '))
if dados['media'] <= 5:
	dados['situacao'] = 'Reprovado'
elif dados['media'] > 5 and dados['media'] <= 6:
	dados['situacao'] = 'Recuperação'
elif dados['media'] >= 7:
	dados['situacao'] = 'Aprovado'
print(dados)
