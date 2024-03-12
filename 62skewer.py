import dogma
import sys
import gzip
import mcb185

file_path = sys.argv[1]
w = int(sys.argv[2])


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	g = seq[0:w].count('G')
	c = seq[0:w].count('C')		
	for i in range(len(seq) - w):
		off = seq[i]
		on = seq[i+w]
	
		if   off == 'C': c -= 1
		elif off == 'G': g -= 1
	
		if   on == 'C': c += 1
		elif on == 'G': g += 1
	
	
		gc_comp = (c + g)/w
		if(g+c) > 0: skew = (g-c)/(g+c)
		else:        skew = 0
	
print(i, gc_comp, skew)

"""

for size 10
real	0m3.413s
user	0m3.349s
sys     0m0.034s

for size 100
real	0m3.576s
user	0m3.480s
sys	    0m0.045s

for size 1000
real	0m3.768s
user	0m3.682s
sys	    0m0.042s

"""
