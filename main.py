import pygame
import time
import game_field
import soldier
import screen




def main():
    game_field.add()
    matrix = game_field.get_matrix()
    running = True
    show_grid_time = 0
    screen.create_screen()
    while running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        soldier.move_soldier("UP")
                    elif event.key == pygame.K_DOWN:
                        soldier.move_soldier("DOWN")
                    elif event.key == pygame.K_LEFT:
                        soldier.move_soldier("LEFT")
                    elif event.key == pygame.K_RIGHT:
                        soldier.move_soldier("RIGHT")
                    elif event.key == pygame.K_RETURN:
                        screen.create_screen_grid()



        if soldier.check_win(matrix):
            screen.create_screen()
            screen.draw_message("WIN")
            time.sleep(3)
            running = False
        elif soldier.check_lose(matrix):
            screen.create_screen()
            screen.draw_message("LOSE")
            time.sleep(3)
            running = False
        else:
            screen.create_screen()

        pygame.quit()
main()
