import math

def defsign(x):
    if x >= 0:
        return 1
    else:
        return -1

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
        self.x0 = 0
        self.x1 = 1
        if b != 0:
            self.y0 = -self.c/self.b
            self.y1 = (-self.c-self.a)/self.b
            self.sin = (self.y1-self.y0)/math.sqrt((self.y1-self.y0)**2+1)
            self.cos = 1/math.sqrt((self.y1-self.y0)**2+1)
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

    def perpendicularLine(self, point):
        a = -1
        if self.b != 0:
            b = self.a/self.b
        else:
            b = self.a 
        c = point.x - b*point.y
        return Line(-a, -b, -c)
        
    def nearPoint(self, point):
        return self.intersection(self.perpendicularLine(point))    

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
            return

    def normalize(self):
        if self.c != 0:
            self.a = self.a/self.c
            self.b = self.b/self.c
            self.c = 1
        elif self.a != 0:
            self.c = 0
            self.b = self.b/self.a
            self.a = 1
        else:
            self.a = 0
            self.c = 0
            self.b = 1

    def parallelLine(self, point):
        c = - self.a * point.x - self.b * point.y
        return Line(self.a, self.b, c)

    def projectionLength(self, point1, point2):
        p1 = self.nearPoint(point1)
        p2 = self.nearPoint(point2)
        return round(math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2),3)
    
    def middlePoint(self, point):
        p = self.nearPoint(point)
        return Point((point.x+p.x)/2, (point.y+p.y)/2)

    def symmetricPoint(self,point):
        p = self.nearPoint(point)
        x = 2*p.x - point.x
        y = 2*p.y - point.y
        return Point(x, y)

    def insideTreug(self, p):
        if (self.a == 0) or (self.b == 0):
            return False
            ox = Line.fromCoord(0,0,1,0)
            oy = Line.fromCoord(0,0,0,1)
            A = self.intersection(ox)
            B = self.intersection(oy)
            C = ox.intersection(oy)
            vara = (A.x-p.x)*(B.y-A.y)-(B.x-A.x)*(A.y-p.y)
            varb = (B.x-p.x)*(C.y-B.y)-(C.x-B.x)*(B.y-p.y)
            varc = (C.x-p.x)*(A.y-C.y)-(A.x-C.x)*(C.y-p.y)
            if defsign(vara) == defsign(varb) == defsign(varc):
                return True
            else:
                return False

    def rotatedLine(self, point):
        if self.b == 0:
            new_x = point.x
            new_y = point.y + (point.x + self.c/self.a)
            new_p = Point(new_x, new_y)
            new_line = parline.perpendicularLine(new_p)
        elif self.a == 0:
            new_y = point.y
            new_x = point.x - (point.y + self.c/self.b)
            new_p = Point(new_x, new_y)
            new_line = parline.perpendicularLine(new_p)
        else:
            parline = self.parallelLine(point)
            r = self.distanceToPoint(point)
            if (-self.a*point.x - self.c)/self.b >= point.y:
                new_x = point.x + r * parline.cos
                new_y = point.y + r * parline.sin
                new_x1 = (line.nearPoint(point)).x + r * parline.cos
                new_y1 = (line.nearPoint(point)).y + r * parline.sin
            else:
                new_x = point.x - r * parline.cos
                new_y = point.y - r * parline.sin
                new_x1 = (line.nearPoint(point)).x - r * parline.cos
                new_y1 = (line.nearPoint(point)).y - r * parline.sin
            new_line = Line.fromCoord(new_x, new_y, new_x1, new_y1)
        new_line.normalize()
        return new_line

    def bisectrix(self, line):
        if self.isParallel(line):
            bis_a = self.a
            bis_b = self.b
            bis_c = -(self.b/self.c + line.c/line.b)/2
            bis = Line(bis_a,bis_b,bis_c)
            bis.normalize()
            return bis
        elif abs(-self.a/self.b - line.b/line.a) <= 0.001:
            return None
        else:
            i1 = math.sqrt((line.a)**2+(line.b)**2)
            i2 = math.sqrt((self.a)**2+(self.b)**2)
            bis_a = i1*self.a + i2*line.a
            bis_b = i1*self.b + i2*line.b
            bis_c = i1*self.c + i2*line.c
            bis = Line(bis_a,bis_b,bis_c)
            bis.normalize()
            return bis
        
    
    def fromCoord(x1,y1,x2,y2):
        return Line(y1-y2, x2-x1, x1*y2 - x2*y1)

line = Line.fromCoord(0,0,1,2)
line2 = Line.fromCoord(0, 0,2,1)
print(line.bisectrix(line2))

line = Line.fromCoord(-7.73, -10.63, 14.18, -0.17)
line2 = Line.fromCoord(-12.23, -7.67, 0.19, 7.40)
print(line.bisectrix(line2))

line = Line.fromCoord(1, 1, -2, -2)
line2 = Line.fromCoord(0, 1, 1, 0)
print(line.bisectrix(line2))

line = Line.fromCoord(4.27,11.18,-12.89,-1.11)
line2 = Line.fromCoord(-5.45,-10.57,-2.30,-12.17)
print(line.bisectrix(line2))
