# N choose Kl Tsegai Co-authored with Khalid Saif


def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac
		
def n_chs_k(n, k):
	if k < 0 or k > n or n < 0:
		return 0
	return factorial(n) / (factorial(k) * factorial(n - k))
	
print(n_chs_k(10, 5))
print(n_chs_k(50, 2))

