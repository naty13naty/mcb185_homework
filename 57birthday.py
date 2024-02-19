import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

success = 0

for i in range(trials):
    calendar = []

    for j in range(people):
        day = random.randint(0, days - 1)

        if day in calendar:
            success += 1
            break

        calendar.append(day)

probability = success / trials * 100
print(probability)