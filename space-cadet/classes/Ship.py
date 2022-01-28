from typing import List, Optional

import pygame

from classes.Laser import Laser


class Ship:
    COOLDOWN = 30

    def __init__(self, x: int, y: int, health: int = 100) -> None:
        self.x = x
        self.y = y
        self.health = health
        self.ship_img: Optional[pygame.Surface] = None
        self.laser_img = None
        self.lasers: List[Laser] = []
        self.cool_down_counter = 0

    def draw(self, window: pygame.Surface) -> None:
        if self.ship_img:
            window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def cooldown(self) -> None:
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
