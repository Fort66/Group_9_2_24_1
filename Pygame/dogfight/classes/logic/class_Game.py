import pygame as pg
pg.init()

from pygame.time import Clock
from pygame.event import get
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_F2

from ..screens.class_Screen import win
from ..groups.class_AllSprites import all_sprites
from ..groups.class_SpritesGroups import groups
from ..screens.class_StartScreen import start_screen
from ..screens.class_PauseScreen import pause_screen
from ..screens.class_GameOverScreen import game_over_screen
from .class_Signals import signals




class Game:
    def __init__(self):
        self.fps = 60
        self.clock = Clock()
        self.loop = True

    def clear_groups(self):
        groups.clear()
        all_sprites.empty()

    def run(self):

        while self.loop:
            win.screen.fill('SkyBlue')

            for event in get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.loop = False
                if event.type == KEYDOWN and event.key == K_F2:
                    signals.change_signals('pause')


            if signals.start:
                start_screen.update()

            elif signals.pause:
                pause_screen.update()

            elif signals.game_over:
                game_over_screen.update()

            else:
                all_sprites.update()

            pg.display.update()
            self.clock.tick(self.fps)
