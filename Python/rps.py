import random
options = ['rock', 'paper', 'scissors']
winlose = {'scissors':'rock', 'rock':'paper', 'paper':'scissors'}

win = 0
lose = 0

while True:
	x = raw_input('Choose:\n1. Rock\n2. Paper\n3. Scissors\n')

	try:
		x = int(x)
	except:
		pass
	
	if x==1: x='rock'
	elif x==2: x='paper'
	else: x='scissors'

	print('You chose ' + x)

	options.append(winlose[x])

	y = random.choice(options)

	print('Opponent chose ' + y)

	if x == y:
		print('Tie')
	elif winlose[x] == y:
		print('YOU LOSE')
		lose += 1
	else:
		print('YOU WIN')
		win += 1

	print('--------------\n'+str(options)+'\n----------------')

	print(win, lose)