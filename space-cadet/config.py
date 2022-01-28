import pygame


WIDTH = 750
HEIGHT = 750
WINDOW: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND: pygame.Surface = pygame.transform.scale(
    pygame.image.load("assets/background-black.png"),
    (WIDTH, HEIGHT))

RED_SPACE_SHIP: pygame.Surface = pygame.image.load(
    "assets/pixel_ship_red_small.png")
GREEN_SPACE_SHIP: pygame.Surface = pygame.image.load(
    "assets/pixel_ship_green_small.png")
BLUE_SPACE_SHIP: pygame.Surface = pygame.image.load(
    "assets/pixel_ship_blue_small.png")
YELLOW_SPACE_SHIP: pygame.Surface = pygame.image.load(
    "assets/pixel_ship_yellow.png")

RED_LASER: pygame.Surface = pygame.image.load("assets/pixel_laser_red.png")
GREEN_LASER: pygame.Surface = pygame.image.load("assets/pixel_laser_green.png")
BLUE_LASER: pygame.Surface = pygame.image.load("assets/pixel_laser_blue.png")
YELLOW_LASER: pygame.Surface = pygame.image.load(
    "assets/pixel_laser_yellow.png")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLOR_MAP = {
    "red": (RED_SPACE_SHIP, RED_LASER),
    "green": (GREEN_SPACE_SHIP, GREEN_LASER),
    "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
}
