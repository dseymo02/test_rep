def fib(n):
	''' function to print out fib sequence '''
	if n in [1,0]:
		return 1
	else:
		return fib(n-1) + fib(n-2)