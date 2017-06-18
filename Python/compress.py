#inp = raw_input('Filename: ')
#		file = open(inp, 'r')
text = ''
runlist = []
counter = 1

output = ''

for char in range(len(text)):
	if text[char] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
		runlist.append(text[char])
		print runlist

		for character in range(len(runlist)):
			print character
			if runlist[character] == text[char]:
				pass
			else:
				txt = text[char-1] + str(len(runlist[0:char]))
				print character
				output += txt
				runlist = []
				break
				print output
		print runlist

	if len(runlist) > 0:
		if runlist[0] == text[-1]:
			counter += 1
			print counter, 'counter'

if counter>1:
	output += text[-1] + str(counter)
print output
