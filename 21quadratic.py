#quadratic formula solver by Naty Tsegai

import math
import sys

def quadratic_formula(a, b, c):		 	#ax**2 +bx + c
	if b**2 - 4*a*c >= 0:  
		x1 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a 	#x1 = x intercept 1
		x2 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a 	#x2 = x intercept 2
		return x1, x2
	
	elif b**2 - 4*a*c < 0: print('no intercepts')
		
	
	
print(quadratic_formula(1, 6, 3))
print(quadratic_formula(1, 3, 6))