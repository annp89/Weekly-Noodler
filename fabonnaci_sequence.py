from collections import defaultdict
 
fib_call_count = defaultdict(int)
 
def fib(n):
	fib_call_count[n] += 1
	if n == 0:
	    return 0
	elif n == 1:
	    return 1
	else:
	    return fib(n - 1) + fib (n - 2)

def fab(n): 
	fib(n)
	for i in xrange(1, n):
		print fib_call_count[i]
