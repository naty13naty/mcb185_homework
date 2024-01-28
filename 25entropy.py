# a program that returns the Shannon entropy for nucleotide counts a, c, g, t
# by Naty Tsegai

import math
import sys

def shannon_entropy(a, c, g, t):
	total_count = a + c + g + t
	if total_count == 0: return 0
	
	pa = a / total_count
	pc = c / total_count
	pg = g / total_count
	pt = t / total_count
	
	entropy = 0
	if a != 0: entropy = entropy + a * math.log2(pa)
	if c != 0: entropy = entropy + c * math.log2(pc)
	if g != 0: entropy = entropy + g * math.log2(pg)
	if t != 0: entropy = entropy + t * math.log2(pt)
	return entropy * -1
	
	
# testing the program
print(shannon_entropy(19, 11, 12, 14))
print(shannon_entropy(0, 8, 9, 6))