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
image3 = pygame.image.load('flag.png')
for i in range (1) :
    surface.blit(soldier.create_soldier(), soldier.placement_soldier())
    surface.blit(text, textRect)
    surface.blit(text2, text2Rect)

    #surface.blit(image,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()


time.sleep(5)
pygame.quit()

def winner():
    pass
def loser():
    pass