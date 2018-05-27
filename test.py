from main import *
import pytest

# question 1a tests
def testexample():
	g = 4
	h = 5
	assert g + h == 9

def testfib():
	n = 19
	assert fib(n) == 6765

def testfibseq():
	n = 19
	assert fibseq(n) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
# question 1b tests	
def testfibseqlimit(): 
	l = 2000
	assert fibseqlimit(l) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,233, 377, 610, 987, 1597]

# question 2 tests
def testsearch():
	s = "hello"
	s1 = "let"
	l = ["do","it","now","hello","aim","fire"]
	size = len(l)
	assert search(s,l,size) == 3
	assert search(s,l,size) == -1
	
