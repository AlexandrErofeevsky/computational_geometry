import math
class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "(%.2f, %.2f, %.2f)"%(self.x,self.y,self.z)
    def len(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    def norm(self):
        if self.len() != 0:
            leng = self.len()
            self.x = self.x/leng
            self.y = self.y/leng
            self.z = self.z/leng
            return self
        else:
            return self
    def xR(self, n):
        self.x = self.x * n
        self.y = self.y * n
        self.z = self.z * n
        return self
    def plusV(self,vect):
        self.x = self.x + vect.x
        self.y = self.y + vect.y
        self.z = self.z + vect.z
        return self
    def minusV(self,vect):
        self.x = self.x - vect.x
        self.y = self.y - vect.y
        self.z = self.z - vect.z
        return self
    def dotV(self,vect):
        temp = self.x * vect.x + self.y * vect.y + self.z * vect.z
        return temp
    def xV(self,vect):
        x = self.y*vect.z-self.z*vect.y
        y = -(self.x*vect.z-self.z*vect.x)
        z = self.x*vect.y-self.y*vect.x
        return Vector3(x,y,z)
    
class Matrix3x3:
    def __init__(self, a, b, c):
        self.a = Vector3(a.x,a.y,a.z)
        self.b = Vector3(b.x,b.y,b.z)
        self.c = Vector3(c.x,c.y,c.z)
        self.column1 = Vector3(a.x,b.x,c.x)
        self.column2 = Vector3(a.y,b.y,c.y)
        self.column3 = Vector3(a.z,b.z,c.z)
    def __str__(self):
        return "((%.2f, %.2f, %.2f),\n (%.2f, %.2f, %.2f),\n (%.2f, %.2f, %.2f))"%((self.a).x,(self.a).y,(self.a).z, (self.b).x,(self.b).y,(self.b).z, (self.c).x,(self.c).y,(self.c).z)
    def I():
        a = Vector3(1,0,0)
        b = Vector3(0,1,0)
        c = Vector3(0,0,1)
        return Matrix3x3(a,b,c)
    def xR(self,n):
        self.a = (self.a).xR(n)
        self.b = (self.b).xR(n)
        self.c = (self.c).xR(n)
        return self
    def plusM(self,matr):
        self.a = (self.a).plusV(matr.a)
        self.b = (self.b).plusV(matr.b)
        self.c = (self.c).plusV(matr.c)
        return self
    def minusM(self,matr):
        self.a = (self.a).minusV(matr.a)
        self.b = (self.b).minusV(matr.b)
        self.c = (self.c).minusV(matr.c)
        return self
    def xV(self,vect):
        x = (self.a).dotV(vect)
        y = (self.b).dotV(vect)
        z = (self.c).dotV(vect)
        return Vector3(x,y,z)
    def xM(self,matr):
        a = Vector3((self.a).dotV(matr.column1),(self.a).dotV(matr.column2),(self.a).dotV(matr.column3))
        b = Vector3((self.b).dotV(matr.column1),(self.b).dotV(matr.column2),(self.b).dotV(matr.column3))
        c = Vector3((self.c).dotV(matr.column1),(self.c).dotV(matr.column2),(self.c).dotV(matr.column3))
        return Matrix3x3(a,b,c)

vect1 =Vector3(2.15, 3.64, 6.26)
vect2 =Vector3(73.25, -45.3, 6.13)
vect3 =Vector3(5.89, -2.25, 6.36)

vect12 =Vector3(26.672, -3478.263, 23.236)
vect22 =Vector3(-346.37, 874.347, -734.63)
vect32 =Vector3(457.27, 9283.36, -27.2678)

m1 = Matrix3x3(vect1,vect2,vect3)
m2 = Matrix3x3(vect12,vect22,vect32)

print(m1.xM(m2))

