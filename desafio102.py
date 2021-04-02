def fatorial(n, show = 0):
	c = n
	vfin = 1
	if show == None or show == False or show == 0:
		for i in range(1, n):
			c *= i
		print(c)
	else:
		if show == True:
			print('Calculando {}!: '.format(n),end='')
			while c > 0:
				print('{}'.format(c), end='')
				print(' x ' if c>1 else ' = ', end ='')
				vfin*=c
				c-=1 
			print(vfin)

fatorial(5, True)		
		
		
	
