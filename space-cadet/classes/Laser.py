from typing import Union

import pygame

from classes.Enemy import Enemy
from classes.Player import Player
import config


class Laser:
    def __init__(self, x: int, y: int, img: pygame.Surface, speed: int = 5) -> None:
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        self.speed = speed
        self.enemy_height = 50

    def draw(self, window: pygame.Surface) -> None:
        """Draws the laser on its current x and y value."""
        window.blit(self.img, (self.x, self.y))

    def move(self) -> None:
        """Moves the laser forward."""
        self.y += self.speed

    def off_screen(self) -> bool:
        """Returns true if the laser is off screen, false otherwise"""
        return not (self.y <= config.HEIGHT and self.y + self.enemy_height >= 0)

    def has_collided(self, obj: Union[Enemy, Player]) -> bool:
        """Returns whether the laser has collided with an object."""
        offset_x = obj.x - self.x
        offset_y = obj.y - self.y
        return self.mask.overlap(obj.mask, (offset_x, offset_y)) != None
