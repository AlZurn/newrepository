a = [9,3,5,8,3,7,4,2]
b = 2
count = 1
for i in a:
	if i == b:
		print('есть в листе')
		break
	elif b + count  == i or b - count == i:
		print(i,'AMENA POKRY')
	else:
		count +=1 
		for i in a:
			if b + count == i or b - count == i:
				print(i,'AMENA POKRY ELI') 
			# break


