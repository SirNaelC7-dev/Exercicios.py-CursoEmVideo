def notas(*n, sit=None):
	"""
	-> Análise e situação para notas de alunos.
	:param n: inserção de notas dos alunos
	:param sit: valor opcional que avalia a situação de acordo com média
	:return: dicionário contendo todas as infomrações 
	"""
	r = {}
	r['total'] = len(n)
	r['maior'] = max(n)
	r['menor'] = min(n)
	r['media'] = sum(n)/len(n)
	if sit:
		if r['media'] >= 7:
			r['situacao'] = 'Boa'
		elif r['media'] >= 5:
			r['situacao'] = 'Razoável'
		else:
			r['situacao'] = 'Ruim'
	return r

resp = notas(7, 4.5, 6.76, 10, sit=True)
#print(resp)
help(notas)
