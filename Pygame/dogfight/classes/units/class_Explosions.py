import gif_pygame as gif

from pygame.sprite import Sprite

from ..groups.class_AllSprites import all_sprites
from ..screens.class_Screen import win
from ..logic.class_Gifs import gifs


class Explosions(Sprite):
    def __init__(self, pos, types):
        Sprite.__init__(self)
        self._layer = 2
        self.speed = 0

        if types == 1:
            self.image = gifs.plane_explosion

        self.rect = self.image.get_rect(center=(pos))
        all_sprites.add(self)

    def move(self):
        self.rect.move_ip(self.speed, 0)

    def update(self):
        if not self.image._ended:
            self.image.render(win.screen, self.rect)
        else:
            self.kill()
        self.move()
