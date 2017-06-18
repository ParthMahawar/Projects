import random

current = 0
num = int(raw_input('What is the losing number '))
starter = raw_input('Would you like to start? (y/n)')
stps = 3

if starter == 'y':
	entry = 5
	while not(0 < entry < 4):
		entry = int(raw_input())
	current += entry

def game(number, curNum, steps):
	idealNum = (number-1)%(steps + 1)

	while idealNum <= curNum:
		idealNum += steps + 1
	if (idealNum - curNum) <= steps:
		curNum = idealNum
	else:
		curNum += random.randint(1, steps)

	return [number, curNum, steps]

while current < num:
	#print(player1(num, current, stps))
	num, current, stps = game(num, current, stps)
	print(current, 'current')
	if current < num:
		entry = 5
		while not(0 < entry < 4):
			entry = int(raw_input())
		current += entry