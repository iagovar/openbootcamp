"""
A B C
D E F
G H I

How many path combinations can we get with such array with the following
constrainsts?

1. We can't use any position twice.
2. We're only allowed to travel one position unless we can "fly over" an
used position.
3. Weid semi-diagonal paths like B -> I are allowed, and such paths
don't "fly over" anything.
4. Can't have more steps than introduced (counting starting point)
"""

from utils import *

STARTING_POINT = None 	# Must be a string from A to I
STEPS = None 			# Must be an integer


def solverOrchestration(STARTING_POINT, STEPS):
	"""
	Calculartes all possible combinations from STARTING_POINT
	"""

	possiblePathsList = getPossiblePaths(STARTING_POINT)

	# Do such combinations satisfy all the constraints?
	# if so, include in satisfyingPaths
	satisfiedList = []

	for element in possiblePathsList:
		# Checking all conditions
		# POSIBLEMENTE NO SEAN NECESARIOS
		# DESARROLLA getPossiblePaths  PRIMERO
		if hasDuplicates(element): continue
		if len(element) != STEPS: continue
		if hasWrongFlyOvers(element): continue

		# Adding to list if meets all criteria
		satisfiedList.append(element)

	#

	return toPrint


# Asking for user input

print("Please, enter your starting point and the desired number of steps.")
STARTING_POINT = input("Starting point (A string from A to I: ")
STEPS = input("Number of desired steps (An integer): ")
STARTING_POINT.upper()

# Printing result

toPrint = solverOrchestration(STARTING_POINT, STEPS)

print("These are all possible paths within given constraints:")
for element in toPrint:
	print(element)