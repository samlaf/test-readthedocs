"""Foo module. Nothing much here."""

x = 3
def getx():
	"""This function returns x."""
	return x
def setx(val):
	"""This function sets the value of x.

	There's more information here..."""
	global x
	x = val
def printx():
	"""This function prints the value of x."""
	print(x)
