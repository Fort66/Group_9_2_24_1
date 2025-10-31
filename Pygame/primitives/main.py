import pygame as pg

from pygame.display import set_mode, set_caption

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from math import pi

pg.init()


# width = 1024
# height = 768

size = [1027, 768]

scr = set_mode(size)
set_caption('MyGame')

loop = True

while loop:
    # scr.fill('SteelBlue')

    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

    pg.draw.line(scr, 'green', [50, 50], [250, 250], 1)
    pg.draw.rect(scr, 'red', [100, 100, 100, 100], 1)
    pg.draw.aaline(scr, 'yellow', [250, 50], [50, 250])
    
    pg.draw.lines(scr, 'blue', False, [[300, 50], [350, 100], [400, 50], [450, 100]], 1)
    pg.draw.aalines(scr, 'gray', False, [[300, 150], [350, 200], [400, 150], [450, 100]])
    
    pg.draw.polygon(scr, 'orange', [[500, 50], [550, 100], [600, 50], [650, 100]], 1)
    
    pg.draw.circle(scr, 'purple', [700, 100], 50, 1)
    pg.draw.ellipse(scr, 'pink', [400, 400, 50, 100], 1)
    
    pg.draw.arc(scr, 'MediumSlateBlue', [700, 400, 50, 100], 0, pi/2, 1)

    pg.display.update()
pg.quit()