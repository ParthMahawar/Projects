tempkey = int(input('Enter Key: '))
base = int(input('Enter Base: '))
text = input('Text to be decrypted: ')

def basechange(num, bas):
	nums = []
	fin = 0
	for i in range(1000):
		nums.append(0)
	tempoutput = []
	output = ''

	for i in range(len(nums)):
		nums[i] = 0
		while bas**(len(nums)-i) <= num:
			num -= bas**(len(nums)-i)
			nums[i] += 1
		tempoutput.append(nums[i])
	tempoutput.append(num)

	for i in tempoutput:
		output += str(i)

	return str(int(output))

key = basechange(tempkey, base)
textlist = list(text.upper())

letternumber = {'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 'K': 11, 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14, 'Q': 17, 'P': 16, 'S': 19, 'R': 18, 'U': 21, 'T': 20, 'W': 23, 'V': 22, 'Y': 25, 'X': 24, 'Z': 26, '1' : 27, '2': 28, '3': 29, '4': 30, '5': 31, '6': 32, '7': 33, '8': 34, '9': 35, '0': 36, ' ':37}

numlist = []
for i in textlist:
	numlist.append(letternumber.get(i, i))
def check(a, b):
	while a>=b:
		a-=b
	return a

for i in range(len(numlist)):
	x = i
	if numlist[x] in [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]:
		try:
			numlist[x] = int(numlist[x]) - int(key[i])
		except:
			i = check(i, len(key))
			try:
				numlist[x] = int(numlist[x]) - int(key[i])
			except:
				pass

inverse = dict()

for keys in letternumber:
	inverse[letternumber[keys]] = keys

outputlist = list()

for i in numlist:
	try:
		while i <= 0:
			i += 37
	except:
		pass
	outputlist.append(inverse.get(i, i))

output =''

for i in outputlist:
	output += str(i)

print('DECRYPTED TEXT:', output)
