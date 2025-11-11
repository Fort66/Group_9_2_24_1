from pygame import Surface
from pygame.image import load
from pygame.transform import scale_by, flip
from pygame.sprite import Sprite

from ..screens.class_Screen import win


class PlayerShoots(Sprite):
    def __init__(self, pos, speed):
        Sprite.__init__(self)
        self.image = flip(scale_by(load('images/rocket.gif').convert_alpha(), .3), True, False)
        self.rect = self.image.get_rect(center=(pos))
        self.pos = pos
        self.speed = speed
        self._layer = 2

    def move(self):
        if self.rect.right < win.screen.get_width() + 200:
            self.rect.move_ip(self.speed, 0)
        else:
            self.kill()

    def update(self):
        self.move()
        win.screen.blit(self.image, self.rect)