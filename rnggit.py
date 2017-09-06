import random

int = [[False, False, False, False, False],[False, False, False, False, False]]
middle = [False,False,False,False,False]
def generateImage():
    for i in range(0, len(int)):
        for x in range(0, len(int[i])):
            if random.randint(0,1) == 1:
                int[i][x] = True
        print int[i]
    for i in range(0, len(middle)):
        if random.randint(0,1) == 1:
            middle[i] = True
    print middle
    print int[1]
    print int[0]
            
            
        