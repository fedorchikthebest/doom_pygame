import pygame
import math
import time

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
        y = p_y + i * math.sin(p_a / 360 * 2 * math.pi)
        x = p_x + i * math.cos(p_a / 360 * 2 * math.pi)
        if MAP[int(y) // TILE_SIZE_Y][int(x) // TILE_SIZE_X] == '#':
            break
        i += 1
    return x, y


def draw_map(screen, p_x, p_y, a):
    for i in range(len(MAP)):
        for z in range(len(MAP[i])):
            if MAP[i][z] == '#':
                screen.fill((255, 255, 255),
                            pygame.Rect(TILE_SIZE_X * z, TILE_SIZE_Y * i,
                                        TILE_SIZE_X, TILE_SIZE_Y))
    for i in range(a, a + 90, 1):
        pygame.draw.line(screen, (0, 255, 0), (p_x, p_y), rng(p_x, p_y, i), 1)
    pygame.draw.circle(screen, (255, 0, 0), (p_x, p_y), 3)


a = 0

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    TILE_SIZE_X = 80
    TILE_SIZE_Y = 80
    p_x = 400
    p_y = 400
    fps = 60
    d_x = 0
    d_y = 0
    p_a = 0
    p_a_s = 0
    running = True
    clock = pygame.time.Clock()
    while running:
        old_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    d_y = -5
                if event.key == pygame.K_a:
                    d_x = -5
                if event.key == pygame.K_s:
                    d_y = 5
                if event.key == pygame.K_d:
                    d_x = 5
                if event.key == pygame.K_RIGHT:
                    p_a_s = 2
                if event.key == pygame.K_LEFT:
                    p_a_s = -2
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_a, pygame.K_d]:
                    d_x = 0
                if event.key in [pygame.K_w, pygame.K_s]:
                    d_y = 0
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    p_a_s = 0
            if event.type == pygame.QUIT:
                running = False
        if MAP[(p_y + d_y) // TILE_SIZE_Y][(p_x + d_x) // TILE_SIZE_X] != '#':
            p_x += d_x
            p_y += d_y
        p_a += p_a_s
        screen.fill((100, 0, 0))
        for i in range(0, 80, 1):
            w_x, w_y = rng(p_x, p_y, p_a + i)
            daln = math.sqrt(abs(w_x - p_x) ** 2 + abs(w_y - p_y) ** 2) * math.cos(p_a + i)
            c = pygame.Color(0, 255, 0)
            h = c.hsla
            c.hsla = h[0], h[1] * (1 - max(0, min(1, daln / 500))), h[2]
            # screen.fill(c,
            #             pygame.Rect(i * 16, 720 / daln,
            #                         i * 16 + 16, 720 - 720 / daln))
            x = i * 16
            y = 720 * daln / 500
            pygame.draw.rect(screen, c, ((x, y), (16, 400)))
        map_screen = pygame.surface.Surface((width, height))
        draw_map(map_screen, p_x, p_y, p_a)
        screen.blit(pygame.transform.scale(map_screen, (300, 300)), (0, 0))
        pygame.display.flip()
        clock.tick(60)
