# Setup Python ----------------------------------------------- #
import pygame
 
# Setup pygame/window ---------------------------------------- #
from pygame.locals import *
import defaults

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def init_menu():
    global mainClock, screen, font
    mainClock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('game base')
    screen = pygame.display.set_mode((500, 500),0,32)
    font = pygame.font.SysFont(None, 20)
 
def main_menu():
    screen.fill((0,0,0))
    draw_text('Python Race', font, (255, 255, 255), screen, 20, 20)

    mx, my = pygame.mouse.get_pos()

    button_1 = pygame.Rect(50, 100, 200, 50)
    button_2 = pygame.Rect(50, 200, 200, 50)
    
    if defaults.click:
        if button_1.collidepoint((mx, my)):
            defaults.mode = defaults.TRACKS
        if button_2.collidepoint((mx, my)):
            defaults.mode = defaults.SHOP
    pygame.draw.rect(screen, (255, 0, 0), button_1)
    draw_text('Play', font, (0, 0, 0), screen, 60, 120)
    pygame.draw.rect(screen, (255, 0, 0), button_2)
    draw_text('Shop', font, (0, 0, 0), screen, 60, 220)

    pygame.display.update()
    mainClock.tick(defaults.fps)
 
main_menu()