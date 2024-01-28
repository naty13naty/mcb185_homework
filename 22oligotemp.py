# a program that returns the oligo melting temperature by Naty Tsegai

import math
import sys

def oligo_temp(A, C, G, T):			# A, C, G, T are nt sequences
	nt_seq = A + C + G + T
	
	if nt_seq > 13:
		Tm = 64.9 + (41*(G + C - 16.4) / (nt_seq))
		return Tm			# Tm is in celsius
		
	elif nt_seq <= 13: 
		Tm = (A + T)*2 + (G + C)*4
		return Tm			#Tm is in celsius	
			
			
#testing the program
print(oligo_temp(10, 8, 7, 8))
print(oligo_temp(3, 3, 2, 2))