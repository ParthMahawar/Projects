import matplotlib.pyplot as plt

thisthing = dict()

asg = range(1,26)
let = range(1,26)
let = list(let)

for num,cha in zip(asg, let):
	thisthing[cha] = num

print(thisthing)

plt.bar(list(thisthing.keys()),list(thisthing.values()))
plt.show()