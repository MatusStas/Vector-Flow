import pygame
import random
pygame.init()

running = True
FPS = 120
bg_color = (0, 0, 0)
(width, height) = (1000, 1000)
offset = 100
'''
matrix = [[[0.01,0.0025],[0.055,-0.015]],
          [[-0.02,0.015],[-0.02,-0.005]]]
'''




def make():
    matrix = [[]]
    for i in range(offset):
        matrix.append([])
        for j in range(offset):
            matrix[i].append([])
            if (j > i and i > 0):
                valueX = int(matrix[i-1][j][0]*1000)
                valueY = int(matrix[i-1][j][1]*1000)
                matrix[i][j].append(random.randint(valueX-20,valueX+20)/1000)
                matrix[i][j].append(random.randint(valueY-10,valueY+10)/1000)
            else:
                matrix[i][j].append(random.randint(-100, 100) / 1000)
                matrix[i][j].append(random.randint(-100, 100) / 1000)

    matrix.remove([])  # remove last []
    return matrix



class Point:
    def __init__(self, X,Y):
        self.X = X
        self.Y = Y
        self.xOffset = 0
        self.yOffset = 0
        self.XOffset = 0
        self.YOffset = 0

    def draw(self):
        self.xOffset += self.XOffset
        self.yOffset += self.YOffset
        self.X += self.xOffset
        self.Y += self.yOffset
        pygame.draw.circle(window,(255,255,255),(int(self.X),int(self.Y)),10,10)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vector Field")

P = []
matrix = make()

for j in range(50):
    co = []
    co.append(random.randint(0,width))
    co.append(random.randint(0,height))
    P.append(Point(co[0],co[1]))

sec = 0
pygame.display.flip()
while running:
    pygame.time.delay(int(1000/FPS))

    for e in pygame.event.get():
    	if e.type == pygame.QUIT:
    		pygame.quit()
    		exit()

    if (sec%3 == 0):
        co = []
        co.append(random.randint(1, width-1))
        co.append(random.randint(1, height-1))
        P.append(Point(co[0], co[1]))

    if (sec%240 == 0):
        matrix = make()

    sec += 1

    for k in P:
        if (k.X > width or k.X < 1 or k.Y > height or k.Y < 1):
            continue
        else:
            k.XOffset = matrix[int(k.Y/offset)][int(k.X/offset)][0]
            k.YOffset = matrix[int(k.Y/offset)][int(k.X/offset)][1]
    #print(p.xOffset,p.yOffset)
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
                break


    if (sec%(120*5) == 0):
        window.fill(bg_color)
    window.fill(bg_color)

    for l in P:
        l.draw()
    pygame.display.update()
