import pygame as pg
pg.init()

from pygame.time import Clock
from pygame.event import get
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from .class_Screen import win
from .class_Player import Player
from .class_Enemies import Enemies
from .class_Clouds import Clouds


player = Player()
enemies = [Enemies() for _ in range(15)]
clouds = [Clouds() for _ in range(15)]



class Game:
    def __init__(self):
        self.fps = 60
        self.clock = Clock()
        self.loop = True


    def run(self):

        while self.loop:
            win.screen.fill('SkyBlue')

            for event in get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.loop = False

            player.update()

            for enemy in enemies:
                enemy.update()

            for cloud in clouds:
                cloud.update()

            pg.display.update()
            self.clock.tick(self.fps)
