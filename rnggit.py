import random
from PIL import Image

image_rgb_data = [[False, False, False, False, False],[False, False, False, False, False],[False,False,False,False,False],[False, False, False, False, False],[False,False,False,False,False]]
def generateImage():
    for i in range(0, 2):
        for x in range(0, len(image_rgb_data[i])):
            if random.randint(0,1) == 1:
                image_rgb_data[i][x] = True
    for i in range(0, len(image_rgb_data[2])):
        if random.randint(0,1) == 1:
            image_rgb_data[2][i] = True
    image_rgb_data[3] = image_rgb_data[1]
    image_rgb_data[4] = image_rgb_data[0]
    
    showImage()
    

def showImage():
    img = Image.new( 'RGB', (5,5), "white")
    pixels = img.load()
    for i in range(img.size[0]):
        for x in range(img.size[1]):
            if (image_rgb_data[i][x]):
                pixels[i,x] = (175, 175, 100)
    img.show()
