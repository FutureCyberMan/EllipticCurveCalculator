# 02 April 2023

class point:

	def __init__(self, x, y, p, curve):
		self.x = x
		self.y = y
		self.p = p
		self.curve = curve
	
	def __str__(self):
		return f"({self.x}, {self.y})"
	
	def slope(self, b):
		if self == b:
			inverse = pow(2*self.y, -1, self.p)
			return ((3*self.x**2 + self.curve.a) * inverse) % self.p
		else:
			try:
				inverse = pow(b.x - self.x, -1, b.p)
			except ValueError as err:
				raise ZeroDivisionError(f"Denominator is {b.x - self.x}")
			return ((b.y - self.y) * inverse) % self.p
	
	def __eq__(self, other):
		if self.p != other.p or self.curve != other.curve:
			raise Exception("Not the same curve!!")
		else:
			return self.x == other.x and self.y == other.y

	def __add__(self, other):
		s = self.slope(other)
		x3 = (s**2 - self.x - other.x) % self.p
		y3 = (s*(self.x - x3) - self.y) % self.p
		return point(x3, y3, self.p, self.curve)
	
	def __mul__(self, other):
		if not isinstance(other, int):
			raise TypeError(f"{other} is not an integer!. Can only multiply with integers")
		output = self
		for _ in range(other-1):
			output += self
		return output
	
	def __rmul__(self, other):
		return self.__mul__(other)

class curve:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def __eq__(self, other):
		return self.a == other.a and self.b == other.b