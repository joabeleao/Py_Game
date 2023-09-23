import pygame
from pygame.locals import *

pygame.init()

screen_width: int = 300
screen_height: int = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')

# colors
color_green: tuple = (0, 255, 0)
color_red: tuple = (50, 50, 50)

line_width: int = 4
cells: list = []

player_1: str = 'X'
player_2: str = 'O'
turn: str = 'P1'


def draw_grid():
    line_grid_width: int = 4
    color_bg: tuple = (234, 2, 200)
    color_grid: tuple = (50, 50, 50)
    screen.fill(color_bg)
    for x_axis in range(1, 3):
        line_x_start_pos: tuple = (0, x_axis * 100)
        line_x_end_pos: tuple = (screen_width, x_axis * 100)
        line_y_start_pos: tuple = (x_axis * 100, 0)
        line_y_end_pos: tuple = (x_axis * 100, screen_width)
        # TODO add responsiveness to screen
        # TODO separate draw screen in functions/classes
        pygame.draw.line(screen, color_grid, line_x_start_pos, line_x_end_pos, line_grid_width)
        pygame.draw.line(screen, color_grid, line_y_start_pos, line_y_end_pos, line_grid_width)


def game_logic():
    player: str
    if turn == 'P1':
        player = 'O'
    else:
        player = 'X'
    print(player)

    if ((cells[0][0] == player and cells[1][1] == player and cells[2][2] == player) or
            (cells[0][2] == player and cells[1][1] == player and cells[2][0] == player)):
        print("WIN-DIAGONAL!!!", player)
        pygame.quit()

    for x in range(3):
        win_hor: bool = True
        win_ver: bool = True
        for y in range(3):
            if cells[y][x] != player:
                win_hor = False
            if cells[x][y] != player:
                win_ver = False
        if win_ver is True:
            print("WIN-VERTICAL!!!", player)
            pygame.quit()
        if win_hor is True:
            print("WIN-HORIZONTAL!!!")
            pygame.quit()


def draw_cells():
    x_axis: int = 0
    for array in cells:
        y_axis: int = 0
        for cell in array:
            if cell == 'X':
                start_position_l1: tuple = (x_axis * 100 + 15, y_axis * 100 + 15)
                end_position_l1: tuple = (x_axis * 100 + 85, y_axis * 100 + 85)
                start_position_l2: tuple = (x_axis * 100 + 15, y_axis * 100 + 85)
                end_position_l2: tuple = (x_axis * 100 + 85, y_axis * 100 + 15)
                l1_width: int = 4
                l2_width: int = 4

                pygame.draw.line(screen, color_green,
                                 start_position_l1,
                                 end_position_l1,
                                 l1_width
                                 )
                pygame.draw.line(screen, color_green,
                                 start_position_l2,
                                 end_position_l2,
                                 l2_width
                                 )
            if cell == 'O':
                circle_position: tuple = (x_axis * 100 + 50, y_axis * 100 + 50)
                circle_radius: int = 38
                circle_width: int = 4

                pygame.draw.circle(screen, color_red,
                                   circle_position,
                                   circle_radius,
                                   circle_width)
            y_axis += 1
        x_axis += 1


def create_cells():
    for mark in range(3):
        row = [0] * 3
        cells.append(row)


# game execution
create_cells()
draw_cells()
run = True
while run:

    draw_grid()  # start surface
    draw_cells()  # x and os
    game_logic()

    for event in pygame.event.get():
        # quit if button pressed
        if event.type == pygame.QUIT:
            run = False
        # mouse handlers
        # if clicked:
        if pygame.mouse.get_pressed()[0]:
            mouse_click_coordinates = pygame.mouse.get_pos()
            mouse_click_coordinate_x: int = mouse_click_coordinates[0] // 100
            mouse_click_coordinate_y: int = mouse_click_coordinates[1] // 100
            selected_cell = cells[mouse_click_coordinate_x][mouse_click_coordinate_y]
            if selected_cell == 0 and turn == 'P1':
                cells[mouse_click_coordinate_x][mouse_click_coordinate_y] = player_1
                turn = 'P2'
            elif selected_cell == 0 and turn == 'P2':
                cells[mouse_click_coordinate_x][mouse_click_coordinate_y] = player_2
                turn = 'P1'
            print(cells)

    pygame.display.update()

pygame.quit()
