opcao='S'
t=contpcm=0#gasto total, quantidade de produtos +1000
pb=''#produto + barato
while opcao=='S':
	n=str(input('Nome do Produto: '))
	p=float(input('Preço do Produto: '))
	t+=p
	if p>1000:
		contpcm+=1
	pb=n
	if n<pb:
		pb=n
	opcao=str(input('Deseja Continuar?[S/N]')).strip().upper()
print('O gasto total foi de R${:.2f}\n{} produtos custam mais de R$ 1000,00\nO produto mais barato é {}'.format(t, contpcm, pb))
