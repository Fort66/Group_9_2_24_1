from pygame.display import set_mode, set_caption
from pygame.locals import DOUBLEBUF


class Screen:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        self.screen = set_mode([1920, 1080], DOUBLEBUF)
        self.caption = set_caption('My Game')



win = Screen()