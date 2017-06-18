import matplotlib.pyplot as plt

nums = []
nums2 = []
nums3 = []

for i in range(-400,400):
	nums.append((i/4)**2)
	nums2.append(i/4)
	nums3.append((i/4)**3)

plt.plot(nums2,nums,'r')

gz =[]

for i in nums3:
	gz.append('a')
	i = str(i)

print(nums2,'\n',nums3)
plt.hist(nums3)
plt.show()