#question 3 

def check(g,n):
	if g < n:
		return "Too low"
	elif g > n:
		return "Too high"
	else:
		return "Correct"

def main():
	
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
	
if __name__ == "__main__":
	main()