import math

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "(%.2f,%.2f)"%(self.x,self.y)
    
    def distanceTo(self, point):
        return math.sqrt((self.x - point.x)**2+(self.y - point.y)**2)
    
class Line:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def __str__(self):
        if self.a < 0:
            real_a = "-%.2f"%(abs(self.a))
        else:
            real_a = "%.2f"%(self.a)
        if self.b < 0:
            real_b = "- %.2f"%(abs(self.b))
        else:
            real_b = "+ %.2f"%(self.b)
        if self.c < 0:
            real_c = "- %.2f"%(abs(self.c))
        else:
            real_c = "+ %.2f"%(self.c)
        return "{}x {}y {} = 0".format(real_a,real_b,real_c)

    def distanceToZero(self):
        denominator = math.sqrt(self.a**2+self.b**2)
        if denominator != 0:
            return abs(self.c)/denominator
        else:
            return c

    def distanceToPoint(self, point):
        denominator = math.sqrt(self.a**2+self.b**2)
        if denominator != 0:
            return abs(self.a*point.x + self.b*point.y + self.c)/denominator
    
    def fromCoord(x1,y1,x2,y2):
        return Line(y1-y2, x2-x1, x1*y2 - x2*y1)

line = Line.fromCoord(1, 0, 0, 1)
point = Point(3, 2)
print(line.distanceToPoint(point))

line = Line.fromCoord(-2.84, 3.485, 6.21, -7.65)
point = Point(8.25, 3.75)
print(line.distanceToPoint(point))

line = Line.fromCoord(5.87, 61.45, -45.86, -3.478)
point = Point(-78.95, 125.75)
print(line.distanceToPoint(point))

line = Line.fromCoord(12, -9.75, -48.245, 68.775)
point = Point(78.85, -85.45)
print(line.distanceToPoint(point))

line = Line.fromCoord(15.75, 96.45, -7.654, -125.65)
point = Point(12.45, -354.8)
print(line.distanceToPoint(point))



