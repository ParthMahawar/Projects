def base(num, bas):
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
