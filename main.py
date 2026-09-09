import pygame
import consts
import screen
start=(0,0)

def keys_pressed(): #הפעולה שבאמצעות המקשים שנלחצו תבחר מיקום
    running = True
    click=0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_UP:
                       click="u"
                   elif event.key == pygame.K_DOWN:
                       click = "d"
                   elif event.key == pygame.K_LEFT:
                       click = "l"
                   elif event.key == pygame.K_RIGHT:
                       click = "r"
    return click

def winner():
    pass
