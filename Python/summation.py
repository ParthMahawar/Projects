x = 0.5
sums = 0
for i in range(53):
	sums += x
	x /= 2
	print(sums)
	print('x', x)