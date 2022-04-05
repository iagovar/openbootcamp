"""
Sandbox of util functions


Learned:

	COPY and DEEP COPY. Mutable objects asignment don't
	create a new ID reference in Python, specially in
	complex data structures.

	https://docs.python.org/3/library/copy.html
"""

import copy
#from main import STATES, GOAL_STATE

def doesInputValidate(array):
	"""
	Expects an array of arrays (lists of lists in python).
	Checks if it's 3x3, has a 0, and if all numbers can be ordered sequentially.
	Returns boolean.
	"""

	# We'll test for size&format first
	arrayWidth = []
	arrayHeight = len(array)

	try:
		for row in array:
			arrayWidth.append(len(row))
	except:
		return False

	for element in arrayWidth:
		if element != arrayHeight:
			return False

	# Testing for sequential order of all elements
		# We first extract all elements and put em in a list
	sequentialList = []

	for row in array:
		for element in row:
			sequentialList.append(element)

		# Check if it includes a zero
	if 0 not in sequentialList:
		return False

	sequentialList.sort()

		# Then we test against counter so to avoid range and len fn's
	counter = 0
	for element in sequentialList:
		if element != counter:
			return False
		counter += 1

	return True

def getGoalState(array):
	"""
	This fn assumes the array is valid already, and just returns the
	goal state by arranging all numbers sequentially and putting 0
	in the last position.
	"""

	arrayLen = len(array)

	outputArray = []

	# Fill the temp array from 1 to arrayLen * ArrayLen
	for row in range(arrayLen):
		tempRow = []
		lowerLimt = arrayLen * row + 1
		upperLimit = lowerLimt + arrayLen 
		for column in range(lowerLimt, upperLimit):
			tempRow.append(column)
		outputArray.append(tempRow)

	# Changing last integer to 0
	outputArray[arrayLen-1][arrayLen-1] = 0

	return outputArray


def possibleStates(currentState):
	"""
	Given the current state, returns the possible moves as arrays (list of lists)

	Possible states are 4 (move up, move down, move right, move left). Moves that
	are not possible are returned as empty arrays.

	This way, we can discard empty arrays with doesInputValidate() down the line.
	"""

	arrayLen = len(currentState)

	# Getting the position of 0

	zeroRow, zeroCol = 0,0

	for row in currentState:
		try:
			zeroCol = row.index(0)
			zeroRow = currentState.index(row)
		except:
			pass


	# Calculating possible states from 0 position

	moveUp, moveDown, moveRight, moveLeft = [],[],[],[] # Possible states

	"""
	This an example array:

			[			A possible state is changing
			[1,2,3]		between 0 and 2. This means
	Rows >	[4,0,5]		0 would move up one row and
			[6,7,8]		don't move any column.
			]
			   v
			Columns
	"""


		# move up

	if zeroRow -1 >= 0:

		upNumber = currentState[zeroRow-1][zeroCol]

		moveUp = copy.deepcopy(currentState)

		moveUp[zeroRow][zeroCol] = upNumber
		moveUp[zeroRow-1][zeroCol] = 0

		# move down

	if zeroRow +1 <= arrayLen -1:

		downNumber = currentState[zeroRow+1][zeroCol]

		moveDown = copy.deepcopy(currentState)

		moveDown[zeroRow][zeroCol] = downNumber
		moveDown[zeroRow+1][zeroCol] = 0

		# move right

	if zeroCol +1 <= arrayLen -1:

		rightNumber = currentState[zeroRow][zeroCol+1]

		moveRight = copy.deepcopy(currentState)

		moveRight[zeroRow][zeroCol] = rightNumber
		moveRight[zeroRow][zeroCol+1] = 0

		# move left

	if zeroCol -1 >= 0:
		leftNumber = currentState[zeroRow][zeroCol-1]

		moveLeft = copy.deepcopy(currentState)

		moveLeft[zeroRow][zeroCol] = leftNumber
		moveLeft[zeroRow][zeroCol-1] = 0


	return [moveUp,moveDown,moveRight,moveLeft]

def getMatch(STATES, GOAL_STATE, lastBatchIndexes): # TODO TEST
	"""
	Checks if any value in the batch is equal to the goal
	state, and returns [boolean, goalMatchIndex]

	Uses STATES, GOAL_STATE global vars declared in main.py
	"""

	for index in lastBatchIndexes:
		try:
			valueToCheck = STATES[index]["nodeValue"]
			if valueToCheck == GOAL_STATE:
				return [True, index]
		except:
			print("Falló con valor: " + str(index))

	return [False, None]

def buildOutputString(finalIndex, STATES):
	"""
	Builds the output string.
	Expects an integer and a list of dictionaries, returns a string.

	Example of dict elements inside STATES list:

	firstNode = {
	"nodeValue": [],
	"parentIndex": Int
	}

	Example of output string.

	[1,2,3]		[1,2,3]		[1,2,3]
	[4,5,6] -> 	[4,5,6] ->	[4,5,6]
	[0,7,8]		[7,0,8]		[7,8,0]

	"""

	# Building a list of all indexes needed. We just traverse through
	# "parentIndex" values until None is reached.

	indexesOfValues = []

	currentIndex = finalIndex

	while currentIndex != None:
		indexesOfValues.append(currentIndex)
		currentIndex = STATES[currentIndex]["parentIndex"]

	# Building a list of nodeValues in ordered fashion
	indexesOfValues.sort()

	orderedNodeValues = []

	for i in indexesOfValues:
		thisValue = STATES[i]["nodeValue"]
		orderedNodeValues.append(thisValue)


	# Building the multi-line string line by line

	strHeight = len(orderedNodeValues[0])
	strLen = len(orderedNodeValues)

		# This fn makes double and single digits to be the same width
		# so it doesn't appear messy in the output
	orderedStringValues = formatValues(orderedNodeValues)

	finalString = ""

	for h in range(strHeight):
		for w in range(strLen):
			finalString += str(orderedStringValues[w][h])

			if w != strLen -1:
				if h == strHeight -2:
					finalString += " -> "
				else:
					finalString += "    " # 4 spaces

			if w == strLen -1 and h != strHeight -1:
				finalString += "\n"

	return finalString
			

def formatValues(orderedNodeValues):
	"""
	Expects a list of lists of lists (!)

	Returns a list of lists of strings (!)

	Those strings are transformed so single digits are
	the same lenght as multiple digits through spaces.
	"""

	# Getting max len to determine how much spaces we need
	maxLen = 0

	for element in orderedNodeValues[0][-1]:
		tempLen = len(str(element))
		if tempLen > maxLen: maxLen = tempLen

	# Building the strings
	orderedStringValues = []

	width = len(orderedNodeValues)
	height = len(orderedNodeValues[0])

	for w in range(width):
		tempWidth = []

		for h in range(height):
			tempHeight = ""
			heightLen = len(orderedNodeValues[w][h])
			tempHeight += "["

			for e in range(heightLen):
				element = orderedNodeValues[w][h][e]
				tempElement = ""
				eLen = len(str(element))
				numSpaces = maxLen - eLen
				if e == 0:
					for s in range(numSpaces): tempElement += " "
				else:
					for s in range(numSpaces+1): tempElement += " "
				tempElement += str(element)
				if e != heightLen -1: tempElement += ","

				
				tempHeight += tempElement
			
			tempHeight += "]"
			tempWidth.append(tempHeight)

		orderedStringValues.append(tempWidth)

	return orderedStringValues