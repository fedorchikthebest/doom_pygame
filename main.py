import pygame
import math
import time
from objects import *

map_l = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
         ['#', '1', '2', '3', '1', '1', '2', '3', '#', '1', '2', '#'],
         ['#', '1', '2', '3', '1', '1', '2', '3', '#', '1', '2', '#'],
         ['#', '1', '2', '3', '1', '1', '2', '3', '#', '1', '2', '#'],
         ['#', '1', '2', '3', '1', '1', '2', '3', '#', '1', '2', '#'],
         ['#', '1', '2', '3', '1', '1', '2', '3', '1', '1', '2', '#'],
         ['#', '1', '2', '3', '1', '1', '2', '3', '#', '1', '2', '#'],
         ['#', '1', '2', '3', '1', '1', '2', '3', '#', '1', '2', '#'],
         ['#', '1', '2', '3', '1', '1', '2', '3', '#', '1', '2', '#'],
         ['#', '1', '2', '3', '1', '1', '2', '3', '#', '1', '2', '#'],
         ['#', '1', '2', '3', '1', '1', '2', '3', '#', '1', '2', '#'],
         ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

a = 0

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    map_r = Map(map_l, 80, 80)
    player = Player(400, 400, 0)
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.move(map_r)
        player.render_world(screen, map_r)
        map_screen = pygame.surface.Surface((width, height))
        map_r.draw(map_screen, player.x, player.y, player.angle)
        screen.blit(pygame.transform.scale(map_screen, (300, 300)), (0, 0))
        pygame.display.flip()
        clock.tick(60)