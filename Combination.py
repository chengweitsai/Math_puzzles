def combination(n, r):
	assert(n>=r)
	if (r==1):
		return n
	if (n == r):
		return 1
	return combination(n-1, r) + combination(n-1, r-1)

MatrixA = [[0 for x in range(10)] for y in range(40)] 
"""resualt = combination(40, 10) 
print " C(40,10) = " +str( resualt)"""


resualt = combination(990, 33) 
print " C(990,33) = " +str( resualt)