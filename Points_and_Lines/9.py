import math

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "(%.2f, %.2f)"%(self.x,self.y)
    
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
        
    def isParallel(self, line):
        return abs(self.a*line.b - self.b*line.a) <= 0.001

    def intersection(self, line):
        if not self.isParallel(line):
            inter_x = (line.c*self.b - self.c*line.b)/(line.b*self.a - self.b*line.a)
            inter_y = (line.c*self.a - self.c*line.a)/(-line.b*self.a + self.b*line.a)
            inter_point = Point(inter_x,inter_y)
            return inter_point
        else:
            return None

    def perpendicular(self, point):
        a = -1
        if self.b != 0:
            b = self.a/self.b
        else:
            b = self.a 
        c = point.x - b*point.y
        return Line(a, b, c)
        
    def nearPoint(self, point):
        return self.intersection(self.perpendicular(point))
        

    def whatSide(self, point):
        if (self.a !=0) & (self.b == 0):
            if round(abs(point.x +self.c/self.a),4)< 0.001:
                return "On"
            elif point.x < -self.c/self.a:
                return "Left"
            else:
                return "Right"
        elif self.b !=0:
            if round(abs(point.y + (self.a*point.x+self.c)/self.b),4) < 0.001:
                return "On"
            elif point.y < (-self.a*point.x-self.c)/self.b:
                return "Down"
            else:
                return "Up"
            
    def oneSide(self, p1, p2):
        trash = [("Right", "Left"), ("Left", "Right"), ("Up", "Down"), ("Down", "Up")]
        if (self.whatSide(p1), self.whatSide(p2)) in trash:
            return False
        else:
            return True
    
    def fromCoord(x1,y1,x2,y2):
        return Line(y1-y2, x2-x1, x1*y2 - x2*y1)

line1 = Line.fromCoord(0, 1, 1, 0)
point1 = Point(3, 4)
point2 = Point(-2, -3)
print(line1.oneSide(point1, point2))

line2 = Line.fromCoord(1, 0, 0, 1)
point1 = Point(3, 3)
point2 = Point(2, 5)
print(line2.oneSide(point1, point2))

line3 = Line.fromCoord(12.85, -3.75, 7.86, 6.45)
point1 = Point(15.784, -15.45)
point2 = Point(-2.34, 7.52)
print(line3)
print(line3.oneSide(point1, point2))

line4 = Line.fromCoord(-3, 0, 0, 1)
point1 = Point(12, 2)
point2 = Point(3, 2)
print(line4.oneSide(point1, point2))

