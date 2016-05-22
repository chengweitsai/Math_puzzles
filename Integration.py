def anonymous(x):
	return x**2 + 1
 
def integrate(fun, start, end):
	step = 0.1
	intercept = start
	area = 0
	tmp=0
	while intercept < end:
		intercept += step
		tmp = ( fun(intercept)+fun(intercept-step) ) / 2 
		area += step * fun(intercept)
	return area

print(integrate(anonymous, 0, 10)) 