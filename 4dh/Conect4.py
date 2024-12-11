from cProfile import label
from distutils.command.upload import upload
from re import search
from tkinter.ttk import Label

import pygame as pg
import sys
import math
import random

from Tools.scripts.dutree import display

from BOARD import *
pg.init()
pg.display.set_caption('Connect 4')
width = COLUMNS * DISC_SIZE
height = (ROWS +1 ) * DISC_SIZE
size = (COLUMNS * DISC_SIZE, (ROWS +1) * DISC_SIZE)
screen = pg.display.set_mode(size)

my_font = pg.font.sysFont('Calibri', 60)

def main():
    grid = new_grid()

    draw_grid(grid)
    pg.display.update()

    pick_random = random.randint(REAL_PLAYER, AI_PLAYER)

    game_over = False
    while not game_over:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()
            elif event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEMOTION:
                pg.draw.rect(screen, WHITE, (0, 0, width, DISC_SIZE))
                position_x = event.pos[0]
                if pick_random == REAL_PLAYER:
                    pg.draw.circle(screen, RED, (position_x, int(DISC_SIZE / 2)),DISC_RADIUS)
                    pg.display.update()
                    if event.type == pg.MOUSEBUTTONDOWN:
                        pg.draw.rect(screen, WHITE, (0, 0, width, DISC_SIZE))
                        if pick_random == REAL_PLAYER:
                            position_x = event.pos[0]
                            col = int(math.floor(position_x / DISC_SIZE))

                        if is_valid_position(grid, col):
                            row = get_next_open_row(grid, col)
                            grid[row] [col] = REAL_PLAYER_PIECE

                            if search_win_move(grid, REAL_PLAYER_PIECE):
                                Label = my_font.render("PLAYER 1 WINS!", 1, RED)
                                screen.blit(label, (10, 10))
                                game_over = True

                            pick_random += 1
                            pick_random = pick_random % 2

                            draw_grid(grid)

                            if pick_random == AI_PLAYER and not game_over:
                                col, minimax_score = minimax(grid, 5, -math.inf, math.inf, True)

                                if is_valid_position(grid, col):
                                    row = get_next_open_row(grid, col)
                                    grid[row] [col] = AI_PLAYER_PIECE:
                                    label = my_font.render("player 2 wins!", 1, YELLOW)
                                    screen.blit

