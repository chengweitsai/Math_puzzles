"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23
Please find the sum of all the multiples of 3 or 5 below 1000."""

import math 

a = 3
b = 5
N = 1000
li = []

for i in range(1, N):
	if( i % a == 0 or i % b == 0):
		li.append(i)

resault = 0
for e in li:
	resault += e

print li
print "Answer :\n" + str(resault)

