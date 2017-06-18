import random
x = 1
y = 2
z = 3

check = 0

while x != y or x != z or y!=z:
	x = random.randint(1,1000)
	y = random.randint(1,1000)
	z = random.randint(1,1000)
	print x,y,z
	check += 1
	print check, 'iterations'
