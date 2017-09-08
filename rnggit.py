import random
import os
from PIL import Image

image_rgb_data = [[False, False, False, False, False],[False, False, False, False, False],[False,False,False,False,False],[False, False, False, False, False],[False,False,False,False,False]]
def generateImage():
    for i in range(0, 2):
        for x in range(0, len(image_rgb_data[i])):
            image_rgb_data[i][x] = random.randint(0,50) >= 30
    for i in range(0, len(image_rgb_data[2])):
        image_rgb_data[2][i] = random.randint(0,50) >= 33
    image_rgb_data[3] = image_rgb_data[1]
    image_rgb_data[4] = image_rgb_data[0]
    
    showImage()
    

def showImage():
    file_path = "images/"
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
    img = Image.new( 'RGB', (500,500), "white")
    pixels = img.load()
    for i in range(img.size[0]):
        for x in range(img.size[1]):
            if (image_rgb_data[int(i/100)][int(x/100)]):
                pixels[i,x] = (175, 175, 100)
    img.show()
    img.save('images/' + str(random.randint(0, 999999999)) + '.png')
