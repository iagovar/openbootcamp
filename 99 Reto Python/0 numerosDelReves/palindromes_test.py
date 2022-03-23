"""
Unit testing palindromes using Pytest

Learning from: https://www.tutorialspoint.com/pytest/pytest_tutorial.pdf

Remember:
 - Testing function names must start by test*
"""

import pytest
import random
from main import *



def testValidRanges():
	# Ranges must be valid, ie end always > initial
	
	for initial in range(1000):
		end = random.randint(0, 1000)	
		fnResult = generatePalindromes(initial, end)
		if initial < end:
			assert fnResult[2] == "Valid Range", "Fails with initial:" + str(initial) + ", end:" + str(end)
		else:
			assert fnResult[2] == "Invalid Range", "Fails with initial:" + str(initial) + ", end:" + str(end)

def testUpperLowerLimits():
	# Includes both upper and lower limits
	assert generatePalindromes(100, 101) == [[101], 1, "Valid Range"], "Fails to include upper limit"
	assert generatePalindromes(101, 102) == [[101], 1, "Valid Range"], "Fails to include lower limit"
	
def testSomePalindromes():
	# Testing some palindromes
	
	palindromes = [109901, 9999999, 1, 44, 1001001, 400004, 313]
	
	for element in palindromes:
		fnResult = generatePalindromes(element, element+1)
		assert fnResult[0][0] == element, "failed at " + str(fnResult)
