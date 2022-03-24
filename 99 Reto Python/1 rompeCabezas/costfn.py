"""
This script calculates de distances between a given
state and a goal state.

It removes all branches of a tree with suboptimal
distances by getting the distance of the current
state VS the goal state, ordering branches by such
metric and deleting all but one of them.

The reason for such cost function is the tradeof
between finding the best path a resource constraints.

So this script shouldn't be called often, as it will
very likely delete branches that could produce the
shortest path between zero and goal state, and it has
a performance hit itself.
"""

def deleteWeakBranches(GOAL, STATES, lastBatchIndexes):
	"""
	Main fn of the cost function. Orchestrates all
	other functions.
	"""

	# Getting the distances of current batch
	distancesListOfDict = getDistances(GOAL, STATES, lastBatchIndexes)

	# Finding the best performer branch
	# (so listing all worse performers for delete)

	branchesToDelete = getWeakBranches(distancesListOfDict)

	# Recursively delete all entries in STATES from
	# weak branches except for the initial entry

	nukeWeakBranches(STATES, branchesToDelete)

	# Nothing to return, just be happy and enjoy life
	# out of the screen.


def getDistances(GOAL, STATES, lastBatchIndexes):
	"""
	Calculates euclidean distances for each integer
	between current and goal state.

	Returns a list of dictionaries with:
	index: 0
	distance 0 (sum of the distances of all integers)
	"""

	distancesListOfDict = []

	

def getWeakBranches(distancesDict):
	"""
	"""
