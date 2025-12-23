from gif_pygame import load
from gif_pygame.transform import scale_by, flip


class Gifs:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.plane_explosion = scale_by(load('images/explosions/rocket_explosion.gif', loops=0), .5, new_gif=True)
        self.rockets = scale_by(load('images/rocket.gif'), .3, new_gif=True)



gifs = Gifs()