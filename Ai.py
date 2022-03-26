import pygame
import Functions


class Ai(pygame.sprite.Sprite):

    def __init__(self, name, x, y, colour, tilesize):
        super().__init__()
        self.name = "Ai" + str(name)
        self.x = x
        self.y = y
        self.image = pygame.Surface([tilesize, tilesize])
        self.image.fill(colour)
        self.rect = pygame.Rect((self.x, self.y), (tilesize, tilesize))
        self.tilesize = tilesize

    def updaterect(self):

        self.rect = pygame.Rect((self.x, self.y), (self.tilesize, self.tilesize))

    def drawself(self, screen):

        screen.blit(self.image, (self.x, self.y))

    def move(self, where):

        if where == "up":
            self.y -= self.tilesize
        if where == "down":
            self.y += self.tilesize
        if where == "left":
            self.x -= self.tilesize
        if where == "right":
            self.x += self.tilesize

        #print("moved " + where)

    def update(self, screen, endpointlist, framecount, intervaltimer):

        self.updaterect()
        self.drawself(screen)

        if framecount % intervaltimer == 0:
            self.howtomove(endpointlist)
            self.checkforcollide(endpointlist)

    def howtomove(self, endpointlist):
        if len(endpointlist) != 0:
            closest = None
            for i in endpointlist:

                if closest is None:
                    closest = i

                if i.name != closest.name:
                    if Functions.returnpositive(i.x) + Functions.returnpositive(self.x) < Functions.returnpositive(closest.x) + Functions.returnpositive(self.x):
                        if Functions.returnpositive(i.y) + Functions.returnpositive(self.y) < Functions.returnpositive(closest.y) + Functions.returnpositive(self.y):
                            closest = i
                    elif Functions.returnpositive(i.y) + Functions.returnpositive(self.y) < Functions.returnpositive(closest.y) + Functions.returnpositive(self.y):
                        if Functions.returnpositive(i.x) + Functions.returnpositive(self.x) < Functions.returnpositive(closest.x) + Functions.returnpositive(self.x):
                            closest = i



            xoffset = self.x - closest.x
            yoffset = self.y - closest.y
            print(closest.name)
            if Functions.returnpositive(xoffset) > Functions.returnpositive(yoffset):
                if xoffset < 0:
                    self.move("right")
                if xoffset > 0:
                    self.move("left")
                if xoffset == 0:
                    pass

            elif Functions.returnpositive(xoffset) == Functions.returnpositive(yoffset):
                if xoffset < 0:
                    self.move("right")
                if xoffset > 0:
                    self.move("left")
                if xoffset == 0:
                    pass
            else:
                if yoffset > 0:
                    self.move("up")
                if yoffset < 0:
                    self.move("down")
                if yoffset == 0:
                    pass


    def checkforcollide(self, endpointlist):
        for i in endpointlist:
            if i.x == self.x and i.y == self.y:
                i.kill()
