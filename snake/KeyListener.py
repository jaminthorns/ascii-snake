import msvcrt
from threading import Thread
from Direction import Direction

class KeyListener(Thread):
	"""Thread class that gets input from the keyboard's keys."""

	def __init__(self):
		# The current direction
		self.direction = None
		# Boolean indicating whether this game is paused
		self.paused = False
		# Boolean indicating whether to quit the game
		self.quit = False
		# Boolean indicating whether this thread is active
		self.active = False
		# Call to the superclass' constructor
		super(KeyListener, self).__init__()

	def run(self):
		self.active = True

		while self.active:
			key = msvcrt.getwch()

			# Get a direction
			if key == "\xe0":
				key = msvcrt.getwch()

				if key in Direction.DIRECTIONS:
					self.direction = key
			# Flip the pause toggle
			elif key == " ":
				self.paused = not self.paused
			# Flip the quit toggle
			elif key == "q":
				self.quit = True

	def end(self):
		"""End this thread."""
		self.active = False
