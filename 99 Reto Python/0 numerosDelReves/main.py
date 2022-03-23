"""
This script generates all valid palindrome numbers from a given range.

It has been coded in Geany FOSS IDE.
"""

def generatePalindromes(initial, end):
	"""
	Expects integers where initial must be lower than end.
	
	Returns a list with another list of palindromes and an interget which
	is the amount of valid ones, plus a validation string.
	"""
	
	inputRange = end - initial
	
	# Checks if the range is valid
	if inputRange < 1:
		return [[], 0, "Invalid Range"]
		
	
	# Main loop logic
	validPalindromes = []
	countPalindromes = 0
	
	for i in range(inputRange +1):
		isItPalindrome = checkIfPalindrome(initial + i)
		
		if isItPalindrome == True:
			validPalindromes.append(initial + i)
			countPalindromes += 1
			
	return [validPalindromes, countPalindromes, "Valid Range"]

def checkIfPalindrome(integer):
	"""
	Checks if a number qualifies as palindrome and returns boolean.
	"""
	
	# As integers are non subscriptable, we must transform it into string
	# and then into list for easy manipulation
	
	listedInteger = []
	
	for index in str(integer):
		listedInteger.append(index)
		
	# Palindromes read the same backwards, so we need to reverse our input
	
	reverseIndex = len(str(integer)) -1
	reverseInteger = []
	
	for index in str(integer):
		reverseInteger.append(str(integer)[reverseIndex])
		reverseIndex -= 1
		
	# Performing comparison and returning
	
	if listedInteger == reverseInteger:
		return True
	else:
		return False
