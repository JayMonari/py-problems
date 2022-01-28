from typing import Union

import pygame

from classes.Laser import Laser
from classes.Player import Player
from classes.Ship import Ship
import config


class Enemy(Ship):

    def __init__(self, x: int, y: int, color: str, health: int = 100) -> None:
        super().__init__(x, y, health)
        self.ship_img = config.COLOR_MAP[color][0]
        self.laser_img = config.COLOR_MAP[color][1]
        self.mask: pygame.Mask = pygame.mask.from_surface(self.ship_img)
        self.width = self.ship_img.get_width()
        self.height = self.ship_img.get_height()
        self.speed = 1
        self.laser_speed = 3

    def move(self) -> None:
        self.y += self.speed

    def shoot(self) -> None:
        if self.cool_down_counter == 0:
            self.cool_down_counter = 1
            self.lasers.append(
                Laser(self.x - 20, self.y, self.laser_img, self.laser_speed)
            )

    def move_lasers(self, player: Player) -> None:
        self.cooldown()
        for laser in self.lasers:
            laser.move()
            if laser.off_screen():
                self.lasers.remove(laser)
            elif laser.has_collided(player):
                player.health -= 10
                self.lasers.remove(laser)

    def has_collided(self, obj: Union[Player, Laser]) -> bool:
        offset_x = obj.x - self.x
        offset_y = obj.y - self.y
        return self.mask.overlap(obj.mask, (offset_x, offset_y)) != None
