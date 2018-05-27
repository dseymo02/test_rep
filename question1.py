from random import randint

# question 1a
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

# question 1b
	
def fibseqlimit(l):
	finished = False
	seq = []
	n = 0
	while not finished:
		fibn = fib(n)
		n += 1
		if fibn < l:
			seq.append(fibn)
		else:
			finished = True
	return seq
		
def main():
	# question 1a programme
	n = 20
	print([i for i in fibseq(n)])
	
	# question 1b programme
	l = 2000
	print([i for i in fibseqlimit(l)])
	
	
if __name__ == "__main__":
	main()

