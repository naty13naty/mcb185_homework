#  Poisson probability of k events by Natnael Tsegai Co-authored with Khalid Saif

import math

def factorial(n):								#Factorial function
		if n == 0: return 1
		fac = 1
		for i in range(1, n + 1):
			fac = fac * i
		return fac

def poisson(n, k):
	if n < 0 or n == 0 or k == 0: 
		return 0
	else:
		return math.e**-n * (n**k / factorial(k))

print(poisson(9, 5))
print(poisson(5, 10))
