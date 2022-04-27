# Setup Python ----------------------------------------------- #
import pygame
import utils
from button import Button, SceenButton

# Setup pygame/window ---------------------------------------- #
from pygame.locals import *
import defaults

mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((500, 500),0,32)

def init_menu():
    global mainClock, screen
    mainClock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Py Race')
    screen = pygame.display.set_mode((500, 500),0,32)
    font = pygame.font.SysFont(None, 20)
    buttons = [
        SceenButton(160, 'Play', defaults.TRACKS),
        SceenButton(220, 'Shop', defaults.SHOP)
    ]
    Button.init_class(font, screen, buttons)
 
def main_menu():
    screen.fill(defaults.background_color)
    screen.blit(utils.scale_image(pygame.image.load("imgs/Title.png"), 2), (50, 20))
    Button.draw_text('"Esc" = "Back"', (255, 255, 255), screen, 50, 460)

    Button.run_all()

    pygame.display.update()
    mainClock.tick(defaults.fps)
 
main_menu()