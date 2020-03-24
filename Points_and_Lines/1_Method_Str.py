import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%.2f,%.2f)"%(self.x,self.y)

# check fields x and y
p = Point(2.34, 5.67)
print ("%.2f" % p.x)
print ("%.2f" % p.y)

# check constructor
point = Point(-18.5, 13.5)
# check overriding __str__()
print(point)

	
# check constructor
point = Point(3.25, -6.75)
# check overriding __str__()
print(point)
