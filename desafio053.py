frase=str(input('Digite algo para checar se é PALÍNDROMO:\n')).lower().strip().replace(' ', '')
frase1=''
for a in range(len(frase)-1,-1,-1):
	frase1+=frase[a:a+1]
	
if frase==frase1:
	print('A frase é um PALÍNDROMO')
else:
	print('A frase NÃO é um PALÍNDROMO')
