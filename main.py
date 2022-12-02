import pygame
import sys
import math
import time

SINS = {}
COSS = {}

i = 0
while i < 360:
    SINS[str(float(i))] = math.sin(i)
    i += 0.1
i = 0

i = 0
while i < 360:
    COSS[str(float(i))] = math.cos(i)
    i += 0.1
i = 0

MAP = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
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


def rng(p_x, p_y, p_a):
    i = 0
    while i < 500:
        x = p_x - i * math.sin(p_a)
        y = p_y + i * math.cos(p_a)
        if MAP[int(y) // TILE_SIZE_Y][int(x) // TILE_SIZE_X] == '#':
            break
        i += 1
    return x, y


def draw_map():
    for i in range(len(MAP)):
        for z in range(len(MAP[i])):
            if MAP[i][z] == '#':
                screen.fill((255, 255, 255),
                            pygame.Rect(TILE_SIZE_X * z, TILE_SIZE_Y * i,
                                        TILE_SIZE_X, TILE_SIZE_Y))


a = 0

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    TILE_SIZE_X = width // len(MAP[0])
    TILE_SIZE_Y = height // len(MAP)
    while pygame.event.wait().type != pygame.QUIT:
        screen.fill((0, 0, 0))
        old_time = time.time()
        draw_map()
        for i in range(-45, 45):
            pygame.draw.line(screen, (0, 255, 0), (400, 400), rng(400, 400, 7))
        pygame.display.flip()
