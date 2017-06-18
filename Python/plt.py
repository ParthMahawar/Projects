import matplotlib.pyplot as plt

nums = list(range(-4000,4001))

funcs = list()
funcs2 = list()

for i in nums:
	i = i/4
	if i != 0:
		funcs.append(((i+1)/i))
		funcs2.append((i/i+1))
	else:
		funcs.append(0)
		funcs2.append(0)

plt.plot(nums,funcs,'r')
plt.plot(nums,funcs2,'g')
plt.show()

print(nums)