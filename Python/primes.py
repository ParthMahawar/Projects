primes = [2]
for number in range(3, 50, 2):
	if str(number).endswith('5') or str(number).endswith('0'):
		continue
	for prime in primes:
		if float(number)/float(prime) < prime:
			primes.append(number)
			print(number)
			break
		elif number%prime == 0:
			break

print(primes)

twinprimes = []
for item in range(len(primes)):
	if primes[item] - primes[item-1] == 2:
		twinprimes.append((primes[item-1], primes[item]))
print('----------------------------------------------')
print(twinprimes)
print('----------------------------------------------')
print(sum(primes))