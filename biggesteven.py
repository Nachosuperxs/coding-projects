x = input("x = ")
y = input("y = ")
z = input("z = ")

def evenx(x):
	if x%2==0:
		return x

def eveny(y):
	if y%2==0:
		return y

def evenz(z):
	if z%2==0:
		return z

x = evenx(x)
y = evenx(y)
z = evenx(z)

if x>y and x>z:
	print "x is the biggest even number!"
	
elif y>x and y>z:
	print "y is the biggest even number!"
	
elif z>x and z>y:
	print "z is the biggest even number!"
elif x==y==z:
	print "They're the same number!"
else:
	print "There are no even numbers!"

input("Press enter to exit!")
