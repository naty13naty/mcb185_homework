import math
import sys

def invert_number(n):
	n = (n * -1)
	return n
print(invert_number(4))

def area_of_sq(x):
	A = x**2
	return A
print(area_of_sq(5))

def area_of_rec(l, w):
	A = ((2*l) + (2*w))
	return A
print(area_of_rec(2, 3))

def area_of_cir(r):
	A = math.pi * r**2
	return A
print(area_of_cir(6))

def vol_of_sphere(r):
	V = 4/3 * math.pi * r**3
	return V
print(vol_of_sphere(5))

def convert_temp(F):
	C = (F - 32) * 5/9
	return C
print(convert_temp(98.6))

def convert_V(mph):
	kph = mph * 1.60934 
	return kph
print(convert_V(60))

def DNA_conc(OD260, dilution_factor): 
	DNA_conc = (50 * OD260 * dilution_factor)  
	return DNA_conc
print(DNA_conc(0.65, 50))

def dist_bn_pts(x1, y1, x2, y2):
	distance = math.sqrt((x2**2 - x1**2) + (y2**2 - y1**2))
	return distance
print(dist_bn_pts(3, 5, 2, 7))

def mid_bn_pts(x1, y1, x2, y2):
	midway = ((x1 + x2)/2, (y1 + y2)/2)
	return midway
print(mid_bn_pts(2, 6, 4, 8))

def is_integer(n): 
	if n == n // 1: 
		return 'integer'
	else:
		return 'not integer'
print(is_integer(8.5))

def odd_number(n):
	if n % 2 != 0: 
		return 'odd number'
	elif n % 2 == 0: 
		return 'even number'
	
print(odd_number(3))
print(odd_number(8))

def valid_prob(n):	
#valid probability is a number between 0 and 1, and the sum of the number equals 1	
	if 0 < n <= 1: 
		return 'valid probablity'
	else:
		return 'not valid probability'
print(valid_prob(0.5))
print(valid_prob(-0.2))

def molecular_wt_dna(letter): 	#letters: A, C, G, T)
	if letter == 'A':
		return 331.2
	if letter == 'C': 
		return 307.2
	if letter == 'G':
		return 347.2
	if letter == 'T': 
		return 322.2
	
	else:
		return 'none'
print(molecular_wt_dna('T'))

def dna_complement(base_pair):		#base pairs: A==T, C==G
	if base_pair == 'A':
		return 'T'
	if base_pair == 'C':
		return 'G'
	if base_pair == 'T':
		return 'A'
	if base_pair == 'G':
		return 'C'
	
print(dna_complement('C'))

