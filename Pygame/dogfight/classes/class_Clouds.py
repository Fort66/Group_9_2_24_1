from pygame import Surface
from pygame.image import load
from pygame.transform import scale_by

from random import uniform, choice

from .class_Screen import win

clouds_list = [
    'images/cloud2.png',
    'images/cloud3.png',
    'images/cloud4.png',
    'images/cloud5.png'
]


class Clouds:
    def __init__(self):
        self.image = scale_by(load(choice(clouds_list)).convert_alpha(), .8)
        self.generate()
        self.speed = uniform(2, 4)

    def generate(self):
            self.rect = self.image.get_rect(center=(
                uniform(win.screen.get_width() + 1000, win.screen.get_width() + 5000),
                uniform(0, win.screen.get_height())
            ))

    def move(self):
        if self.rect.left > -2000:
            self.rect.move_ip(-self.speed, 0)
        else:
            self.generate()

    def update(self):
        self.move()
        win.screen.blit(self.image, self.rect)