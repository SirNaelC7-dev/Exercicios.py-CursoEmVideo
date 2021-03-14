vnums = list()
for v in range(0,5):
	nums = int(input('Digite um número: '))
	if v == 0:
		vnums.append(nums)
	elif nums > vnums[-1]:
		vnums.append(nums)
	else:
		pos = 0
		while pos < len(vnums):
			if nums <= vnums[pos]:
				vnums.insert(pos, nums)
				break
			pos+=1 
print('--'*30)
print(vnums)	
