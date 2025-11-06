from pygame import Surface
from pygame.image import load
from pygame.transform import scale_by

from random import uniform

from .class_Screen import win

class Enemies:
    def __init__(self):
        self.image = scale_by(load('images/rocket.gif').convert_alpha(), .3)
        self.generate()
        self.speed = uniform(5, 15)

    def generate(self):
            self.rect = self.image.get_rect(center=(
                uniform(win.screen.get_width(), win.screen.get_width() + 1000),
                uniform(0, win.screen.get_height())
            ))

    def move(self):
        if self.rect.left > -200:
            self.rect.move_ip(-self.speed, 0)
        else:
            self.generate()

    def update(self):
        self.move()
        win.screen.blit(self.image, self.rect)