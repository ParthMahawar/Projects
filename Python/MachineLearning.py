import random

file = open('words.txt', 'r')
file = file.read()

wordlist = file.split('\n')

print(wordlist)
print(len(wordlist))

userInput = raw_input('Enter text')
userInput.strip()
userInput.lower()

userWords = userInput.split(' ')

for word in userWords:
	if word not in wordlist:
		wordlist.append(word)

wordScores = dict()

for word in wordlist:
	wordScores[word] = 0

for word in userWords:
	if word not in wordScores:
		wordScores[word] = 0
	wordScores[word] += 1

scorelist = []

for key, value in wordScores.iteritems():
	scorelist.append(value)

scorelist.sort()

iterlst = []

for num in scorelist:
	if num not in iterlst:
		iterlst.append(num)
	else:
		del num

scorelist = iterlst[:]

newScores = {}

for score in scorelist:
	scorewords = []
	words = wordlist[:]
	for word in words:
		if wordScores[word] == score:
			scorewords.append(word)
	newScores[score] = scorewords

	print random.choice(scorewords), score