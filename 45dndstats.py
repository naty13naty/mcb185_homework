# A program that determines the average stat value using the various rules below:

"""
3D6: roll 3 six-sided dice
3D6r1: roll 3 six-sided dice, but re-roll any 1s
3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
4D6d1: roll 4 six-sided dice, dropping the lowest die roll
"""

import random

rolls = 10000
total = 0

#3D6: roll 3 six-sided dice
for i in range(rolls):
	for j in range(3):
		roll = random.randint(1, 6)
		total += roll
print(total / rolls)

	
#3DR1: roll 3 six-sided dice, but re-roll any 1s
rolls = 10000
total = 0

for i in range(rolls):
	for j in range(3):
		roll = random.randint(1, 6)
		if roll == 1: roll = random.randint(1, 6)
		total += roll
print(total / rolls)


rolls = 100000
total = 0

for i in range(rolls):
	score = 0
	for j in range(3):
		r1 = random.randint(1, 6)
		r2 = random.randint(1, 6)
		if r1 > r2: 
			score += r1
		else:
			score += r2
	total += score
print(total / rolls)


#4D6d1: roll 4 six-sided dice, dropping the lowest die roll
rolls = 10000
total = 0

for i in range(rolls):
	score = 0
	r1 = random.randint(1, 6)
	r2 = random.randint(1, 6)
	r3 = random.randint(1, 6)
	r4 = random.randint(1, 6)
	if r1 <= r2 and r1 <= r3 and r1 <= r4:
		score += r2 + r3 + r4
	elif r2 <= r1 and r2 <= r3 and r2 <= r4:
		score += r1 + r3 + r4
	elif r3 <= r1 and r3 <= r2 and r3 <= r4:
		score += r1 + r2 + r4
	elif r4 <= r1 and r4 <= r2 and r4 <= r3:
		score += r1 + r2 + r3
	total += score
print(total / rolls)

