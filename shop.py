# Setup Python ----------------------------------------------- #
import pygame
from button import Button, ShopButton

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
	pygame.display.set_caption('Fix up your car')
	screen = pygame.display.set_mode((500, 500),0,32)
	font = pygame.font.SysFont(None, 20)

	UPGRADES = [
		ShopButton(160, 'Max Speed', 'max_vel', 100, 50, 5),
		ShopButton(220, 'Anti-Bounc', 'bounc', 100, 250, 5),
		ShopButton(280, 'Drift Speed', 'rotation_vel', 100, 100, 5),
		ShopButton(340, 'Acceleration', 'acceleration', 100, 150, 5)
	]
	Button.init_class(font, screen, UPGRADES)
 
def render():
	screen.fill(defaults.background_color)
	Button.draw_text('Car Upgrades! - ' + str(defaults.money) + "$", (255, 255, 255), screen, 50, 130)

	Button.run_all()

	pygame.display.update()
	mainClock.tick(defaults.fps)
 
render()