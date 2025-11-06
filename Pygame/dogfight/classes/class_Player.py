from pygame import Surface
from pygame.key import get_pressed
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_w, K_s, K_a, K_d
from pygame.image import load
from pygame.transform import scale_by

from .class_Screen import win

class Player:
    def __init__(self):
        self.image = scale_by(load('images/su-33.png').convert_alpha(), .2)
        self.rect = self.image.get_rect(center=(
            win.screen.get_width() // 2,
            win.screen.get_height() // 2
        ))
        self.speed = 5

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