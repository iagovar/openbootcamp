"""
This script computes de distances between a given
state and a goal state.

It removes all branches of a tree with suboptimal
distances by getting the distance of the current
state VS the goal state, ordering branches by such
metric and deleting half of them.

The reason for such cost function is the tradeof
between finding the best path and resource constraints.

So this script shouldn't be called often, as it will
very likely delete branches that could produce the
shortest path between zero and goal state, and it has
a performance hit itself.
"""

def deleteWeakBranches(GOAL_STATE, STATES, lastBatchIndexes):
	"""
	Main fn of the cost function. Orchestrates all
	other functions.
	"""

	# Getting the distances of current batch
	distancesListOfDict = getDistances(GOAL_STATE, STATES, lastBatchIndexes)

	# Finding the best performer branch
	# (so listing all worse performers for delete)

	branchesToSave = getWeakBranches(distancesListOfDict)

	# Recursively delete all entries in STATES from
	# weak branches except for the initial entry

	nukeWeakBranches(STATES, branchesToSave)

	# Nothing to return, just be happy and enjoy life
	# out of the screen.


def getDistances(GOAL_STATE, STATES, lastBatchIndexes):
	"""
	Calculates distances for each integer
	between current and goal state.

	- Returns a list of dictionaries with:

	index: 0
	distance 0 (sum of the distances of all integers)

	- Distances are the result of such operation:

	goal index 		= {height postion, width position}
	current index 	= {height postion, width position}
	num distance 	= abs(currentH-goalH) + abs(ccurrentW-goalW)
	total distance 	= sum of all num distances
	"""

	arrayLen = len(GOAL_STATE)

	# Building a dictionary of positions for
	# each integer in the GOAL array
	goalPositions = {}

	for height in range(arrayLen):
		for width in range(arrayLen):
			number = GOAL_STATE[height][width]
			goalPositions[number] = {"height": height, "width": width}

	# Building a dictionary of positions for
	# each integer in the STATE array
	# 
	# statePositions[0]
	# 	{
	#	 "index": o,
	#	 "positions":
	#				 {
	#				  0: {"height": 1, "width": 2}
	#				 }
	#	}

	statePositions = [] # > It's a list of dictionaries!

	for index in lastBatchIndexes:
		thisDict = {}
		thisDict["index"] = index
		thisDict["positions"] = {}
		thisDict["numDistances"] = {}
		thisDict["distance"] = None

		thisArray = STATES[index]["nodeValue"]

		for height in range(arrayLen):
			for width in range(arrayLen):
				number = thisArray[height][width]
				thisDict["positions"][number] = {"height": height, "width": width}

		statePositions.append(thisDict)

	# Comparing state vs goal positions
	# and storing it all with this
	# abhorrent for loop

	currentLen = len(statePositions)
	numberLen = len(goalPositions)

	for i in range(currentLen):
		for number in range(numberLen):
			currentHeight 	= statePositions[i]["positions"][number]["height"]
			currentWidth 	= statePositions[i]["positions"][number]["width"]
			goalHeight 		= goalPositions[number]["height"]
			goalWidth 		= goalPositions[number]["width"]

			numDistance = abs(currentHeight-goalHeight) + abs(currentWidth-goalWidth)

			statePositions[i]["numDistances"][number] = numDistance

		sumOfDistances = sum(statePositions[i]["numDistances"].values())
		statePositions[i]["distance"] = sumOfDistances

		del statePositions[i]["numDistances"]
		del statePositions[i]["positions"]

	return statePositions


def getWeakBranches(distancesListOfDict):
	"""
	Expects a list of dictionaries like this:
	
	{
	index: int,
	distance: int
	}

	Orders such list by distance, the lower
	the better.

	Then removes 50% of such list with worse
	distance, an returns the rest as a list of
	integers.
	"""

	distancesListOfDict.sort(key=lambda e: e["distance"])

	halfList = round(len(distancesListOfDict)/2)

	branchesToSave = []

	for i in range(len(distancesListOfDict)):
		if i < halfList:
			thisIndex = distancesListOfDict[i]["index"]
			branchesToSave.append(thisIndex)

	return branchesToSave


def nukeWeakBranches(STATES, branchesToSave):
	"""
	This fn deletes all branches of STATES
	not needed to reach any of the state indexes
	listed in branchesToSave.

	Expects the STATES list of dictionaries and
	branchesToSave list of integers.
	"""

	# Buiilding a list of all the needed indexes
	# to reach saved current STATES.
	neededIndexes = []

	for element in branchesToSave:
		currentIndex = element
		while currentIndex != None:
			neededIndexes.append(currentIndex)
			currentIndex = STATES[currentIndex]["parentIndex"]


	# Deleting all indexes in STATES not in neededIndexes
	# Lists know their lenght in python, so calling len()
	# shouln't be a problem for such large data structure.

	statesLen = len(STATES)
	print("La longitud del índice es " + str(statesLen))
	input("presiona una tecla")

	for i in range(statesLen):
		if i not in neededIndexes:
			try: 
				print("indice " + str(i) + " NO está en los necesarios")
				print("Global es  es " + str(STATES[i]) + "\n")
				del STATES[i]
			except:
				pass
		print("indice " + str(i) + " SÍ está en los necesarios")

	# this should be done auto on scope out, but somehow
	# it doesn't sometimes ¿? so adding manually.
	del neededIndexes