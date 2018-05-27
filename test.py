from main import *
import pytest

def testexample():
	g = 4
	h = 5
	assert g + h == 9

def testfib():
	n = 20
	assert fib(n) == "0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765"