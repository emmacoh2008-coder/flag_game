
game_matriz=[]
from random import randrange
import consts


def inserting ():
    for row in range(consts.BOARD_ROWS):
        new_row = []
        for col in range(consts.BOARD_COLS):
            new_row.append(consts.EMPTY_COL)
        game_matriz.append(new_row)


def add():
    for row in range(0,consts.SOLDIER_ROWS):
        for col in range(0,consts.SOLDIER_COLS):
            game_matriz[row][col] =consts.SOLDIER
    for row in range(consts.flag_row,consts.flag_row+consts.FLAG_ROWS):
        for col in range(consts.flag_col,consts.flag_col+consts.FLAG_COLS):
            game_matriz[row][col]=consts.FLAG



    for i in range(consts.MINES_COUNT):
        row = randrange(consts.BOARD_ROWS)
        col = randrange(consts.BOARD_COLS)
        while game_matriz[row][col] == consts.MINE or game_matriz[row][col] == consts.SOLDIER or game_matriz[row][col] == consts.FLAG:
            row = randrange(consts.BOARD_ROWS)
            col = randrange(consts.BOARD_COLS)
        game_matriz[row][col] = consts.MINE
    return game_matriz

def print_game_matrix():
    for row in game_matriz:
        print(row)
inserting()
add()
print_game_matrix()


