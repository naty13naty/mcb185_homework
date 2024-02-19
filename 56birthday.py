import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])


success = 0
for i in range(trials):
	birthdays = [random.randint(1, days) for j in range(people)]
	shared_birthday = False
	for n in range(len(birthdays) - 1):
		birthday = birthdays[n]
		if birthday in birthdays[n+1:]:
			shared_birthday = True
			break
			
	if shared_birthday:
			success += 1
			
probability = (success / trials) * 100
print(probability)	
