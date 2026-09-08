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
#def keys_pressed(): #הפעולה שבאמצעות המקשים שנלחצו תבחר מיקום

#def legs
#def body