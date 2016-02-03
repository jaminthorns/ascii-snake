from Square import Square
from KeyListener import KeyListener

class Snake:
	"""This class represents the snake in a game of Snake."""

	def __init__(self, start):
		# List of squares representing the snake
		self.snake = [start]

	def __contains__(self, square):
		"""Returns whether this snake consists of a certain square."""
		return square in self.snake

	def advance(self, square):
		"""Moves the snake forward by one square."""
		self.snake.pop(0)
		self.snake.append(square)

	def grow(self, square):
		"""Grows the snake and moves it forward by one square."""
		self.snake.append(square)

	def head(self):
		"""Get the square at the head of the snake."""
		return self.snake[-1]
