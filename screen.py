import pygame
import time
import consts
import random
import soldier
pygame.init()
surface = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

color = "dark green"

# Changing surface color
surface.fill(color)
pygame.display.flip()

image1 = pygame.image.load('grass.png')
w = image1.get_width()
h = image1.get_height()
image_grass = pygame.transform.scale(image1, (w * 0.1 , h * 0.1))

for i in range (20) :
    surface.blit(image_grass, (random.randint(0, 819), random.randint(0, 460)))
    #surface.blit(image,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()



f = pygame.font.SysFont('arial',20)
text = f.render('Welcome to The Flag game.', True, 'white')
text2 = f.render('Have fun!', True, 'white')

textRect = text.get_rect()
text2Rect = text.get_rect()
textRect.center = ( 150,  20)
text2Rect.center = ( 150,  40)
def create_flag() :
  image3 = pygame.image.load('flag.png')

  image_flag = pygame.transform.scale(image3, (consts.CELL_SIZE * consts.FLAG_ROWS , consts.CELL_SIZE * consts.FLAG_COLS ))
  return image_flag

size= consts.CELL_SIZE
for i in range (1) :
    surface.blit(soldier.create_soldier(), soldier.placement_soldier())
    surface.blit(create_flag() , (consts.flag_col * size , consts.flag_row * size))
    surface.blit(text, textRect)
    surface.blit(text2, text2Rect)
    # (consts.CELL_SIZE * flag_row,                                         consts.CELL_SIZE * flag_co
    #surface.blit(image,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()


time.sleep(5)
pygame.quit()

# def winner():
#     pass
# def loser():
#     pass
# import pygame
# import consts
# import random
# import game_field
# image1 = pygame.image.load('grass.png')
# image3 = pygame.image.load('flag.png')
# image_mine = pygame.image.load('mine.png')
# image_soldier = pygame.image.load('soldier.png')
# pygame.init()
# surface = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
# pygame.display.set_caption("The Flag")
#
# font = pygame.font.SysFont('arial', 20)
# win_text = font.render('You Won!', True, 'white')
# lose_text = font.render('You Lost!', True, 'red')
# welcome_text1 = font.render('Welcome to The Flag game.', True, 'white')
# welcome_text2 = font.render('Have fun!', True, 'white')
#
# # הגרלת מיקומי הדשא מראש
# grass_positions = [(random.randint(0, consts.WINDOW_WIDTH - consts.CELL_SIZE),
#                     random.randint(0, consts.WINDOW_HEIGHT - consts.CELL_SIZE)) for _ in range(20)]
# def draw_game(soldier_pos, matrix, show_grid_and_mines=False):
#     if show_grid_and_mines:
#         # מצב חשיפת מוקשים
#         surface.fill("black")
#
#         # ציור רשת
#         for x in range(0, consts.WINDOW_WIDTH, consts.CELL_SIZE):
#             pygame.draw.line(surface, consts.GRID_COLOR, (x, 0), (x, consts.WINDOW_HEIGHT))
#         for y in range(0, consts.WINDOW_HEIGHT, consts.CELL_SIZE):
#             pygame.draw.line(surface, consts.GRID_COLOR, (0, y), (consts.WINDOW_WIDTH, y))
#
#         # ציור מוקשים
#         for r in range(consts.BOARD_ROWS):
#             for c in range(consts.BOARD_COLS):
#                 if matrix[r][c] == consts.MINE:
#                     # נצייר את המוקש רק על המשבצת הראשונה שלו כדי שלא ישוכפל 3 פעמים
#                     if c == 0 or matrix[r][c - 1] != consts.MINE:
#                         surface.blit(image_mine, (c * consts.CELL_SIZE, r * consts.CELL_SIZE))
#     else:
#         # מצב משחק רגיל
#         surface.fill(consts.GREEN)
#         for pos in grass_positions:
#             surface.blit(image1, pos)
#         surface.blit(welcome_text1, (150, 20))
#         surface.blit(welcome_text2, (150, 40))
#
#     # ציור דגל (מופיע בשני המצבים)
#     surface.blit(image3, (game_field.flag_col * consts.CELL_SIZE, game_field.flag_row * consts.CELL_SIZE))
#
#     # ציור חייל (מופיע בשני המצבים)
#     surface.blit(image_soldier, (soldier_pos[1] * consts.CELL_SIZE, soldier_pos[0] * consts.CELL_SIZE))
#
#     pygame.display.flip()
#
#
# def draw_message(msg):
#     surface.fill("black")
#     if msg == "WIN":
#         text = win_text
#     else:
#         text = lose_text
#     surface.blit(text, (consts.WINDOW_WIDTH // 2 - 50, consts.WINDOW_HEIGHT // 2))
#     pygame.display.flip()
#
# draw_game((0,0),game_field.game_matriz, show_grid_and_mines=False)