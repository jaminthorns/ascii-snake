class Square:
	"""This class represents a square on a plane."""

	def __init__(self, x, y, num):
		# The x coordinate of this square
		self.x = x
		# The y coordinate of this square
		self.y = y
		# Big number used for hashing
		self.num = num

	def __eq__(self, other):
		"""Tests the equality of two Squares."""
		return self.x == other.x and self.y == other.y

	def __hash__(self):
		"""Hashes a Square."""
		return self.num * self.y + self.x

	def up(self):
		"""Return the Square above this square."""
		return Square(self.x + 1, self.y, self.num)

	def left(self):
		"""Return the Square to the left of square."""
		return Square(self.x, self.y - 1, self.num)

	def down(self):
		"""Return the Square below this square."""
		return Square(self.x - 1, self.y, self.num)

	def right(self):
		"""Return the Square to the right of this square."""
		return Square(self.x, self.y + 1, self.num)
