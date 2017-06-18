import math

class rectangle:
	def __init__(self, l, b):
		self.l = l
		self.b = b
	def area(self):
		return self.l*self.b
	def pmeter(self):
		return (2*self.l) + (2*self.b)

class circle:
	def __init__(self, r):
		self.r = r
	def area(self):
		return math.pi * (self.r**2)
	def pmeter(self):
		return 2*math.pi*self.r

class square(rectangle):
        def __init__(self, side):
                rectangle.__init__(self, side, side)
