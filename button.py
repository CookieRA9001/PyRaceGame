from tkinter import font
import pygame
import utils
import defaults

pygame.init()

class Button():
	MOUSE_POS = (0,0)
	FONT = pygame.font.SysFont(None, 20)
	SCREEN = None
	ATLES = []
	BUTTON_IMG_CLICKED = utils.scale_image(pygame.image.load("imgs/button3.png"), 2)
	BUTTON_IMG_HOVER = utils.scale_image(pygame.image.load("imgs/button2.png"), 2)
	BUTTON_IMG_BASIC = utils.scale_image(pygame.image.load("imgs/button1.png"), 2)

	def init_class(font, screen, all_the_buttons_on_screen):
		Button.FONT = font
		Button.SCREEN = screen
		Button.ATLES = all_the_buttons_on_screen

	def run_all():
		Button.MOUSE_POS = pygame.mouse.get_pos()
		for btn in Button.ATLES:
			btn.render()
			if defaults.click:
				btn.click()

	def __init__(self, y, text):
		self.rect = pygame.Rect(50, y, 256, 64)
		self.y = y
		self.text = text

	def draw_text(text, color, surface, x, y):
		textobj = Button.FONT.render(text, 1, color)
		textrect = textobj.get_rect()
		textrect.topleft = (x, y)
		surface.blit(textobj, textrect)

	def click(self):
		if self.rect.collidepoint(Button.MOUSE_POS):
			print("No action defined!")
	
	def render(self):
		if self.rect.collidepoint(Button.MOUSE_POS):
			if defaults.click:
				Button.SCREEN.blit(Button.BUTTON_IMG_CLICKED, (50, self.y))
			else:
				Button.SCREEN.blit(Button.BUTTON_IMG_HOVER, (50, self.y))
		else:
			Button.SCREEN.blit(Button.BUTTON_IMG_BASIC, (50, self.y))

		Button.draw_text(self.text, (95, 205, 228), Button.SCREEN, 70, self.y+20)
		
class SceenButton(Button):
	def __init__(self, y, text, mode):
		self.mode = mode
		super().__init__(y, text)
	
	def click(self):
		if self.rect.collidepoint(Button.MOUSE_POS):
			defaults.mode = self.mode

class GameButton(Button):
	def __init__(self, y, text, game_index):
		self.game_index = game_index
		super().__init__(y, text)
	
	def click(self):
		if self.rect.collidepoint(Button.MOUSE_POS):
			defaults.current_game = self.game_index
			defaults.mode = defaults.GAME
	
class ShopButton(Button):
	def __init__(self, y, text, atr, start_price, increse, max_lv, upgrade_image):
		self.title = text
		self.atr = atr
		self.start_price = start_price
		self.increse = increse
		self.max_lv = max_lv
		self.level = defaults.upgrades[self.atr]
		self.upgrade_image = upgrade_image
		super().__init__(y, text)
	
	def click(self):
		if self.rect.collidepoint(Button.MOUSE_POS):
			if defaults.money >= self.start_price+(self.level-1)*self.increse:
				if self.level < self.max_lv:
					defaults.money -= self.start_price+(self.level-1)*self.increse
					self.level += 1
					defaults.upgrades[self.atr] += 1

	def render(self):
		if self.rect.collidepoint(Button.MOUSE_POS):
			Button.SCREEN.blit(self.upgrade_image, (350, 200))
			if defaults.click:
				Button.SCREEN.blit(Button.BUTTON_IMG_CLICKED, (50, self.y))
			else:
				Button.SCREEN.blit(Button.BUTTON_IMG_HOVER, (50, self.y))
		else:
			Button.SCREEN.blit(Button.BUTTON_IMG_BASIC, (50, self.y))
			
		if self.level < self.max_lv:
			self.text = self.title + " " + str(self.start_price+(self.level-1)*self.increse) + "$ Lv:" + str(self.level)
		else:
			self.text = self.title + " - Max Lv:" + str(self.level)
		
		Button.draw_text(self.text, (95, 205, 228), Button.SCREEN, 70, self.y+20)