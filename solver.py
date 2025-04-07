import pygame
import random
import sys
from collections import deque

# Setting
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 51, 51 
CELL_SIZE = WIDTH // COLS
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
GREEN = (0, 255, 0)

maze = [[1 for _ in range(COLS)] for _ in range(ROWS)]

def generate_maze(x,y):
    maze[y][x] = 0
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(directions)

    for dir_x, dir_y in directions:
        new_x, new_y = x + dir_x, y + dir_y

        if 0 <= new_x < COLS and 0 <= new_y < ROWS and maze[new_y][new_x] == 1:
            maze[x + dir_x // 2][y + dir_y // 2] = 0 
            generate_maze(new_x, new_y)

start = (1, 1)
end = (ROWS -2, COLS -2)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver")
clock = pygame.time.Clock()

def draw_maze():
    for y in range(ROWS):
        for x in range(COLS):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))