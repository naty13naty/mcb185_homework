#Fizz Buzz program by Naty Tsegai

limit = (100)
for i in range(1, limit):
	if(i % 3 == 0): print(i, 'fizz')
	if(i % 5 == 0): print(i, 'buzz')
	if(i % 3 == 0 and i % 5 == 0): print(i, 'fizzbuzz')
	else: print(i)