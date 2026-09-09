import consts
import pygame
import game_field

def create_soldier() :
    image2 = pygame.image.load('soldier.png')
    w = image2.get_width()
    h = image2.get_height()
    image_solider = pygame.transform.scale(image2, (consts.CELL_SIZE * consts.SOLDIER_ROWS , consts.CELL_SIZE * consts.SOLDIER_COLS ))
    return image_solider


def placement_soldier(row = 0,col= 0) :
    r= row * consts.CELL_SIZE
    c=col * consts.CELL_SIZE
    return r,c

soldier_pos = (0, 0)

def get_soldier_pos():
    return soldier_pos

def move_soldier(direction):
    if direction == "UP" and soldier_pos[0] > 0:
        soldier_pos[0] -= 1
    elif direction == "DOWN" and soldier_pos[0] < consts.BOARD_ROWS - consts.SOLDIER_ROWS:
        soldier_pos[0] += 1
    elif direction == "LEFT" and soldier_pos[1] > 0:
        soldier_pos[1] -= 1
    elif direction == "RIGHT" and soldier_pos[1] < consts.BOARD_COLS - consts.SOLDIER_COLS:
        soldier_pos[1] += 1

def check_win(matrix):
    for r in range(consts.SOLDIER_BODY_ROWS):
        for c in range(consts.SOLDIER_COLS):
            check_r = soldier_pos[0] + r
            check_c = soldier_pos[1] + c
            if matrix[check_r][check_c] == consts.FLAG:
                return True
    return False

def check_lose(matrix):
    feet_row = soldier_pos[0] + consts.SOLDIER_BODY_ROWS
    for c in range(consts.SOLDIER_COLS):
        check_c = soldier_pos[1] + c
        if matrix[feet_row][check_c] == consts.MINE:
            return True
    return False
