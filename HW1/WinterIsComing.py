import random
from PIL import Image, ImageDraw

park = Image.open("park.jpg")
winter = Image.open("winter.jpg")
draw = ImageDraw.Draw(park)
width  = park.size[0]
height = park.size[1]
pix1 = park.load()
pix2 = winter.load()

start = width // 3
finish = start * 2

for x in range(width):
        for y in range(height):
            if x < start:
                r = pix1[x, y][0]
                g = pix1[x, y][1]
                b = pix1[x, y][2]
            elif x > finish:
                r = pix2[x, y][0]
                g = pix2[x, y][1]
                b = pix2[x, y][2]
            else:
                q = (x - start) / (finish - start)
                r = round(pix1[x, y][0]*(1 - q) + pix2[x, y][0]*q)
                g = round(pix1[x, y][1]*(1 - q) + pix2[x, y][1]*q)
                b = round(pix1[x, y][2]*(1 - q) + pix2[x, y][2]*q)
            draw.point((x, y), (r, g, b))
park.show()
del draw
