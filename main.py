def fib(n):
	''' function to print out fib numbers'''
	if n in [1,0]:
		return 1
	else:
		return fib(n-1) + fib(n-2)

def fibseq(n):
	seq = []
	for i in range(0,n+1):
		seq.append(fib(i))
	return seq
	
def main():
	n = 20
	print([i for i in fibseq(n)])
	
if __name__ == "__main__":
	main()
