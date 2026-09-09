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
def check_place(r,c):
  if r >= consts.BOARD_ROWS :
      return False
  if c >= consts.BOARD_COLS :
      return False
  return True


def remove_soldier():
    if consts.HEAD in game_field.game_matriz:
       game_field.game_matriz=[i for i in game_field.game_matriz if i != consts.HEAD or i != consts.LEGS]

tuple=(0,0)
def if_touch(r,c):
    global tuple
    tuple=(r,c)
    for row in range(r,consts.SOLDIER_BODY_ROWS):
        for col in range(c,consts.SOLDIER_COLS):
            if game_field.game_matriz[row][col] ==consts.EMPTY_COL:
                game_field.game_matriz[row][col]=consts.HEAD
            elif game_field.game_matriz[row][col]==consts.FLAG:
                pass
    for row in range(r,consts.SOLDIER_FEET_ROWS):
        for col in range(c,consts.SOLDIER_COLS):
            if game_field.game_matriz[row][col] ==consts.EMPTY_COL:
                game_field.game_matriz[row][col]=consts.LEGS
            elif game_field.game_matriz[row][col]==consts.MINE:
                pass

# def move():
#     global tuple

    #if
        ##if_touch(tuple[0],tuple[1]+1)
