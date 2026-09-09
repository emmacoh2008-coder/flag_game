import sys
import screen
game_matriz=[]
from random import randrange
import consts
import pygame


def inserting ():
    for row in range(consts.BOARD_ROWS):
        new_row = []
        for col in range(consts.BOARD_COLS):
            new_row.append(consts.EMPTY_COL)
        game_matriz.append(new_row)


def add():
    for row in range(consts.flag_row,consts.flag_row+consts.FLAG_ROWS):
        for col in range(consts.flag_col,consts.flag_col+consts.FLAG_COLS):
            game_matriz[row][col]=consts.FLAG

    for i in range(consts.MINES_COUNT):
        row = randrange(consts.SOLDIER_ROWS-1,consts.BOARD_ROWS)
        col = randrange(consts.BOARD_COLS-consts.MINE_COLS)
        while game_matriz[row][col] !=consts.EMPTY_COL:
            row = randrange(consts.SOLDIER_ROWS-1,consts.BOARD_ROWS)
            col = randrange(consts.BOARD_COLS-consts.MINE_COLS)
        for i in range(consts.MINE_ROWS):
            for j in range(consts.MINE_COLS):
                game_matriz[row+i][col+j] = consts.MINE
    return game_matriz

def print_game_matrix():
    for row in game_matriz:
        print(row)
inserting()
add()
print_game_matrix()
print("hi")







