add = 1
currentno = 0.0

for i in range(1,1000000000,2):
	if add == 1:
		add = 0
		currentno += (4.0/i)
	else:
		add = 1
		currentno -= (4.0/i)

print currentno