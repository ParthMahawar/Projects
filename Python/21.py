import random

numbersToTry = 100
winList = []
wins = None
plr = 1

current = 0
num = 20
stps = 3

def game(number, curNum, steps, player):
	player = player%2
	idealNum = number%(steps + 1)

	while idealNum <= curNum:
		idealNum += steps + 1
		print(idealNum, 'calc')
	print(idealNum, 'i')
	if (idealNum - curNum) <= steps:
		curNum = idealNum
	else:
		curNum += random.randint(1, steps)
	if player == 1 and curNum == number:
		win = True
	else:
		win = False
	return [number, curNum, steps, win]

while current < num:
	#print(player1(num, current, stps))
	num, current, stps, wins = game(num, current, stps, plr)
	plr += 1
	print(current, 'current')
	if current < num:
		num, current, stps, wins = game(num, current, stps, plr)
		plr += 1
		print(current, 'current')

print wins

for integer in range(1, numbersToTry):
	wins = None
	plr = 1
	current = 0
	num = integer
	stps = 3
	while current < num:
		#print(player1(num, current, stps))
		num, current, stps, wins = game(num, current, stps, plr)
		plr += 1
		print(current, 'current')
		if current < num:
			num, current, stps, wins = game(num, current, stps, plr)
			plr += 1
			print(current, 'current')

	print wins
	winList.append(wins)

print winList