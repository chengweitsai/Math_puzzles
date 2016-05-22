"""
C(5,2) = 5! / (3! * 2!), but it may ovreflow in sone condition. so we need to change the way 
we compute combination
there is another way to compute combination:
C(n,r) = C(n-1, r-1) + C(n-1, r-1)
C(n,1) = n
C(n, n) = 1
please refer the above equation to compute C(40,10) and C(990,33)

while you compute C(990,33), python will hit the limit of recursion or consume too much time. 
you must find some way to fix these problem.
"""

def combination(n, r):
	assert(n>=r)
	if (r==1):
		return n
	if (n == r):
		return 1
	return combination(n-1, r) + combination(n-1, r-1)

"""resualt = combination(40, 10) 
print " C(40,10) = " +str( resualt)"""



h, w =40, 10
Matrix = [[0 for x in range(w+1)] for y in range(h+1)]
for i in range(1,h+1):
	for j in range(1,w+1):
		if (j==1): 
			Matrix[i][j] = i
		elif (i==j ): 
			Matrix[i][j] = 1
		else:
			Matrix[i][j] = Matrix[i-1][j] + Matrix[i-1][j-1]

print  " C(40,10) = " +str( Matrix[h][w] ) 

h, w =990, 33
Matrix = [[0 for x in range(w+1)] for y in range(h+1)]
for i in range(1,h+1):
	for j in range(1,w+1):
		if (j==1): 
			Matrix[i][j] = i
		elif (i==j ): 
			Matrix[i][j] = 1
		else:
			Matrix[i][j] = Matrix[i-1][j] + Matrix[i-1][j-1]

print  " C(990,33) = " +str( Matrix[h][w] ) 