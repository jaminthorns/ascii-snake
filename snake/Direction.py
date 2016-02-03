class Direction:
	"""This class represents a directions on a plane."""

	UP = "H"
	LEFT = "K"
	DOWN = "P"
	RIGHT = "M"
	DIRECTIONS = ["H", "K", "P", "M"]

	@staticmethod
	def opposite(direction):
		"""Return the opposite of the current direction."""
		if direction == Direction.UP:
			return Direction.DOWN
		elif direction == Direction.LEFT:
			return Direction.RIGHT
		elif direction == Direction.DOWN:
			return Direction.UP
		elif direction == Direction.RIGHT:
			return Direction.LEFT
