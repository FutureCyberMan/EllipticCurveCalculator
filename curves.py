# 02 April 2023

class curve:
	"""
	A class used to represent an elliptic curve

	Attributes
	----------
	a : int
		the a coefficient in an elliptic curve
	b : int
		the b term in an elliptic curve
	"""
	def __init__(self, a: int, b: int) -> None:
		self.a = a
		self.b = b
	
	def __eq__(self, other: 'curve') -> bool:
		return self.a == other.a and self.b == other.b

class point:
	"""
	A class used to represent a point on an elliptic curve

	Attributes
	----------
	x : int
		the x coordinate
	y : int
		the y coordinate
	p : int
		the modulo p
	curve : int
		the curve that this point exists on
	
	Methods
	-------
	"""

	def __init__(self, x: int, y: int, p: int, curve: curve) -> None:
		self.x = x
		self.y = y
		self.p = p
		self.curve = curve
	
	def __str__(self):
		return f"({self.x}, {self.y})"
	
	def __slope(self, b: 'point') -> int:
		"""Gets the slope between two points
		
		Parameters
		----------
		self : point
			The current point
		b : point
			The other point to determine slope
		
		Returns
		-------
		int
			the integer slope
		"""
		if self == b:
			inverse = pow(2*self.y, -1, self.p)
			return ((3*self.x**2 + self.curve.a) * inverse) % self.p
		else:
			try:
				inverse = pow(b.x - self.x, -1, b.p)
			except ValueError as err:
				raise ZeroDivisionError(f"Denominator is {b.x - self.x}")
			return ((b.y - self.y) * inverse) % self.p
	
	def __eq__(self, other: 'point') -> bool:
		if self.p != other.p or self.curve != other.curve:
			raise Exception("Not the same curve!!")
		else:
			return self.x == other.x and self.y == other.y

	def __add__(self, other: 'point') -> 'point':
		s = self.__slope(other)
		x3 = (s**2 - self.x - other.x) % self.p
		y3 = (s*(self.x - x3) - self.y) % self.p
		return point(x3, y3, self.p, self.curve)
	
	def __mul__(self, other: int) -> 'point':
		if not isinstance(other, int):
			raise TypeError(f"{other} is not an integer!. Can only multiply with integers")
		output = self
		for _ in range(other-1):
			output += self
		return output
	
	def __rmul__(self, other: int) -> 'point':
		return self.__mul__(other)