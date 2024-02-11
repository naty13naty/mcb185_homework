#A program that estimates pi using Monte Carlo by Naty Tsegai

import math
import random

inside_circle = 0
total = 0
while True:
	x = random.random()
	y = random.random()						
	if math.sqrt(x**2 + y**2) < 1: 
		inside_circle += 1
	total += 1
	pi = 4* (inside_circle / total)
	print(pi)											#^C stops the loop