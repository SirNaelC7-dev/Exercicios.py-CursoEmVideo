n=0
while True:
	n=int(input('Qual tabuada deseja exibir?'))
	if n < 0:
		break
	for i in range(1,10):
		print('{} x {} = {}'.format(n, i, n*i))
print('FIM')
