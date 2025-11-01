import pygame as pg

from pygame.display import set_mode, set_caption

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN

from icecream import ic

from random import uniform

pg.init()

size = [1027, 768]

scr = set_mode(size)
set_caption('MyGame')

fps = 60
clock = pg.time.Clock()

class Player:
    def __init__(self):
        self.image = pg.Surface((50, 50))
        self.image.fill('SteelBlue')
        self.rect = self.image.get_rect(center=(
            scr.get_width() // 2,
            scr.get_height() // 2
        ))
        self.speed = 5

    def move(self):
        keys = pg.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)

        if keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

        if keys[K_UP]:
            self.rect.move_ip(0, -self.speed)

        if keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)

    def check_position(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= scr.get_width():
            self.rect.right = scr.get_width()
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= scr.get_height():
            self.rect.bottom = scr.get_height()

    def update(self):
        self.move()
        self.check_position()
        scr.blit(self.image, self.rect)


class Rockets:
    def __init__(self):
        self.image = pg.Surface((25, 25))
        self.image.fill('Maroon')
        self.rect = self.image.get_rect(center=(
                uniform(scr.get_width(), scr.get_width() + 1000),
                uniform(0, scr.get_height())
            ))
        self.speed = uniform(5, 15)

    def generate(self):
        if self.rect.left < -200:
            self.rect = self.image.get_rect(center=(
                uniform(scr.get_width(), scr.get_width() + 1000),
                uniform(0, scr.get_height())
            ))

    def move(self):
        self.rect.move_ip(-self.speed, 0)

    def update(self):
        self.move()
        self.generate()
        scr.blit(self.image, self.rect)

player = Player()


rokets = [Rockets() for _ in range(15)]



loop = True

while loop:
    scr.fill('black')

    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    player.update()

    for rocket in rokets:
        rocket.update()

    pg.display.update()
    clock.tick(fps)
pg.quit()