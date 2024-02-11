#A program that simulates death saves with the probability one dies, stabilizes, or revives?

import random

death = 0
stablize= 0
revive = 0
trials = 1000
for i in range(trials):
	success = 0
	failure = 0
	while success < 3 and failure < 3:
		roll = random.randint(1, 20)
		if roll == 1:
			failure += 2
		elif 1 < roll < 10:
			failure += 1
		elif 10 <= roll < 20:
			success += 1
		elif roll == 20:
			revive += 1
			break
	if failure >= 3:
		death += 1
	if success == 3:
		stablize += 1
prob_death = death / trials
prob_stable = stablize / trials
prob_revive = revive/ trials
print('die', prob_death) 
print('stablize', prob_stable)
print('revive', prob_revive)