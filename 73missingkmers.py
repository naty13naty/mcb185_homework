# 73missingkmer.py by Naty Tsegai 
import sys
import mcb185
import itertools
import gzip

fasta = sys.argv[1]

for k in range(1, len(seq)):
	print('checking', k)
	
	kcount = {}
	for defline, seq in mcb185.read_fasta(fasta):
		for i in range(len(seq) -k +1):
			kmer = seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
		
	if len(kcount.keys()) == 4**k: continue
	
	#report missing kmer
	for ktup in itertools.product('ACGT', repeat=k):
		kmer = ''.join(ktup)
		print(kmer)
		
