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
	
# question 2
def search(str,lst,size):
	if str in lst:
		return lst.index(str)
	else: 
		return -1

#question 3 

def check(g,n):
	if g < n:
		return "Too low"
	elif g > n:
		return "Too high"
	else:
		return "Correct"
	
def readSolution(solutions,size):
	str = input()
	solutions  = str.split() 
	assert len(solutions) == size
	return solutions

def readAnswers(answers,size):
	str = input()
	answers = str.split()
	studentnumber = answers.pop(0)
	assert len(answers) == size
	return studentnumber, answers
		
def main():
	'''
	# question 1a programme
	n = 20
	print([i for i in fibseq(n)])
	
	# question 1b programme
	l = 2000
	print([i for i in fibseqlimit(l)])
	
	# question 3
	number = randint(0,99)
	guess = 0
	finished = False
	count = 0
	guess = int(input("Guess a number between 0 and 99: "))
	while not finished:
		count += 1
		if guess < number:
			guess = int(input("Too low, Guess again: "))
		elif guess > number:
			guess = int(input("To high, Guess again: "))
		else:
			finished = True
	print("Correct. It took you ",count, " guesses")
	'''
	size = 6
	solutions = []
	answers = []
	solutions = readSolution(solutions,size)
	studentnumber, answers = readAnswers(answers,size)
	print(studentnumber, answers)
	
if __name__ == "__main__":
	main()

