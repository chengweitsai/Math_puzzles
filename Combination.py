def combination(n, r):
	assert(n>=r)
	if (r==1):
		return n
	if (n == r):
		return 1
	return combination(n-1, r) + combination(n-1, r-1)

MatrixA = [[0 for x in range(10)] for y in range(40)] 

print combination(20, 5)
