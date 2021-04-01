from random import randint
nums = list()
def sorteio():
	for i in range(0, 5):
		num = randint(0, 10)
		nums.append(num)
	print(f'Os números sorteados foram: {nums}')
def somaPar():
	somap = 0
	for n in nums:
		if n%2==0:
			somap+=n
	print(f'A soma dos números pares dos valores sorteados foi: {somap}')
	

sorteio()
somaPar()	
