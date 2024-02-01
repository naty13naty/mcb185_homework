i = 0
while True:
	i = i + 1
	print ('hey', i)
	if i == 3: break
	
i = 0
while i < 3:
	print (i)
	i = i + 3
print ('final value of i is', i)

for i in range(0, 8, 2):
	print (i)
	
for i in range(5):
	print (i)
	
for char in 'hello':
	print(char)
	
seq = 'GATCC'
for nt in seq:
	print(nt)

for nt1 in 'AGCT':
	for nt2 in 'AGCT':
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')		
	
nts = 'ACGT'
for nt1 in nt2: 
	if nt1 == nt2: print(nt1, nt2, '+1')
	else:          print(nt1, nt2, '-1')
	
limit = 4
for i in range(0, limit):
	for j in range(i+1, limit):
	 print(i+1, j+1)

limit = 10
for i in range(0, limit):
	for j in range(i+1, limit):
	 print('hey', i, j+1)
