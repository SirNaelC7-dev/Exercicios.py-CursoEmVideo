nums=[0,0,0,0]
for a in range(0,len(nums)):
	nums[a] = int(input('Digite o {}° número: '.format(a+1)))

print(nums) 
print('O número 9 aparece: {} vezes'.format(nums.count(9)))

