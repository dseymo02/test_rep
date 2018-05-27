def readSolution(solutions,size):
	str = input()
	solutions  = str.split() 
	assert len(solutions) == size
	return solutions

def readAnswers(answers,size):
	str = input()
	answers = str.split()
	studentnumber = answers.pop(0)
	return studentnumber, answers

def main():

	size = 6
	solutions = []
	answers = []
	terminate = 999
	solutions = readSolution(solutions,size)
	print(solutions)
	finished = False
	while not finished:
		studentnumber, answers = readAnswers(answers,size)
		print(studentnumber, answers)
		if studentnumber == "999":
			finished = True
			print(studentnumber)
	print(finished)
	
if __name__ == "__main__":
	main()