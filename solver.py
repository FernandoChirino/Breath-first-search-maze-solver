import pygame
import random
import sys
from collections import deque

# Setting
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 61, 61 
CELL_SIZE = WIDTH // COLS
FPS = 350  # Controls the speed 

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
            maze[y + dir_y // 2][x + dir_x // 2] = 0  # Remove wall between current cell and new cell
            generate_maze(new_x, new_y)

start = (1, 1)
end = (ROWS -2, COLS -2)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver")
clock = pygame.time.Clock()

def draw_maze():
    screen.fill(BLACK)
    for y in range(ROWS):
        for x in range(COLS):
            if maze[y][x] == 1:  # Wall 
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def BFS_visuals(start, end):
    queque = deque()
    queque.append(start)

    visited = set()
    visited.add(start)

    came_from = {}

    while queque:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current = queque.popleft() # popleft() removes the first element from the deque. current is a tuple (x,y)
        #print(current)
        x,y = current
        #print(x,y)
        
        if current == end:
            break 

        pygame.draw.rect(screen, PURPLE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()  # Updates the screen 
        clock.tick(FPS)

        for dir_x, dir_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]: # Explore neighbors (up, right, down, left)
            new_x, new_y = x + dir_x, y + dir_y
            neighbor = (new_x, new_y)

            if 0 <= new_x < ROWS and 0 <= new_y < COLS and maze[new_y][new_x] == 0 and (new_x, new_y) not in visited:
                visited.add(neighbor)
                queque.append(neighbor)
                came_from[neighbor] = current

    current = end
    while current != start: 

        x,y = current
        pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        clock.tick(FPS)

        current = came_from[current]  # move to the previous cell in the path
        if current == start:
            break

def main():
    generate_maze(start[0], start[1])
    draw_maze()
    pygame.draw.rect(screen, GREEN, (start[0] * CELL_SIZE, start[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, GREEN, (end[0] * CELL_SIZE, end[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()
    clock.tick(FPS)

    BFS_visuals(start, end)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(FPS)   

    pygame.display.flip()
    pygame.quit()
    sys.exit() 

main()
