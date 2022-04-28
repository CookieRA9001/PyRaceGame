MENU = "main_menu"
GAME = "game"
SHOP = "car_shop"
TRACKS = "track_select"

mode = "main_menu" # menu / game / shop
init = ""
run = True
click = False
fps = 30
current_game = 0
money = 0
background_color = (48, 55, 62)
car_scaler = 0.5

upgrades = {
	"max_vel": 1,
	"bounc": 1,
	"rotation_vel": 1,
	"acceleration": 1,
}