"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ? """

import math

def factorize(li, N, D):
	if(N==D):
		li.append(D)
		return 
	if ( N%D == 0):
		li.append(D)
		factorize(li, N/D, D)
	else:
		factorize(li, N, D+1)


def check_prime(N):
	limit = int (math.sqrt(N) )
	for e in range(2,limit):
		if(N%e ==0): return False
	return True

li = [];
factorize(li, 13195, 2)
print "13195 = ", li;

Num = 600851475143
limit = int (math.sqrt(Num) )
print limit
ui=[]
MatrixA = [0 for x in range(limit)] 
for i in range(2, limit):
	if(Num % i == 0): 
		MatrixA[i] =1
		ui.append(i)

print ui
print "next find the biggest prime in ui, it is the answer"
resault=0
for u in ui:
	if(check_prime(u)): resault = u
print "The biggest Prime of", Num, "is ", resault