from PIL import Image
import random
import math

def emc(m, c):
    """E=mc^2"""
    c = 299.792458
    return m*(math.pow(c,2))

def pytha(a, b):
    """a^2 + b^2 = c^2"""
    return math.sqrt(math.pow(a,2)*math.pow(b,2))

def random_color_emc():
    #return int(round(emc(random.randrange(0,10), random.randrange(0,5))))
    return int(round(emc(random.randrange(0,100), random.randrange(0,8))))

def random_color():
    #return int(round(emc(random.randrange(0,10), random.randrange(0,5))))
    return int(round(pytha(random.randrange(0,30), random.randrange(0,30))))


def random_color1():
    return random.randrange(0,255)

width = 500
height = 500

pixels = []

for p in range(width*height):
#    R = random.randrange(0,255)
#    G = random.randrange(0,255)
#    B = random.randrange(0,255)
    R = random_color()
    G = random_color()
    B = random_color()
    pixels.append((R,G,B))

#img = Image.new('RGB', (width, height), color = 'yellow')
img = Image.new('RGB', (width, height))
img.putdata(pixels)
img.save('pil_red.png')

#list_of_pixels = list(im.getdata())
## Do something to the pixels...
#im2 = Image.new(im.mode, im.size)
#im2.putdata(list_of_pixels)
#
#img = Image.new('RGB', (500, 500))
#img.putdata(my_list)
#img.save('image.png')

