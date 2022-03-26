import pygame
import Functions


class Endpoint(pygame.sprite.Sprite):

    def __init__(self, name, x, y, colour, tilesize):
        super().__init__()
        self.name = "Endpoint" + str(name)
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

    def update(self, screen, framecount, intervaltimer):

        self.updaterect()
        self.drawself(screen)


