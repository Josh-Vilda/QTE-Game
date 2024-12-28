import time

import pygame
from sys import exit

import score
from player import Player
from round import Round
from score import guessingScore
from banner import Banner

ROUND_COUNT = 3
NUM_PLAYERS = 2

screen = pygame.display.set_mode((1280, 1024))
def main(currentGuesser, player1Score, player2Score):
    pygame.init()
    pygame.display.set_caption('Your Mom')
    clock = pygame.time.Clock()
    game_active = True

    wiiBackground = pygame.image.load("assets/sunshine.jpg")
    mainMenuBG = pygame.image.load("assets/main_menu_bg.png")
    banner = pygame.image.load("assets/banner.png")


    font = pygame.font.Font('assets/wiiMenuFont.ttf', 48)
    guesserFont = pygame.font.Font('assets/wiiMenuFont.ttf', 70)

    screen.blit(wiiBackground, (0, 0))
    wiiBackground.blit(mainMenuBG, (0, 0))

    rounds = []

    for i in range(1, ROUND_COUNT + 1):
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
        screen.blit(wiiBackground, (0, 0))
        wiiBackground.blit(mainMenuBG, (0, 0))

        guesser_text = font.render(f'PLAYER {currentGuesser} IS GUESSING', True, 'white')
        screen.blit(guesser_text, (380, 50))

        score1_text = font.render(f'Player 1: {player1Score.get_score()}', True, 'darkgoldenrod2')
        score2_text = font.render(f'Player 2: {player2Score.get_score()}', True, 'darkgoldenrod2')
        screen.blit(score1_text, (50, 50))
        screen.blit(score2_text, (974, 50))


        for i in range(match_count + 1):
            rounds[i].update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if not game_active:
                pygame.time.wait(500)
                is_running = False

        if game_active:

            rounds[match_count].check_match()

            if rounds[match_count].get_is_match():
                time.sleep(0.15)

                if match_count >= ROUND_COUNT - 1:
                    guessingScore.gameWon = True
                    is_running = False

                else:
                    rounds[match_count + 1].prev_guess.append(rounds[match_count].player_1_direction)
                    match_count += 1
                    rounds[match_count].set_current_round(True)

            elif not rounds[match_count].get_is_match() and not rounds[match_count].get_is_current_round():
                game_active = False

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    currentGuesser = 1
    player1Score = guessingScore()
    player2Score = guessingScore()

    while True:
        currentGuesser = (currentGuesser + 1) % NUM_PLAYERS + 1

        main(currentGuesser, player1Score, player2Score)

        if currentGuesser == 1 and guessingScore.gameWon == True:
            player1Score.set_score()
            guessingScore.gameWon = False

        elif currentGuesser == 2 and guessingScore.gameWon == True:
            player2Score.set_score()
            guessingScore.gameWon = False

        currentGuesser += 1