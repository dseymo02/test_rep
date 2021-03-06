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

def score(solutions, answers, size):
	score = 0
	for i in range(0,size):
		if answers[i] == solutions[i]:
			score += 1
		elif answers[i] != solutions[i]:
			score -= 1
	return score


def main():

	size = 6
	solutions = []
	answers = []
	results = []
	terminate = 999
	solutions = readSolution(solutions,size)
	finished = False
	while not finished:
		studentnumber, answers = readAnswers(answers,size)
		if studentnumber == "999":
			finished = True
			break
		results.append((studentnumber,score(solutions,answers,size)))
	for i in results:
		print(i[0]," ",i[1], " marks")

if __name__ == "__main__":
	main()