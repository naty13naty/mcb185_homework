#  Estimating pi using the Nilakantha series by Natnael Tsegai Co-authored with Khalid Saif

def nilakantha(n):
	initial = 3
	sign = 1
	for i in range(1, n + 1):
		formula = 4 / ((2*n) * (2*n - 1) * (2*n - 2))
		result = initial + (formula * sign)
		sign = -1 * sign
	return result
print(nilakantha(10000))	
	