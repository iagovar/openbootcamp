"""
Sliding cards solver.

This solver just brute-forces the problem.

It calculates al possible states, stores states
in a dictionary linked in a sort of tree data
structure, and chooses the earliest solution.

"""
import copy
from utils import *
from costfn import *

# Gloval vars & structures (I know, I know!)

	# Is it solved?, What's the index of the final step matching the goal?

SOLVED = [False, None]

STATES = [] # list of dictionaries {nodeValue: [list/array], parentIndex: int}
GOAL_STATE = []

	# Turns on/off the cost fn (based on manhattan distance) to free memory up.
	# This cost fn could avoid the shortest path to GOAL, so it's a trade-off.

COST_FN = False
				

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

		# Exploring possible states from previous ones
		for thisBatchIndex in lastBatchIndexes:
			tempMoveList = possibleStates(STATES[thisBatchIndex]["nodeValue"])

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

		# Temporal batch indexes substitutes last batch indexes
		# So we can interate all over again
		lastBatchIndexes = copy.deepcopy(tempBatchIndexes)

		# Freeing up memory in case of COST_FN = True
		if COST_FN == True:
			if len(STATES) > 1000:
				deleteWeakBranches(GOAL_STATE, STATES, lastBatchIndexes)

		
	# Building the output string

	finalIndex = SOLVED[1]
	outputString = buildOutputString(finalIndex, STATES)

	return outputString

toPrint = solveCardsPuzzle([[2,3,8],[1,4,5],[7,6,0]])

print(toPrint)

