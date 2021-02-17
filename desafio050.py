soma=0
for nums in range(1,7):
	nums=int(input('Digite o {}° número: '.format(nums)))
	if nums%2==0:
		soma+=nums
print(soma)
		
