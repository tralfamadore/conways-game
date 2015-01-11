import pygame
import sys
from game import get_next_generation, get_random_generation
from pygame.locals import QUIT, K_RETURN, KEYUP


WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

CELL_SIZE_PX = 20

ROWS = 20
COLUMNS = 40

FPS = 20


def draw(surface, generation):
    surface.fill(WHITE)
    for y, inner in enumerate(generation):
        for x, alive in enumerate(inner):
            if alive:
                rect_x = x * CELL_SIZE_PX
                rect_y = y * CELL_SIZE_PX
                rect = (rect_x, rect_y, CELL_SIZE_PX, CELL_SIZE_PX)
                pygame.draw.rect(surface, GRAY, rect)


if __name__ == '__main__':
    pygame.init()
    window_height = ROWS * CELL_SIZE_PX
    window_width = COLUMNS * CELL_SIZE_PX
    MAIN_SURFACE = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Hello Conway's Game!")
    fps_clock = pygame.time.Clock()

    world = get_random_generation(COLUMNS, ROWS)
    draw(MAIN_SURFACE, world)

    while True:
        world = get_next_generation(world)
        for key_up_event in pygame.event.get(KEYUP):
            if key_up_event.key == K_RETURN:
                world = get_random_generation(COLUMNS, ROWS)
        draw(MAIN_SURFACE, world)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fps_clock.tick(FPS)
