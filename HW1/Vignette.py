import random
from PIL import Image, ImageDraw
from math import sqrt

image = Image.open("park.jpg")
draw = ImageDraw.Draw(image)
width  = image.size[0]
height = image.size[1]
pix = image.load()

start = (height / 2)**2 / (height / 3)**2
finish = 1

for x in range(width):
        for y in range(height):
            q1 = (x - width / 2)**2 / (width / 2)**2 + (y - height / 2)**2 / (height / 2)**2
            q2 = (x - width / 2)**2 / (width / 3)**2 + (y - height / 2)**2 / (height / 3)**2
            if q1 > 1:
                draw.point((x, y), (255, 255, 255))
            elif q2 < 1:
                r = pix[x, y][0]
                g = pix[x, y][1]
                b = pix[x, y][2]
                draw.point((x, y), (r, g, b))
            else:
                q = (q2 - finish)/(start - finish)
                r = round(pix[x, y][0]*(1 - q) + 255*(q))
                g = round(pix[x, y][1]*(1 - q) + 255*(q))
                b = round(pix[x, y][2]*(1 - q) + 255*(q))
                draw.point((x, y), (r, g, b))
image.show()
del draw
