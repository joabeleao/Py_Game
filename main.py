import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')

line_width = 4
markers = []


def draw_grid():
    color_bg = (234, 2, 200)
    color_grid = (50, 50, 50)
    screen.fill(color_bg)
    for x_axis in range(1, 3):
        # horizontal line #TODO add responsiviness
        pygame.draw.line(screen, color_grid, (0, x_axis * 100), (screen_width, x_axis * 100), line_width)
        # vertical line #TODO add responsiviness
        pygame.draw.line(screen, color_grid, (x_axis * 100, 0), (x_axis * 100, screen_width), line_width)


for mark in range(1, 3):
    row = [0] * 3
    markers.append(row)

run = True
while run:

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
