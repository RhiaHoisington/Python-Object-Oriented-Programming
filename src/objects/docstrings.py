# Example of docstring generated by autoDocstring VS Code extension

class DocStrings:
	"""

	"""
	def __init__(self, x: int, y: str) -> None:
		""" Initializer.

		Args:
				x (int): integer input data
				y (str): string input data
		"""
		self.x = x
		self.y = y

	def __str__(self) -> str:
		"""String representation of Class

		Returns:
				str: returns string rep.
		"""
		return f'{self.x} {self.y}'

