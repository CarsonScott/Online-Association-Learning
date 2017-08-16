from decimal import Decimal 

def Dec(x):
	return Decimal(x)

e = 2.718281828459

class Function:

	def __init__(self, a=None, b=None, c=None):
		self.setparams(a, b, c)

	def setparams(self, a=None, b=None, c=None):
		self.a = a
		self.b = b
		self.c = c

	def reflect(self):
		self.c *= -1

	def __call__(self, x):
		return

class Gaussian(Function):

	def __call__(self, x):
		return self.a * pow(e, -pow(x-self.b, 2) / pow(2 * self.c, 2))

class Logistic(Function):

	def __call__(self, x):
		try:
			y = self.a / (1+pow(e, -self.c * (x-self.b)))
		except OverflowError:
			y = float('inf')
		return y
class Window(Function):

	def __call__(self, x):
		if x in range(self.b-self.c, self.b+self.c):
			return self.a
		return 0

class Step(Function):
	
	def __call__(self, x):
		if x >= self.b:
			return self.a
		return 0

class Decay(Function):

	def __call__(self, x):
		return

