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

vect1 = Vector3(4,5,6)
vect2 = Vector3(1,2.5,4.7)
print(vect1.dotV(vect2))
