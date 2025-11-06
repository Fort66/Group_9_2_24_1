from pygame import Surface
from pygame.image import load
from pygame.transform import scale_by

from random import uniform

from .class_Screen import win

class Enemies:
    def __init__(self):
        # self.image = Surface((25, 5))
        # self.image.fill('Maroon')
        self.image = scale_by(load('images/rocket.gif').convert_alpha(), .3)
        self.rect = self.image.get_rect(center=(
                uniform(win.screen.get_width(), win.screen.get_width() + 1000),
                uniform(0, win.screen.get_height())
            ))
        self.speed = uniform(5, 15)

    def generate(self):
        if self.rect.left < -200:
            self.rect = self.image.get_rect(center=(
                uniform(win.screen.get_width(), win.screen.get_width() + 1000),
                uniform(0, win.screen.get_height())
            ))

    def move(self):
        self.rect.move_ip(-self.speed, 0)

    def update(self):
        self.move()
        self.generate()
        win.screen.blit(self.image, self.rect)