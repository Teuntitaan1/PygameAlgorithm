import pygame
import sys
import Ai
import Endpoint
import Functions
import random


pygame.init()

# img imports
WindowIcon = pygame.image.load("WindowIcon.png")

# colour settings
red = 255, 0, 0
blue = 0, 0, 255
black = 0, 0, 0
white = 255, 255, 255

# window settings
size = width, height = 800, 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_icon(WindowIcon)
pygame.display.set_caption("Moving Algorithm")
refreshrate = 60

tilesize = 40

# init statements
pygame.init()
ailist = pygame.sprite.Group()
endpointlist = pygame.sprite.Group()

# variable statements
poslist = Functions.generatelocation(width, height, tilesize)
poslistx = poslist[0]
poslisty = poslist[1]
framecount = 0

for i in range(3):
    ailist.add(Ai.Ai(i, poslistx[random.randint(0, (len(poslistx)-1))], poslisty[random.randint(0, (len(poslisty)-1))], red, tilesize))


for i in range(10):
    endpointlist.add(Endpoint.Endpoint(i, poslistx[random.randint(0, (len(poslistx)-1))], poslisty[random.randint(0, (len(poslisty)-1))], blue, tilesize))

# main loop
while 1:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # game check statements
    if len(endpointlist) == 0:
        for i in range(random.randint(0, 25)):
            endpointlist.add(Endpoint.Endpoint(i, poslistx[random.randint(0, (len(poslistx) - 1))], poslisty[random.randint(0, (len(poslisty) - 1))], blue, tilesize))


    # game update statements
    screen.fill(black)
    endpointlist.update(screen, framecount, 15)
    ailist.update(screen, endpointlist, framecount, 15)

    # screen update statements
    pygame.display.update()
    framecount += 1
    clock.tick(refreshrate)
