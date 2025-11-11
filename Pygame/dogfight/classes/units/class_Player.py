from pygame import Surface
from pygame.key import get_pressed
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_w, K_s, K_a, K_d, K_c
from pygame.image import load
from pygame.transform import scale_by
from pygame.sprite import Sprite



from ..screens.class_Screen import win
from ..groups.class_SpritesGroups import groups
from ..groups.class_AllSprites import all_sprites
from .class_PlayerShoots import PlayerShoots

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = scale_by(load('images/su-33.png').convert_alpha(), .2)
        self.rect = self.image.get_rect(center=(
            win.screen.get_width() // 2,
            win.screen.get_height() // 2
        ))
        self.speed = 5
        self._layer = 2
        groups.player_group.add(self)
        all_sprites.add(self)

    def move(self):
        keys = get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            self.rect.move_ip(-self.speed, 0)

        if keys[K_RIGHT] or keys[K_d]:
            self.rect.move_ip(self.speed, 0)

        if keys[K_UP] or keys[K_w]:
            self.rect.move_ip(0, -self.speed)

        if keys[K_DOWN] or keys[K_s]:
            self.rect.move_ip(0, self.speed)

        if keys[K_c]:
            shoot = PlayerShoots((self.rect.centerx - 46, self.rect.centery + 10), 10)
            all_sprites.add(shoot)

    def check_position(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= win.screen.get_width():
            self.rect.right = win.screen.get_width()
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= win.screen.get_height():
            self.rect.bottom = win.screen.get_height()

    def update(self):
        self.move()
        self.check_position()
        win.screen.blit(self.image, self.rect)