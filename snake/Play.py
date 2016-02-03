import platform
import os
import msvcrt
from Direction import Direction
from Game import Game

def displayMenu(option, size, difficulty, placeObstacles):
	"""Display the main menu."""
	if size == 0: sizeString = "Small"
	elif size == 1: sizeString = "Medium"
	elif size == 2: sizeString = "Large"

	if difficulty == 0: difficultyString = "Easy"
	elif difficulty == 1: difficultyString = "Medium"
	elif difficulty == 2: difficultyString = "Hard"

	if placeObstacles: obstacleString = "On"
	else: obstacleString = "Off"

	print("SNAKE\n")
	print(">" if option == 0 else " ", "Play")
	print(">" if option == 1 else " ", "Size:", sizeString)
	print(">" if option == 2 else " ", "Difficulty:", difficultyString)
	print(">" if option == 3 else " ", "Obstacles:", obstacleString)
	print(">" if option == 4 else " ", "Quit")

def playGame(size, difficulty, placeObstacles):
	"""Initialize and play the game Snake"""
	if size == 0: height, width = 20, 20
	elif size == 1: height, width = 30, 30
	elif size == 2: height, width = 40, 40

	if difficulty == 0: speed = 0.075
	elif difficulty == 1: speed = 0.05
	elif difficulty == 2: speed = 0.025

	game = Game(height, width, speed, placeObstacles)
	game.play()

def processKey():
	"""Process the user input for menu navigation."""
	global option, size, difficulty, placeObstacles, play, quit

	key = msvcrt.getwch()

	if key == "\xe0":
		key = msvcrt.getwch()

		if key == Direction.UP and option > 0:
			option -= 1
		elif key == Direction.DOWN and option < 4:
			option += 1
		elif key == Direction.LEFT:
			if option == 1 and size > 0 and size <= 2:
				size -= 1
			elif option == 2 and difficulty > 0 and difficulty <= 2:
				difficulty -= 1
			elif option == 3:
				placeObstacles = not placeObstacles
		elif key == Direction.RIGHT:
			if option == 1 and size >= 0 and size < 2:
				size += 1
			elif option == 2 and difficulty >= 0 and difficulty < 2:
				difficulty += 1
			elif option == 3:
				placeObstacles = not placeObstacles
	elif key == "\r":
		if option == 0:
			play = True
		elif option == 4:
			quit = True

option = 0
size = 0
difficulty = 0
placeObstacles = False
play = False
quit = False
clearScreen = "cls" if platform.system() == "Windows" else "clear"

while not quit:
	# Display the menu
	os.system(clearScreen)
	displayMenu(option, size, difficulty, placeObstacles)

	# Process user input
	processKey()

	# Play the game
	if play:
		playGame(size, difficulty, placeObstacles)
		play = False
