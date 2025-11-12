from random import choice

from ..units.class_Player import Player
from ..units.class_Enemies import Enemies
from ..units.class_Clouds import Clouds


clouds_list = [
    'images/clouds/cloud2.png',
    'images/clouds/cloud3.png',
    'images/clouds/cloud4.png',
    'images/clouds/cloud5.png'
]

planes_list = [
    ['images/planes/plane1.png', .11],
    ['images/planes/plane2.png', .11],
    ['images/planes/plane3.png', .11],
    ['images/planes/plane4.png', .13],
    ['images/planes/plane5.png', .13],
]

class CreateObjects:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def create(self):
        self.player = Player()
        self.enemies = [Enemies(choice(planes_list)) for _ in range(15)]
        self.clouds = [Clouds(choice(clouds_list)) for _ in range(15)]

create_objects = CreateObjects()