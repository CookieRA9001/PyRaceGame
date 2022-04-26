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
    pygame.display.set_caption('Pick a track!')
    screen = pygame.display.set_mode((500, 500),0,32)
    font = pygame.font.SysFont(None, 20)
 
def render():
    screen.fill((0,0,0))
    draw_text('Track Select', font, (255, 255, 255), screen, 20, 20)

    mx, my = pygame.mouse.get_pos()

    button_1 = pygame.Rect(50, 100, 256, 64)
    button_2 = pygame.Rect(50, 180, 256, 64)
    button_3 = pygame.Rect(50, 260, 256, 64)
    button_4 = pygame.Rect(50, 340, 256, 64)
    
    if defaults.click:
        if button_1.collidepoint((mx, my)):
            defaults.current_game = 0
            defaults.mode = defaults.GAME
        if button_2.collidepoint((mx, my)):
            defaults.current_game = 1
            defaults.mode = defaults.GAME
        if button_3.collidepoint((mx, my)):
            defaults.current_game = 2
            defaults.mode = defaults.GAME
        if button_4.collidepoint((mx, my)):
            defaults.current_game = 3
            defaults.mode = defaults.GAME

    pygame.draw.rect(screen, (255, 0, 0), button_1)
    draw_text('Defaut Track - Dif: 2 Laps: 5', font, (0, 0, 0), screen, 60, 130)
    pygame.draw.rect(screen, (255, 0, 0), button_2)
    draw_text('Test Track - Dif: 1 Laps: 2', font, (0, 0, 0), screen, 60, 210)
    pygame.draw.rect(screen, (255, 0, 0), button_3)
    draw_text('Waterfall - Dif: 4 Laps: 3', font, (0, 0, 0), screen, 60, 290)
    pygame.draw.rect(screen, (255, 0, 0), button_4)
    draw_text('Waterfall:border - Dif: 3 Laps: 3', font, (0, 0, 0), screen, 60, 370)

    pygame.display.update()
    mainClock.tick(defaults.fps)
 
render()