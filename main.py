# The main file for a implementation of the classic arcade game Space Invaders.

# All the imports needed.
import pygame
import random
import os
import time

pygame.font.init()

# The width and Height of the window.
WIDTH, HEIGHT = 750, 750

# Load all Images
RED_SPACE_SHIP = pygame.image.load(os.path.join("Images", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("Images", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("Images", "pixel_ship_blue_small.png"))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("Images", "pixel_ship_yellow.png"))
RED_LASER = pygame.image.load(os.path.join("Images", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("Images", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("Images", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("Images", "pixel_laser_yellow.png"))
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Images", "background-black.png")), (WIDTH, HEIGHT))

# Initiate the window.
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Space Invaders v1")


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_height(self):
        return self.ship_img.get_height()

    def get_width(self):
        return self.ship_img.get_width()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health


def main():
    running = True
    FPS = 60
    level = 1
    lives = 10
    main_font = pygame.font.SysFont("comicsans", 40)
    gameClock = pygame.time.Clock()
    player = Player(300, 650)
    playerVelocity = 5

    def redraw_window():
        WIN.blit(BACKGROUND, (0, 0))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 0, 0))
        level_label = main_font.render(f"Level: {level}", 1, (255, 0, 0))
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        player.draw(WIN)
        pygame.display.update()

    while running:
        gameClock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - playerVelocity > 0:
            player.x -= playerVelocity
        if keys[pygame.K_d] and player.x + playerVelocity + player.get_width() < WIDTH:
            player.x += playerVelocity
        if keys[pygame.K_w] and player.y - playerVelocity > 0:
            player.y -= playerVelocity
        if keys[pygame.K_s] and player.y + playerVelocity + player.get_height() < HEIGHT:
            player.y += playerVelocity


main()
