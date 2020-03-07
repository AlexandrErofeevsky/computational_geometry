import random
from math import sqrt
from PIL import Image, ImageDraw #Подключим необходимые библиотеки

image = Image.open("park.jpg") #Открываем изображение
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования
width  = image.size[0] #Определяем ширину
height = image.size[1] #Определяем высоту
pix = image.load() #Выгружаем значения пикселей
image2 = Image.open("winter.jpg") #Открываем изображение
draw2 = ImageDraw.Draw(image) #Создаем инструмент для рисования
width2  = image.size[0] #Определяем ширину
height2 = image.size[1] #Определяем высоту
pix2 = image.load() #Выгружаем значения пикселей

start = 480
finish = 960

for x in range(width):
        for y in range(height):
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                r2 = pix2[x, y][0]
                g2 = pix2[x, y][1]
                b2 = pix2[x, y][2]
                
                if x<start:
                    draw.point((x, y), (r, g, b))
                elif (x>start) and (x<finish):
                    q = (x-start)//(finish-start)
                    draw.point((x, y), (r*(1-q)+r2*q, g*(1-q)+g2*q, b*(1-q)+b2*q))


for x in range(width2):
        for y in range(height2):
                r2 = pix2[x, y][0]
                g2 = pix2[x, y][1]
                b2 = pix2[x, y][2]

                if x>finish:
                    draw.point((x, y), (r2, g2, b2))

image.show()
del draw
