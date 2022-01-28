#!/usr/bin/env python3

import random
from typing import List

import pygame

from classes.Enemy import Enemy
from classes.Player import Player
import config


pygame.display.set_caption("Space Cadet")
pygame.font.init()


def main() -> None:
    run = True
    FPS = 60
    level = 0
    main_font: pygame.Font = pygame.font.SysFont("monospace", 50)
    lost_font: pygame.Font = pygame.font.SysFont("monospace", 60)

    enemies: List[Enemy] = []
    wave_length = 5

    player = Player(300, 630)

    clock: pygame.Clock = pygame.time.Clock()

    has_lost = False
    lost_count = 0

    def redraw_window() -> None:
        config.WINDOW.blit(config.BACKGROUND, (0, 0))
        lives_label = main_font.render(
            f"Lives: {player.lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        config.WINDOW.blit(lives_label, (10, 10))
        config.WINDOW.blit(level_label, (config.WIDTH -
                           level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(config.WINDOW)

        player.draw(config.WINDOW)

        if has_lost:
            lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
            config.WINDOW.blit(
                lost_label, (config.WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if player.lives <= 0 or player.health <= 0:
            has_lost = True
            lost_count += 1

        if has_lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if not enemies:
            level += 1
            wave_length += 5
            for _ in range(wave_length):
                enemies.append(Enemy(random.randrange(50, config.WIDTH - 100),
                               random.randrange(-1500, -100),
                               random.choice(["red", "blue", "green"])
                                     ))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        if pygame.key.get_pressed()[pygame.K_a]:
            player.move_left()
        if pygame.key.get_pressed()[pygame.K_d]:
            player.move_right()
        if pygame.key.get_pressed()[pygame.K_w]:
            player.move_up()
        if pygame.key.get_pressed()[pygame.K_s]:
            player.move_down()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies:
            enemy.move()
            enemy.move_lasers(player)
            if random.randrange(0, 2 * 60) == 1:
                enemy.shoot()

            if enemy.collision(player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.height > config.HEIGHT:
                player.lives -= 1
                enemies.remove(enemy)

        player.move_lasers(enemies)


def main_menu() -> None:
    title_font = pygame.font.SysFont("monospace", 60)
    run = True
    while run:
        config.WINDOW.blit(config.BACKGROUND, (0, 0))
        title_label = title_font.render(
            "Click to begin...", 1, (255, 255, 255))
        config.WINDOW.blit(title_label, (config.WIDTH / 2 -
                           title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


if __name__ == "__main__":
    main_menu()
