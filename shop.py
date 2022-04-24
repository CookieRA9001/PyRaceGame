# Setup Python ----------------------------------------------- #
import pygame

# Setup pygame/window ---------------------------------------- #
from pygame.locals import *
import defaults

mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((500, 500),0,32)

font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

class Upgrade():
	index = 0

	def __init__(self, title, atr, start_price, increse, max_lv):
		self.title = title
		self.atr = atr
		self.start_price = start_price
		self.increse = increse
		self.max_lv = max_lv
		self.level = 1
		self.my_index = Upgrade.index
		self.rect = pygame.Rect(50, 100+80*self.my_index, 200, 50)
		Upgrade.index += 1
	
	def draw(self):
		pygame.draw.rect(screen, (255, 0, 0), self.rect)
		draw_text(self.title + " " + str(self.start_price+(self.level-1)*self.increse) + "$ Lv:"+str(self.level), font, (0, 0, 0), screen, 60, 120+80*self.my_index)

	def click(self, mx, my):
		if self.rect.collidepoint((mx, my)):
			print("click" + self.atr)

UPGRADES = []

def init_menu():
	global mainClock, screen, font, UPGRADES
	mainClock = pygame.time.Clock()
	pygame.init()
	pygame.display.set_caption('Fix up you car!')
	screen = pygame.display.set_mode((500, 500),0,32)
	font = pygame.font.SysFont(None, 20)

	Upgrade.index = 0
	UPGRADES = [
		Upgrade("Max Speed", "max_vel", 100, 50, 10),
		Upgrade("Anti-Bounc", "bounc", 100, 200, 5),
		Upgrade("Drift Speed", "rotation_vel", 100, 100, 5),
		Upgrade("Acceleration", "acceleration", 100, 100, 5),
	]
 
def render():
	screen.fill((0,0,0))
	draw_text('Car Upgrades', font, (255, 255, 255), screen, 20, 20)

	mx, my = pygame.mouse.get_pos()
	for u in UPGRADES:
		if defaults.click:
			u.click(mx, my)
		u.draw()

	pygame.display.update()
	mainClock.tick(defaults.fps)
 
render()