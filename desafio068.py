from random import choice
print('VAMOS JOGAR PAR OU ÍMPAR\n')
opcao=''
cond=''
escolha=[1,2]
chooseuser=choosepc=soma=cont=0
while True:
	opcao=str(input('Você escolhe[PAR/IMPAR]:')).strip().upper()
	chooseuser=int(input('Digite um número:'))
	choosepc=choice(escolha)
	soma=chooseuser+choosepc
	if soma%2==0:
		cond='PAR'
	else:
		cond='IMPAR'
	if cond==opcao:
		print('O Jogador Venceu!')
		cont+=1
	else:
		print('O Computador Ganhou!\nMais Sorte da Próxima Vez!')
		break
print('Você Conquistou {} Vitórias Consecutivas, PARABÉNS!!!'.format(cont))

