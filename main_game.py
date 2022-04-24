from asyncio.windows_events import NULL
import pygame, sys
from pygame.locals import *
import time
import math
import defaults
from utils import scale_image, blit_rotate_center, blit_text_center

RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.55)

clock = pygame.time.Clock()
images = []
player_car = NULL
computer_car = NULL

class Game:
    def __init__(self, path, finish_pos, track, bg, border, finish, title, levels):
        pygame.font.init()
        self.PATH = path
        self.FINISH_POSITION = finish_pos
        self.TRACK = track
        self.GRASS = bg
        self.TRACK_BORDER = border
        self.TRACK_BORDER_MASK = pygame.mask.from_surface(self.TRACK_BORDER)
        self.FINISH = finish
        self.END_LEVEL = levels
        self.LEVEL = 1
        self.TITLE = title
        self.started = False
        self.level_start_time = 0

        self.FINISH_MASK = pygame.mask.from_surface(self.FINISH)
        self.WIDTH, self.HEIGHT = self.TRACK.get_width(), self.TRACK.get_height()
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.MAIN_FONT = pygame.font.SysFont("comicsans", 44)

    def start(self):
        global images
        pygame.display.set_caption(self.TITLE)

        images = [(self.GRASS, (0, 0)), (self.TRACK, (0, 0)),
          (self.FINISH, self.FINISH_POSITION), (self.TRACK_BORDER, (0, 0))]

    def next_level(self):
        self.LEVEL += 1
        self.started = False

    def reset(self):
        self.LEVEL = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self):
        return self.LEVEL > self.END_LEVEL

    def start_level(self):
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self):
        if not self.started:
            return 0
        return round(time.time() - self.level_start_time)

class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0

class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel
        self.move()

class ComputerCar(AbstractCar):
    IMG = GREEN_CAR
    START_POS = (150, 200)

    def __init__(self, max_vel, rotation_vel, path=[]):
        super().__init__(max_vel, rotation_vel)
        self.path = path
        self.current_point = 0
        self.vel = max_vel

    def draw_points(self, win):
        for point in self.path:
            pygame.draw.circle(win, (255, 0, 0), point, 5)

    def draw(self, win):
        super().draw(win)
        # self.draw_points(win)

    def calculate_angle(self):
        target_x, target_y = self.path[self.current_point]
        x_diff = target_x - self.x
        y_diff = target_y - self.y

        if y_diff == 0:
            desired_radian_angle = math.pi / 2
        else:
            desired_radian_angle = math.atan(x_diff / y_diff)

        if target_y > self.y:
            desired_radian_angle += math.pi

        difference_in_angle = self.angle - math.degrees(desired_radian_angle)
        if difference_in_angle >= 180:
            difference_in_angle -= 360

        if difference_in_angle > 0:
            self.angle -= min(self.rotation_vel, abs(difference_in_angle))
        else:
            self.angle += min(self.rotation_vel, abs(difference_in_angle))

    def update_path_point(self):
        target = self.path[self.current_point]
        rect = pygame.Rect(
            self.x, self.y, self.img.get_width(), self.img.get_height())
        if rect.collidepoint(*target):
            self.current_point += 1

    def move(self):
        if self.current_point >= len(self.path):
            return

        self.calculate_angle()
        self.update_path_point()
        super().move()

    def next_level(self, level):
        self.reset()
        self.vel = self.max_vel + (level - 1) * 0.2
        self.current_point = 0

GAMES = []
CurentGame = NULL
player_car = PlayerCar(4, 4)
computer_car = ComputerCar(2, 4, [])

def init_game():
    global GAMES, CurentGame, computer_car, player_car
    GAMES = [
        Game(
            [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
            (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)],
            (130, 250),
            scale_image(pygame.image.load("imgs/track.png"), 0.9),
            scale_image(pygame.image.load("imgs/grass.jpg"), 2.5),
            scale_image(pygame.image.load("imgs/track-border.png"), 0.9),
            pygame.image.load("imgs/finish.png"),
            "Racing Game!",
            10
        )
    ]
    CurentGame = GAMES[0]
    CurentGame.start()
    player_car = PlayerCar(4, 4)
    computer_car = ComputerCar(2, 4, CurentGame.PATH)

def draw(win, images, player_car, computer_car):
    for img, pos in images:
        win.blit(img, pos)

    level_text = CurentGame.MAIN_FONT.render(
        f"Level {CurentGame.LEVEL}", 1, (255, 255, 255))
    win.blit(level_text, (10, CurentGame.HEIGHT - level_text.get_height() - 70))

    time_text = CurentGame.MAIN_FONT.render(
        f"Time: {CurentGame.get_level_time()}s", 1, (255, 255, 255))
    win.blit(time_text, (10, CurentGame.HEIGHT - time_text.get_height() - 40))

    vel_text = CurentGame.MAIN_FONT.render(
        f"Speed: {round(player_car.vel, 1)}px/s", 1, (255, 255, 255))
    win.blit(vel_text, (10, CurentGame.HEIGHT - vel_text.get_height() - 10))

    player_car.draw(win)
    computer_car.draw(win)
    pygame.display.update()


def move_player(player_car):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()

    if not moved:
        player_car.reduce_speed()


def handle_collision(player_car, computer_car):
    if player_car.collide(CurentGame.TRACK_BORDER_MASK) != None:
        player_car.bounce()

    computer_finish_poi_collide = computer_car.collide(
        CurentGame.FINISH_MASK, *CurentGame.FINISH_POSITION)
    if computer_finish_poi_collide != None:
        blit_text_center(CurentGame.WIN, CurentGame.MAIN_FONT, "You lost!")
        pygame.display.update()
        pygame.time.wait(5000)
        CurentGame.reset()
        player_car.reset()
        computer_car.reset()

    player_finish_poi_collide = player_car.collide(
        CurentGame.FINISH_MASK, *CurentGame.FINISH_POSITION)
    if player_finish_poi_collide != None:
        if player_finish_poi_collide[1] == 0:
            player_car.bounce()
        else:
            CurentGame.next_level()
            player_car.reset()
            computer_car.next_level(CurentGame.LEVEL)

def play_game():
    clock.tick(defaults.fps)

    draw(CurentGame.WIN, images, player_car, computer_car)

    while not CurentGame.started:
        blit_text_center(CurentGame.WIN, CurentGame.MAIN_FONT, f"Press any key to start level {CurentGame.LEVEL}!")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                defaults.run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                CurentGame.start_level()

    move_player(player_car)
    computer_car.move()

    handle_collision(player_car, computer_car)

    if CurentGame.game_finished():
        blit_text_center(CurentGame.WIN, CurentGame.MAIN_FONT, "You won the game!")
        pygame.time.wait(5000)
        CurentGame.reset()
        player_car.reset()
        computer_car.reset()


pygame.quit()
