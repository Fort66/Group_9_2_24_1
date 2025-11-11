from pygame.sprite import Group, GroupSingle

from icecream import ic

class SpritesGroups:
    __instance = None

    __groups_dict = {
        'player_group': GroupSingle(),
        'player_rocket_group': Group(),
        'enemies_group': Group(),
    }


    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.__dict__ = self.__groups_dict

    def sprites(self):
        return list(self.__dict__)

    def clear(self):
        for group in self.__dict__.values():
            group.empty()


groups = SpritesGroups()


