import main_game, track_select, main_menu, shop
import pygame, sys
import defaults, utils
from pygame.locals import *
pygame.display.set_icon(pygame.image.load("imgs/Title.png"))

while defaults.run:
	defaults.click = False
	for event in pygame.event.get():
		if event.type == QUIT:
			defaults.run = False
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				defaults.mode = defaults.MENU
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				defaults.click = True
	
	if defaults.mode == defaults.MENU:
		if defaults.init != defaults.mode:
			main_menu.init_menu()
			defaults.init = defaults.mode
		main_menu.main_menu()

	elif defaults.mode == defaults.TRACKS:
		if defaults.init != defaults.mode:
			track_select.init_menu()
			defaults.init = defaults.mode
		track_select.render()

	elif defaults.mode == defaults.SHOP:
		if defaults.init != defaults.mode:
			shop.init_menu()
			defaults.init = defaults.mode
		shop.render()

	elif defaults.mode == defaults.GAME:
		if defaults.init != defaults.mode:
			main_game.init_game()
			defaults.init = defaults.mode
		main_game.play_game()