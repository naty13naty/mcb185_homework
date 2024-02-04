# a program that reports the first 10 Fibonacci numbers 
#by Natnael Tsegai co-authored with Khalid 

def fib_seq(n):
	limit = n
	n1 = 0 
	n2 = 1
	for n in range(0, n):
		n3 = n2 + n1
		n1 = n2
		n2 = n3
		print(n1)

		
#testing the program
print(fib_seq(10))
		
