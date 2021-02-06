from random import choice
nums=[0,1,2,3,4,5]
escolhapc=choice(nums)
escolhauser=int(input('Advinhe o número escolhido pela máquina entre 0 - 5\nDigite o número escolhido: '))
print('A escolha da máquina foi: {}'.format(escolhapc))
if escolhapc==escolhauser:
	print('O usuário venceu, PARABÉNS!!!')
else:
	print('A máquina venceu, KKKKKK')


