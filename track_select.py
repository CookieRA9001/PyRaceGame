# Setup Python ----------------------------------------------- #
import pygame
from button import Button, GameButton
 
# Setup pygame/window ---------------------------------------- #
from pygame.locals import *
import defaults

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Pick a track!')
screen = pygame.display.set_mode((500, 500),0,32)

def init_menu():
    global mainClock, screen
    mainClock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Pick a track!')
    screen = pygame.display.set_mode((500, 500),0,32)
    font = pygame.font.SysFont(None, 20)
    buttons = [
        GameButton(160, 'Defaut Track - Dif: 2 Laps: 5', 0),
        GameButton(220, 'Test Track - Dif: 1 Laps: 2', 1),
        GameButton(280, 'Waterfall - Dif: 4 Laps: 3', 2),
        GameButton(340, 'Waterfall:border - Dif: 3 Laps: 3', 3)
    ]
    Button.init_class(font, screen, buttons)
 
def render():
    screen.fill(defaults.background_color)
    Button.draw_text('Track Select', (255, 255, 255), screen, 50, 130)

    Button.run_all()

    pygame.display.update()
    mainClock.tick(defaults.fps)
 
render()