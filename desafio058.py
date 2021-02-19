from random import choice
nums=[0,1,2,3,4,5,6,7,8,9,10]
chplayer=00
chpc=choice(nums)
numtent=0
while chplayer!=chpc:
	chplayer=int(input('Digite seu palpite: '))
	if chplayer==chpc:
		print('O jogador acertou! ')
		print('Número de tentativas: {}'.format(numtent))
	if chplayer!=chpc:
		print('O jogador errou\nTente Novamente')
	numtent+=1
