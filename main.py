import pygame
import sys
import random


pygame.init()

CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20

WIDTH = CELL_SIZE * GRID_WIDTH
HEIGHT = CELL_SIZE * GRID_HEIGHT

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SANDSIMv1")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

grid = [[0 for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]


def drawGrid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = YELLOW if grid[y][x] == 1 else BLACK
            pygame.draw.rect(screen, color, rect)


def updateGrid():
    for y in range(GRID_HEIGHT - 2, -1, -1):
        for x in range(GRID_WIDTH):
            if grid[y][x] == 1:
                if grid[y + 1][x] == 0:
                    grid[y][x] = 0
                    grid[y + 1][x] = 1
                else:
                    right_free = (x + 1 < GRID_WIDTH) and (grid[y + 1][x + 1] == 0)
                    left_free = (x - 1 >= 0) and (grid[y + 1][x - 1] == 0)

                    if right_free and left_free:
                        if random.choice([True, False]):
                            grid[y][x] = 0
                            grid[y + 1][x + 1] = 1
                        else:
                            grid[y][x] = 0
                            grid[y + 1][x - 1] = 1
                    elif right_free:
                        grid[y][x] = 0
                        grid[y + 1][x + 1] = 1
                    elif left_free:
                        grid[y][x] = 0
                        grid[y + 1][x - 1] = 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        mx, my = pygame.mouse.get_pos()
        grid_x = mx // CELL_SIZE
        grid_y = my // CELL_SIZE
        if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
            grid[grid_y][grid_x] = 1

    updateGrid()
    screen.fill(BLACK)
    drawGrid()
    pygame.display.flip()
    clock.tick(30)
