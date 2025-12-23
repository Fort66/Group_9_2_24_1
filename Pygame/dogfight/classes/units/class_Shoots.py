from gif_pygame.transform import flip
from pygame.sprite import Sprite
from pygame import Vector2

from ..screens.class_Screen import win
from ..logic.class_Gifs import gifs
from ..units.class_Explosions import Explosions
from ..groups.class_AllSprites import all_sprites


from icecream import ic

class Shoots(Sprite):
    def __init__(self, pos, speed, owner):
        Sprite.__init__(self)
        if owner == 'Player':
            self.image = flip(gifs.rockets, True, False, new_gif=True)
        else:
            self.image = gifs.rockets
        self.pos = Vector2(pos)
        self.rect = self.image.get_rect(center=(self.pos))
        self.speed = speed
        self._layer = 2
        self.kill_shoot_distance = 300
        self.old_shoot_coordinates = Vector2(self.rect.center)
        self.direction = Vector2(1, 0)

    def move(self):
        # self.rect.move_ip(self.speed * self.di, 0)
        self.rect.move_ip(self.speed, 0)

    def check_position(self):
        if Vector2(self.rect.center).distance_to(self.old_shoot_coordinates) > self.kill_shoot_distance:
            self.kill_rockets = Explosions(pos=self.rect.center, types=1)
            self.kill_rockets.add(all_sprites)
            self.kill()

    def update(self):
        self.check_position()
        self.move()
        self.image.render(win.screen, self.rect)