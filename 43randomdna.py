import random

nts = 'ACGT'
for i in range(3):
	print(f'>seq-{i+1}', sep='')
	for j in range(random.randint(40, 60)):
		print(random.choice(nts), end='')
	print()