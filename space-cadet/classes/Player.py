from typing import List

import pygame

from classes.Enemy import Enemy
from classes.Laser import Laser
from classes.Ship import Ship
import config


class Player(Ship):
    MARGIN = 10

    def __init__(self, x: int, y: int, health: int = 100) -> None:
        super().__init__(x, y, health)
        self.ship_img: pygame.Surface = config.YELLOW_SPACE_SHIP
        self.laser_img: pygame.Surface = config.YELLOW_LASER
        self.mask: pygame.Mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.width = self.ship_img.get_width()
        self.height = self.ship_img.get_height()
        self.speed = 5
        self.lives = 5
        self.laser_speed = 5

    def move_lasers(self, enemies: List[Enemy]) -> None:
        self.cooldown()
        for laser in self.lasers:
            laser.move()
            if laser.off_screen():
                self.lasers.remove(laser)
                return

            for enemy in enemies:
                if laser.has_collided(enemy):
                    enemies.remove(enemy)
                    if laser in self.lasers:
                        self.lasers.remove(laser)

    def move_left(self) -> None:
        is_inbounds_left = self.x - self.speed > 0
        if is_inbounds_left:
            self.x -= self.speed

    def move_right(self) -> None:
        is_inbounds_right = self.x + self.speed + self.width < config.WIDTH
        if is_inbounds_right:
            self.x += self.speed

    def move_up(self) -> None:
        is_inbounds_up = self.y - self.speed > 0
        if is_inbounds_up:
            self.y -= self.speed

    def move_down(self) -> None:
        is_inbounds_down = self.y + self.speed + self.height + 25 < config.HEIGHT
        if is_inbounds_down:
            self.y += self.speed

    def draw(self, window: pygame.Surface) -> None:
        super().draw(window)
        self.healthbar(window)

    def shoot(self) -> None:
        if not self.cool_down_counter == 0:
            return
        self.cool_down_counter = 1
        laser = Laser(self.x, self.y, self.laser_img, -self.laser_speed)
        self.lasers.append(laser)

    def healthbar(self, window: pygame.Surface) -> None:
        current_health = self.health / self.max_health
        full_width = self.width * current_health
        margin_top = self.y + self.height + self.MARGIN
        missing_health_dimensions = (self.x, margin_top, self.width, 10)
        full_health_dimensions = (self.x, margin_top, full_width, 10)
        pygame.draw.rect(window, config.RED, missing_health_dimensions)
        pygame.draw.rect(window, config.GREEN, full_health_dimensions)
