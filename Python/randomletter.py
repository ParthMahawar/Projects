import random

Input = input('Enter text (Letters, Commas,Numbers, And Periods: ')
counter = 0

Output = ''

lst = []

for i in range(len(Input)):
	lst.append('')

while Output != Input:
	for i in range(len(lst)):
		if lst[i] != Input[i]:
			lst[i] = random.choice(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,. '))
		Output += lst[i]
	print('Iteration', counter, ':', Output)
	if lst == list(Input):
		break
	counter += 1
	Output = ''

print('That took', counter, 'iterations')
