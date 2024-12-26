import time

import pygame
from sys import exit
from player import Player
from round import Round
ROUND_COUNT = 3
def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 1024))
    pygame.display.set_caption('Your Mom')
    clock = pygame.time.Clock()
    game_active = True

    mainMenuBG = pygame.image.load("assets/main_menu_bg.png")
    
    screen.fill((255, 255, 255))
    screen.blit(mainMenuBG, (0, 0))

    rounds = []

    for i in range(1,ROUND_COUNT+1):
        player1 = Player(1, 300 * i, pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)
        player2 = Player(2, 300 * i, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT)
        rounds.append(Round(i, player1, player2, screen))
    match_count = 0
    rounds[match_count].set_current_round(True)

    is_running = True

    pygame.event.clear()
    #
    while is_running:
        screen.fill((255, 255, 255))
        screen.blit(mainMenuBG, (0, 0))
        for i in range(match_count + 1):
            rounds[i].update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if not game_active:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_running = False

        if game_active:


            rounds[match_count].check_match()

            if rounds[match_count].get_is_match():
                time.sleep(0.1)
                if match_count >= ROUND_COUNT - 1:
                    game_active = False
                else:
                    match_count += 1
                    rounds[match_count].set_current_round(True)

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    while True:
        main()
