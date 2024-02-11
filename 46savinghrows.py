#A program that simulates saving throws against DCs of 5, 10, and 15

import random

trials = 1000										

#DC = difficulty class/ Advantage
print('DC\tadv')									
for i in range(5, 16, 5):							
	print(i, end='\t')
	success = 0
	for j in range(trials):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		if r1 > r2: 
			a = r1
		else: 
			a = r2
		if a >= i:
			success += 1
	print(success / trials)
print('\n')

#DC = difficulty class/ Disadvantage
print('DC\tdisadv')
for i in range(5, 16, 5):							
	print(i, end='\t')
	success = 0
	for j in range(trials):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		if r1 < r2:
			a = r1
		else:
			a = r2
		if a >= i:
			success += 1
	print(success / trials)
print('\n')

#DC = difficulty class/ Normal
print('DC\tnormal')
for i in range(5, 16, 5):							
	print(i, end='\t')
	success = 0
	for j in range(trials):
		r = random.randint(1, 20)
		if r >= i:
			success += 1
	print(success / trials)