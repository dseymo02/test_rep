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

	size = 6
	solutions = []
	answers = []
	solutions = readSolution(solutions,size)
	studentnumber, answers = readAnswers(answers,size)
	print(studentnumber, answers)
	
if __name__ == "__main__":
	main()