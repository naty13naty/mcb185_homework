import gzip
import sys
import math

gffpath = sys.argv[1]
feature = sys.argv[2]

def gen_count(vals):
	total = 0
	for val in vals: total += val
	return total 

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi

def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)

def stdv(vals):
	total = 0
	mean_val = mean(vals)
	for val in vals:
		total += (val - int(mean_val))**2
	return math.sqrt(total / len(vals))
	
def median(vals):
	vals.sort()
	if len(vals) % 2!= 0:             #if the count is odd
		med = int(len(vals) / 2)
		return med
	else: 								#if the count is even
		med1 = int(len(vals) / 2) - 1
		med2 = int(len(vals) / 2)
		return int((vals[med1] + vals[med2]) / 2)

lengths = []	
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		words = line.split()
		if words[2] != feature: continue
		beg = int(words[3])
		end = int(words[4])
		lengths.append(end - beg + 1)
		
	gen_count  = (len(lengths))
	gen_mini, gen_maxi = (minmax(lengths))
	gen_mean       = mean(lengths)
	gen_stdv       = stdv(lengths)
	gen_median     = median(lengths)
	
print(f'count: {gen_count}')
print(f'min: {gen_mini}')
print(f'max: {gen_maxi}')	
print(f'mean: {gen_mean}')
print(f'stdv: {gen_stdv}')
print(f'median: {gen_median}')
		