"""
import random
random.seed(1) # genrates the same random

size = 100
words = []
wordd = {}
for i in range(size):
	token = []
	for j in range(10):
		token.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	token = ''.join(token)
	#words.append(token)
	#words[token] = True
	wordd[token] = True
	
print(words)	

for i in range(1000):
	if 'MYNAMEISNATY' in words:
		print('found')


import mcb185
import sys

kcount = {}
k = 3

for aas in itertools.product('ACDEFGHIJKLMNOPQRTSUVWXYZ'):
	kmer = ''.join(aas)

kcount(kmer) += 1


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] +=1
		
for kmer, n in kcount.items():
	print(kmer,  n)


seq = 'ACTGCGTCGCAGTCAGTCAGTACGTAAACGGT'
w = 10

def gc(s):
	c = ss.count('C')
	g = ss.count('G')
	return((g + c)/len(s))
	
for i in range(len(seq) -w +1):
	ss = seq[i:i+w]
	print(ss, gc(ss))
	
	
	
seq = 'ACTGCGTCGCAGTCAGTCAGTACGTAAACGGT'
w = 5

g = seq[0:w].count('G')
c = seq[0:w].count('C')	
	
for i in range(len(seq) - w):
	off = seq[i]
	on = seq[i+w]
	
	if   off == 'C': c -= 1
	elif off == 'G': g -= 1
	
	if   on == 'C': c += 1
	elif on == 'G': g += 1
	
	
	comp = (c + g)/w
	if(g+c) > 0: skew = (g-c)/(g+c)
	else:         skew = 0
	
	print(i, comp, skew)
	

	
seq = 'ATGATGCGTCGCAGTGACAGTCAGTACGTAAACGGTTA'

for frame in range(3):
	print(frame)
	stop_used = {}
	fseq = seq[frame:]
	for i in range(0, len(fseq) - 3 +1, 3):
		codon = fseq[i:i+3]
		if codon == 'ATG': 
			start = i
			#print('found ATG at', i)
			for j in range(i, len(fseq) -2, 3):
				codon = fseq[j:j+3]
				if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
					stop = j
					if stop not in stop_used:
						print('gene', i, j)
						stop_used[stop] = True
			
"""

d = {}
d = dict()

d = {'dog': 'woof', 'cat': 'meow'}
print(d)

print(d['cat'])

d['pig'] = 'oink'	
print(d)

d['cat'] = 'mew'	
print(d)

del d['cat']	
print(d)

if 'dog' in d: print(d['dog'])

for key in d: print(f'{key} says {d[key]}') 

for k, v in d.items(): print(k, 'says', v) 

for thing in d.items(): print(thing[0], thing[1]) 

print(d.keys(), d.values(), list(d.values()))     

kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):							
	for aa in seq: kd += kdtable[aa]
	return kd/len(seq)

    
import itertools
seq = 'ATGATGCGTCGCAGTGACAGTCAGTACGTAAACGGTTA'
 
for k in range(0, 5):
	print(k)
	kcount = {}	
	for t in itertools.product('ACTG', repeat=k):
		kmer = ''.join(t)
		kcount[kmer] = 0
print(kcount)