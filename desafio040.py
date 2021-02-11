nota1=float(input('Insira a primeira nota: '))
nota2=float(input('Insira a segunda nota: '))
media=(nota1+nota2)/2
if media<5.00:
	print('Reprovado')
elif media>=5.00 and media<=6.9:
	print('Recuperação')
else:
	print('Aprovado')
