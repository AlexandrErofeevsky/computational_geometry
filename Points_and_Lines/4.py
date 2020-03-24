import math
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
    
    def fromCoord(x1,y1,x2,y2):
        return Line(y1-y2, x2-x1, x1*y2 - x2*y1)
    
print(Line.distanceToZero(Line.fromCoord(1,0,0,1)))

print(Line.distanceToZero(Line.fromCoord(3,2,4,8)))

print(Line.distanceToZero(Line.fromCoord(2.34,8.75,-4.86,-12.36)))

print(Line.distanceToZero(Line.fromCoord(12.8,48.6,-7.568,-4.675)))

print(Line.distanceToZero(Line.fromCoord(48.6,-9.245,13.76,-5.92)))
