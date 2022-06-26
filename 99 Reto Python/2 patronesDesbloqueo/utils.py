def getPossiblePaths(STARTING_POINT):
	"""
	Computes all possible paths for a grid by an starting point

	Expects a string for STARTING_POINT.
	Returns a list of lists.
	"""

	grid = [["A","B","C"],["D","E","F"],["G","H","I"]]
	gridLen = len(grid) * len(grid[0])
	gridHeight = len(grid)
	gridWidth = len(grid[0])

	storedStates = []

	



def hasDuplicates(element):
	"""
	Checks if a list has duplicated elements.
	Expects a list.
	Returns a boolean.
	"""

	if len(element) == len(set(element)):
		return False
	else:
		return True