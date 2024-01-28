# a program that returns Kyte-Doolittle hydrophobicity value for an amino acid letter 
# By Naty Tsegai

def kyte_doolittle_hydrophobicity(aa):
	if aa == 'A': return 1.81
	if aa == 'L': return 4.92		
	if aa == 'V': return 4.04
	if aa == 'P': return 4.04
	if aa == 'F': return 2.98
	if aa == 'M': return 2.35
	if aa == 'W': return 2.33
	if aa == 'C': return 1.28
	if aa == 'G': return 0.94
	if aa == 'Y': return -0.14
	if aa == 'T': return -2.57
	if aa == 'S': return -3.40
	if aa == 'H': return -4.66
	if aa == 'Q': return -5.54
	if aa == 'A': return -5.55
	if aa == 'N': return -6.64
	if aa == 'E': return -6.81
	if aa == 'D': return -8.72
	if aa == 'R': return -14.9
	else: return None
	
#testing the program
print(kyte_doolittle_hydrophobicity('F'))
print(kyte_doolittle_hydrophobicity('M'))