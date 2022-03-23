"""
Unit testing tiles puzzle using Pytest

Learning from: https://www.tutorialspoint.com/pytest/pytest_tutorial.pdf

Remember:
 - Testing function names must start by test*
"""

import pytest
from main import *
from utils import *


def testInputFormatSize():
	# Testing for lack of 0
	assert doesInputValidate([[1,2,3],[4,5,6],[7,8,9]]) == False, "Accepts input without 0, it shouldn't"
	# Testing for continuity
	assert doesInputValidate([[1,2,3],[4,5,6],[7,8,0]]) == True, "Fails on a 3x3 sequential input"
	assert doesInputValidate([[1,2,3],[4,5,6],[7,9,0]]) == False, "Accepts on a 3x3 non-sequential input"
	# Check for non-square inputs
	assert doesInputValidate([[1,2,3],[4,5,6],[7,0]]) == False, "Accepts non-square input"
	assert doesInputValidate([[1,0,3],[4,5,6],[7,2]]) == False, "Accepts non-square input"
	# Check for other dimensions
	assert doesInputValidate([[1,0,3,2],[4,5,6,9],[7,8,10,11],[12,13,14,15]]) == True, "Fails on 4x4 input"
	assert doesInputValidate(
		[
		[0,1,2,3,4],
		[5,6,7,8,9],
		[10,11,12,13,14],
		[15,16,17,18,19],
		[20,21,22,23,24]
		]
		) == True, "Fails on 5x5 input"

# NOTE: All fn down the line assume inputs as valid

def testForGoalState():
	# Testing for unordered arrays
	assert getGoalState([[0,1,4,3],[2,6,10,11],[8,5,9,7],[13,12,14,15]]) == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]], "Fails at 4x4 unordered Array"
	assert getGoalState([[0,1,4],[2,6,3],[8,5,7]]) == [[1,2,3],[4,5,6],[7,8,0]], "Fails at 3x3 unordered Array"	


def testforPossibleStates():
	# Testing possible states as nested array outputs [moveUp,moveDown,moveRight,moveLeft]

	firstClue 	=	[[1,2,3],[4,0,5],[6,7,8]]
	firstUp		=	[[1,0,3],[4,2,5],[6,7,8]]
	firstDown	=	[[1,2,3],[4,7,5],[6,0,8]]
	firstRight	=	[[1,2,3],[4,5,0],[6,7,8]]
	firstLeft	=	[[1,2,3],[0,4,5],[6,7,8]]

	assert possibleStates(firstClue) == [firstUp,firstDown,firstRight,firstLeft]

	secondClue 	=	[[1,2,3],[4,5,0],[6,7,8]]
	secondUp	=	[[1,2,0],[4,5,3],[6,7,8]]
	secondDown	=	[[1,2,3],[4,5,8],[6,7,0]]
	secondRight	=	[]
	secondLeft	=	[[1,2,3],[4,0,5],[6,7,8]]

	assert possibleStates(secondClue) == [secondUp,secondDown,secondRight,secondLeft]

	thirdClue 	=	[[1,2,0],[3,4,5],[6,7,8]]
	thirdUp		=	[]
	thirdDown	=	[[1,2,5],[3,4,0],[6,7,8]]
	thirdRight	=	[]
	thirdLeft	=	[[1,0,2],[3,4,5],[6,7,8]]

	assert possibleStates(thirdClue) == [thirdUp,thirdDown,thirdRight,thirdLeft]

#def testForGetMatch() TODO
	 