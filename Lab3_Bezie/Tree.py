import random
from PIL import Image, ImageDraw #Подключим необходимые библиотеки
from math import pi, sin, cos

def sign(x): # знак числа
        if x > 0:
                return 1
        if x < 0:
                return -1
        return 0
def line(x1, y1, x2, y2):  # рисуем линию из точки (x1,y1) в точку (x2,y2)
        dX = abs(x2 - x1)
        dY = abs(y2 - y1)
        if dX >= dY: # если наклон по X больше Y, то X меняем на 1 и смотрим Y
            if x1 > x2: # если точка 2 правее точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dY
            y = y1
            dirY = sign(y2 - y1)
            for x in range(x1, x2 + 1):
                    draw.point((x,y),(0,0,0))
                    err += dErr
                    if err + err >= dX:
                            y += dirY
                            err -= dX
        else: # если наклон по Y больше, то, наоборот, Y меняем на 1 и смотрим X
            if y1 > y2: # если точка 2 ближе точки 1, меняем их местами
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
            err = 0 # накапливаемая "ошибка"
            dErr = dX
            x = x1
            dirX = sign(x2 - x1)
            for y in range(y1, y2 + 1):
                    draw.point((x,y),(0,0,0))
                    err += dErr
                    if err + err >= dY:
                            x += dirX
                            err -= dY

class tartilla():
    def __init__(self):
        self.direction = 0
        self.x = 50
        self.y = 500
    def right(self, angle):
        self.direction += angle
        self.direction = self.direction % 360
    def fd(self, distance):
        old_x = self.x
        old_y = self.y
        self.x += distance * cos(self.direction/180*pi)
        self.y += distance * sin(self.direction/180*pi)
        line(round(old_x), round(old_y), round(self.x), round(self.y))

def fractal(paint,length,iterations):
    if iterations == 1:
        paint.fd(length)
        paint.fd(-length)
    else:
        paint.fd(length//2)
        paint.right(-30)
        fractal(paint,length//2,iterations-1)
        paint.right(30)
        paint.fd(length//4)
        paint.right(30)
        fractal(paint,length//2,iterations-1)
        paint.right(-30)
        paint.fd(length//4)
        paint.right(-30)
        fractal(paint,length//2,iterations-1)
        paint.right(30)
        paint.fd(-length)
        
image = Image.open("white_picture.png") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину 
height = image.size[1] #Определяем высоту 	
pix = image.load() #Выгружаем значения пикселей

paint = tartilla()

fractal(paint, 1000, 10)

image.show()
del draw
