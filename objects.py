import pygame
import math
from functions import *


class Map:
    def __init__(self, map_r: list, tile_size_x: int, tile_size_y: int):
        self.map_r = map_r
        self.tile_size_x = tile_size_x
        self.tile_size_y = tile_size_y

    def get_elem_from_map(self, x, y):
        return self.map_r[y][x]

    def get_elem_from_cords(self, x, y):
        size_x, size_y = self.tile_size_y, self.tile_size_x
        return self.map_r[int(y) // size_y][int(x) // size_x]

    def draw(self, screen, p_x, p_y, p_a):
        for i in range(len(self.map_r)):
            for z in range(len(self.map_r[i])):
                if self.map_r[i][z] == '#':
                    screen.fill((255, 255, 255),
                                pygame.Rect(self.tile_size_x * z,
                                            self.tile_size_y * i,
                                            self.tile_size_x,
                                            self.tile_size_y))
        for i in range(p_a, p_a + 80, 1):
            pygame.draw.line(screen, (0, 255, 0), (p_x, p_y),
                             rng(p_x, p_y, i, self),
                             1)
        pygame.draw.circle(screen, (255, 0, 0), (p_x, p_y), 3)


class Player:
    def __init__(self, x, y, a, speed=10, angle_speed=5):
        self.x = x
        self.y = y
        self.angle = a
        self.speed = speed
        self.angle_speed = angle_speed

    def move(self, map_r: Map):
        keys = pygame.key.get_pressed()
        if keys[pygame.key.key_code("w")]:
            new_x, new_y = move_forward(self.x, self.y, self.angle + 45,
                                        self.speed)
            if map_r.get_elem_from_cords(new_x, new_y) != '#':
                self.x, self.y = new_x, new_y
        if keys[pygame.key.key_code("s")]:
            new_x, new_y = move_forward(self.x, self.y,
                                        self.angle + 45, -self.speed)
            if map_r.get_elem_from_cords(new_x, new_y) != '#':
                self.x, self.y = new_x, new_y
        if keys[pygame.key.key_code("d")]:
            self.angle += self.angle_speed
        if keys[pygame.key.key_code("a")]:
            self.angle -= self.angle_speed

    def render_world(self, screen, map_r: Map):
        screen.fill((100, 0, 0))
        screen.fill((0, 100, 0), pygame.Rect((0, 360, 1280, 360)))
        p_x, p_y, angle = self.x, self.y, self.angle
        for i in range(0, 80, 1):
            w_x, w_y = rng(p_x, p_y, self.angle + i, map_r)
            daln = math.sqrt(
                abs(w_x - p_x) ** 2 + abs(w_y - p_y) ** 2) * math.cos(
                (i - 45) / 360 * 2 * math.pi)
            c = pygame.Color(0, 255, 0)
            h = c.hsla
            c.hsla = h[0], h[1] * (1 - max(0, min(1, daln / 500))), h[2]
            x = i * 16
            y = (daln - math.sin(i - self.angle)) / 2
            pygame.draw.rect(screen, c,
                             ((x, y),
                              (16, 720 - (daln - math.sin(i - self.angle)))))
