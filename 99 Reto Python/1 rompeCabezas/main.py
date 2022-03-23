"""
Sliding cards solver.

This solver just brute-forces the problem.

It calculates al possible states, stores states
in a dictionary linked in a sort of tree data
structure, and chooses the earliest solution.

"""
import copy
from utils import *

# Gloval vars & structures

SOLVED = [False, None] # Is it solved?, What's the index of the final step matching the goal?

STATES = [] # list of dictionaries {nodeValue, parentIndex}
GOAL_STATE = []

def solveCardsPuzzle(inputArray):

	# input validation
	isInputValid = doesInputValidate(inputArray)
	if isInputValid == False:
		return None

	# Storing our goal state (desired array)
	global GOAL_STATE
	GOAL_STATE = getGoalState(inputArray)

	# Storing the initial array as root node in tree
	# (up to 4 branches for each node, but variable)

	firstNode = {
	"nodeValue": [],
	"parentIndex": None # for further traversing & string output building
	}

	firstNode["nodeValue"] = inputArray

	global STATES
	STATES.append(firstNode)

	# Iterating until we find a state that matches goal
	tempBatchIndexes = []
	lastBatchIndexes = [0]

	global SOLVED
	SOLVED = [False, None]

	while SOLVED[0] == False:

		# Matching states with goal
		isThereMatch = getMatch(STATES, GOAL_STATE, lastBatchIndexes)
		if isThereMatch[0] == True:
			SOLVED[0] = True # Redundant/not useful for now
			SOLVED[1] = isThereMatch[1]
			break

		#DEBUG
		#print("Match result " + str(isThereMatch))

		# Exploring possible states from previous ones
		for thisBatchIndex in lastBatchIndexes:
			tempMoveList = possibleStates(STATES[thisBatchIndex]["nodeValue"])

			#DEBUG
			#print("Prueba  " + str(lastBatchIndexes))
			#print("Batch loop " + str(thisBatchIndex))

			# Storing new obtained states
			for thisMove in tempMoveList:
				if len(thisMove) != 0:
					tempMoveDict = {
						"nodeValue": thisMove,
						"parentIndex": thisBatchIndex
						}
					STATES.append(tempMoveDict)

					# Building new batch index for next iteration
						# Note: Python lists already store their lenght
						# according to a bunch of dudes in S.O., so do
						# not wet your blankets with len(someHugeList)
					tempMoveDictIndex = len(STATES) -1
					tempBatchIndexes.append(tempMoveDictIndex)
					#DEBUG
					#print("Storing " + str(thisMove) + " with index " + str(tempMoveDictIndex))
					#input("Press a key")

		# Temporal batch indexes substitutes last batch indexes
		# So we can interate all over again
		lastBatchIndexes = copy.deepcopy(tempBatchIndexes)

		
	# Building the output string

	finalIndex = SOLVED[1]
	outputString = buildOutputString(finalIndex, STATES)

	return outputString

toPrint = solveCardsPuzzle([[1,2,3,4],[5,6,7,8],[9,0,11,12],[13,10,14,15]])

print(toPrint)

