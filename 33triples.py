# Pythagorean triples by Natnael Tsegai Co-authored with Khalid Saif

for a in range(1, 100):
	for b in range(a, 100):
		c = (a**2 + b**2)**0.5
		if c == c // 1:	print('triples', a, b, c)
				
	