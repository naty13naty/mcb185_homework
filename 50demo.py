"""
seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])
for nt in seq: print(nt, end='')
print()
for i in range(len(seq)):
	print(i, seq[i])
	
s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s, s[::], s[::2], s[::-1])


nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)


tax = ('Homo', 'sapiens', 9606)
print(tax)

print(tax[0])
print(tax[::-1])

def quadratics(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2
x1, x2 = quadratics(5, 6, 1)
print(x1, x2)

nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])
    
for i, nt in enumerate(nts):
    print(i, nt)


names = ('adenine', 'cytosine', 'guanine', 'thymine')
nts = ['A', 'C', 'T', 'G']
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):
    print(nt, name)
for name, nt in zip(names, nts):
	print(name, nt)

 
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
  
nts.append('C')
print(nts)  

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)
    
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)   

items = list()
print(items)
items.append('eggs')   
print(items)

stuff = []
stuff.append(3)
print(stuff)


alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)


text = 'good day	to you'
words = text.split()
print(words)


line = '1.41, 2.72, 3.14'
print(line.split(','))

alph = 'ACDEFGHIKLMPQRSVW'
aas = list(alph)
print(aas)
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
print('index Z?', alph.index('Z'))

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
"""
def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)

def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h
print(entropy([0.2, 0.3, 0.5]))

















   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    