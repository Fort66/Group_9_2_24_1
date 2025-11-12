from pygame import Surface
from pygame.key import get_pressed
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_w, K_s, K_a, K_d, K_c, K_k
from pygame.image import load
from pygame.transform import scale_by, rotozoom
from pygame.sprite import Sprite, groupcollide

from ..screens.class_Screen import win
from ..groups.class_SpritesGroups import groups
from ..groups.class_AllSprites import all_sprites
from .class_PlayerShoots import PlayerShoots
from .class_Explosions import Explosions

from icecream import ic

from time import time


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = scale_by(load('images/su-33.png').convert_alpha(), .2)
        self.image_rotation = self.image.copy()
        self.rect = self.image.get_rect(center=(
            win.screen.get_width() // 2,
            win.screen.get_height() // 2
        ))
        self.speed = 5
        self._layer = 2
        self.shoot_time = 1
        self.permission_shoot = 1
        groups.player_group.add(self)
        all_sprites.add(self)

    def move(self):
        keys = get_pressed()
        if True in keys:
            if keys[K_LEFT] or keys[K_a]:
                self.rect.move_ip(-self.speed, 0)

            if keys[K_RIGHT] or keys[K_d]:
                self.rect.move_ip(self.speed, 0)

            if keys[K_UP] or keys[K_w]:
                self.rect.move_ip(0, -self.speed)
                self.image_rotation = self.image.copy()
                self.image_rotation = rotozoom(self.image_rotation, 15, 1)
                self.rect = self.image_rotation.get_rect(center=self.rect.center)

            if keys[K_DOWN] or keys[K_s]:
                self.rect.move_ip(0, self.speed)
                self.image_rotation = self.image.copy()
                self.image_rotation = rotozoom(self.image_rotation, -15, 1)
                self.rect = self.image_rotation.get_rect(center=self.rect.center)

            if keys[K_c]:
                if not self.shoot_time:
                    self.shoot_time = time()
                if time() - self.shoot_time >= self.permission_shoot:
                    shoot = PlayerShoots((self.rect.centerx - 46, self.rect.centery + 10), 10)
                    groups.player_rocket_group.add(shoot)
                    all_sprites.add(shoot)
                    self.shoot_time = time()

            if keys[K_k]:
                self.rect.move_ip(-self.speed, 0)
                self.image_rotation = self.image.copy()
                self.image_rotation = rotozoom(self.image_rotation, 60, 1)
                self.rect = self.image_rotation.get_rect(center=self.rect.center)

        else:
            self.image_rotation = self.image.copy()
            self.image_rotation = rotozoom(self.image_rotation, 0, 1)
            self.rect = self.image_rotation.get_rect(center=self.rect.center)

    def check_position(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= win.screen.get_width():
            self.rect.right = win.screen.get_width()
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= win.screen.get_height():
            self.rect.bottom = win.screen.get_height()

    def collisions(self):
        rocket_collide = groupcollide(groups.player_rocket_group, groups.enemies_group, True, True)
        if rocket_collide:
            hits = list(rocket_collide.keys())
            self.explosion_rocket = Explosions(hits[0].rect.center, 1)
            self.explosion_rocket.speed = self.speed * -1


        # player_collide = groupcollide(groups.player_group, groups.enemies_group, True, True)

    def update(self):
        self.move()
        self.check_position()
        self.collisions()
        win.screen.blit(self.image_rotation, self.rect)