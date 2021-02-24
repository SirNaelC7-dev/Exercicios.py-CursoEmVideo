opcao = 'S'
s = c = maiornum = menornum = 0#soma,contador
while opcao in 'Ss':
	num = int(input('Digite um número: '))
	s += num
	c += 1
	if c == 1:
		maiornum = menornum = num
	else:
		if menornum > num:
			menornum = num
		if maiornum < num:
			maiornum = num
	opcao = str(input('Quer continuar digitando? [S/N]')).upper().strip()
m = s/c#media
print('O maior valor foi {} e o menor foi {}'.format(maiornum,menornum))
print('Você digitou {} números, a média foi {}'.format(c,m))
