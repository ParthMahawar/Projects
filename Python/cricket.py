import random

score = 0
ball = 0
run = 0
wickets = 0
centuries = 0
innscore = 0
scores = []

while wickets != 1000000:
	run = random.randint(1, 6)
	ball += 1
	if run != 5:
		score += run
		innscore += run
		print 'Scored', run, 'runs'
	else:
		print 'You scored', score, 'runs off', ball, 'balls.'
		wickets += 1
		scores.append(innscore)
		if innscore > 99:
			centuries += 1
		innscore = 0

print 'Strike Rate:', float(score)/ball*100
print 'Average:', float(score)/wickets
print 'Centuries:', centuries
print 'HS: ', max(scores)