from pygame import Surface
from pygame.image import load
from pygame.transform import scale_by
from pygame.sprite import Sprite

from random import uniform

from ..screens.class_Screen import win
from ..groups.class_SpritesGroups import groups
from ..groups.class_AllSprites import all_sprites


class Enemies(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = scale_by(load('images/rocket.gif').convert_alpha(), .3)
        self.generate()
        self.speed = uniform(5, 10)
        self._layer = 2
        groups.enemies_group.add(self)
        all_sprites.add(self)

    def generate(self):
            self.rect = self.image.get_rect(center=(
                uniform(win.screen.get_width()+ 1000, win.screen.get_width() + 5000),
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