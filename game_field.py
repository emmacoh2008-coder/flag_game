import sys
import screen
game_matriz=[]
import random
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
    mines_placed = 0
    while mines_placed < consts.MINES_COUNT:
        row = random.randint(0, consts.BOARD_ROWS - consts.MINE_ROWS)
        col = random.randint(0, consts.BOARD_COLS - consts.MINE_COLS)

        if row < consts.SOLDIER_ROWS and col < consts.SOLDIER_COLS:
            continue

        can_place = True
        for i in range(consts.MINE_ROWS):
            for j in range(consts.MINE_COLS):
                if game_matriz[row + i][col + j] != consts.EMPTY_COL:
                    can_place = False
                    break
            if not can_place:
                break
        if can_place:
            for i in range(consts.MINE_ROWS):
                for j in range(consts.MINE_COLS):
                    game_matriz[row + i][col + j] = consts.MINE
            mines_placed += 1


def get_matrix():
    return game_matriz

def print_game_matrix():
    for row in game_matriz:
        print(row)
inserting()
add()
print_game_matrix()








