# question 2
def search(str,lst,size):
	pos = 0
	result = -1
	for s in lst:
		if s == str:
			result = pos
		else: 
			pos += 1
	return result
