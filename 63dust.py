# 63dust.py by Naty Tsegai, and assisted by George Mo

import math
import sys
import gzip
import mcb185
import dogma


def calculate_entropy(a, c, g, t):
	total = a + c + g + t
	pa = a / total
	pc = c / total
	pg = g / total
	pt = t / total
	
	entropy = 0
	if a != 0: entropy += pa * math.log2(pa)
	if c != 0: entropy += pc * math.log2(pc)
	if g != 0: entropy += pg * math.log2(pg)
	if t != 0: entropy += pt * math.log2(pt)
	return -entropy




file_path = sys.argv[1]
w = int(sys.argv[2])
entropy_threshold = float(sys.argv[3])


for defline, seq in mcb185.read_fasta(path):

	print(f'>{defline}')

	sequence = list(seq)
	
	for i in range(len(seq) +1 - w):
		s = seq[i:i+w]
		A = s.count('A')
		C = s.count('C')
		G = s.count('G')
		T = s.count('T')
		entropy_s = calculate_entropy(A, C, G, T)
		if entropy_s < entropy_threshold:
			for j in range(i, i + w):
				sequence[j] = 'N'
		
	joined_seq = ''.join(sequence)

	for i in range(0, len(joined_seq), 60):
		line = joined_seq[i:i+60]
		print(line)
