"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23
Please find the sum of all the multiples of 3 or 5 below 1000."""

m = int(1000/3)
n = int(1000/5)

li = []

for i in range(0, m):
	for j in range(0, n):
		li.append(3**i * 5**j)

resault = 0

for e in li:
	resault = resault + e

print "Answer :\n" + str(resault)
