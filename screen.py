import pygame
import consts
import random

import game_field
import soldier
import sys

surface = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def create_flag() :
  image3 = pygame.image.load('flag.png')

  image_flag = pygame.transform.scale(image3, (consts.CELL_SIZE * consts.FLAG_ROWS , consts.CELL_SIZE * consts.FLAG_COLS ))
  return image_flag

size= consts.CELL_SIZE
sol = soldier.create_soldier()
    # (consts.CELL_SIZE * flag_row,
def create_screen() :
    pygame.init()
    color = "dark green"
    surface.fill(color)
    pygame.display.flip()
    image1 = pygame.image.load('grass.png')
    w = image1.get_width()
    h = image1.get_height()
    image_grass = pygame.transform.scale(image1, (w * 0.1, h * 0.1))
    for i in range(20):
        surface.blit(image_grass, (random.randint(0, consts.WINDOW_WIDTH - consts.CELL_SIZE), random.randint(0, consts.WINDOW_HEIGHT - consts.CELL_SIZE)))
    f = pygame.font.SysFont('arial', 20)
    text = f.render('Welcome to The Flag game.', True, 'white')
    text2 = f.render('Have fun!', True, 'white')
    text_rect = text.get_rect()
    text2_rect = text.get_rect()
    text_rect.center = (150, 20)
    text2_rect.center = (150, 40)
    surface.blit(sol, soldier.soldier_pos)
    surface.blit(create_flag() , (consts.flag_col * size , consts.flag_row * size))
    surface.blit(text, text_rect)
    surface.blit(text2, text2_rect)
    pygame.display.update()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0, 255)


def create_screen_grid():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid(game_field.get_matrix())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def mine():
    image4 = pygame.image.load('mine.png')
    image_mine = pygame.transform.scale(image4,(consts.CELL_SIZE * consts.MINE_COLS, consts.CELL_SIZE * consts.MINE_ROWS))
    return image_mine


def drawGrid(matrix):
    blockSize =  consts.CELL_SIZE #Set the size of the grid block
    for x in range(0, consts.WINDOW_WIDTH, blockSize):
        for y in range(0, consts.WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, GREEN, rect, 1)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == consts.MINE :
                    if j==0 or matrix[i][j-1] == consts.EMPTY_COL :
                        surface.blit(mine(), (j * consts.CELL_SIZE, i * consts.CELL_SIZE))



create_screen_grid()