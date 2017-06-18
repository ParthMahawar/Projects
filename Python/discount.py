import matplotlib.pyplot as plt
percentages = []
hundredvals = []

for i in range(401):
	percentages.append(i/4)

for i in percentages:
	hundredvals.append(((100-i)/100)*i)

print(hundredvals)

plt.plot(percentages, hundredvals)
plt.show()