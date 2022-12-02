import math
import objects


def rng(p_x, p_y, p_a, map_r):
    i = 0
    while i < 720:
        y = p_y + i * math.sin(p_a / 360 * 2 * math.pi)
        x = p_x + i * math.cos(p_a / 360 * 2 * math.pi)
        if map_r.get_elem_from_cords(x, y) == '#':
            break
        i += 1
    return x, y


def move_forward(x, y, a, step):
    ny = y + math.sin(a / 360 * 2 * math.pi) * step
    nx = x + math.cos(a / 360 * 2 * math.pi) * step
    return nx, ny