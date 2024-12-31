import time

import pygame
from sys import exit


import score
from player import Player
from round import Round
from score import guessingScore
from banner import Banner
from gpiozero import Button
from gpioEventHandlers import drink
import random
import threading


ROUND_COUNT = 3
NUM_PLAYERS = 2
RELAY_P1_PIN = 2
RELAY_P2_PIN = 3
drinkingP1Thread = threading.Thread(target=drink,args=(RELAY_P1_PIN,))
drinkingP2Thread = threading.Thread(target=drink,args=(RELAY_P2_PIN,))
screen = pygame.display.set_mode((1280, 1024))
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

p1UpButton = Button(5)
p1DownButton = Button(6)
p1RightButton = Button(13)
p1LeftButton = Button(19)

p2UpButton = Button(12)
p2DownButton = Button(16)
p2RightButton = Button(20)
p2LeftButton = Button(21)    

def main(currentGuesser, player1Score, player2Score):
    pygame.init()
    pygame.display.set_caption('Your Mom')
    clock = pygame.time.Clock()
    game_active = True

    
    wiiBackground1 = pygame.image.load("assets/Matt/matt1.jpg")

    wiiBackground2 = pygame.image.load("assets/Matt/matt2.jpg")
    wiiBackground2 = pygame.transform.scale_by(wiiBackground2, 6)

    wiiBackground3 = pygame.image.load("assets/Matt/matt3.jpg")
    wiiBackground3 = pygame.transform.scale_by(wiiBackground3, 4.4)

    wiiBackground4 = pygame.image.load("assets/Matt/matt4.jpg")
    wiiBackground4 = pygame.transform.scale_by(wiiBackground4, 3.45)

    wiiBackground5 = pygame.image.load("assets/Matt/matt5.jpg")
    wiiBackground5 = pygame.transform.scale_by(wiiBackground5, 5.7)

    wiiBackground6 = pygame.image.load("assets/Matt/matt6.jpg")
    wiiBackground6 = pygame.transform.scale_by(wiiBackground6, 3.1)

    wiiBackground7 = pygame.image.load("assets/Matt/matt7.jpg")
    wiiBackground7 = pygame.transform.scale_by(wiiBackground7, 5.35)

    backgroundArray = [wiiBackground1, wiiBackground2, wiiBackground3, wiiBackground4, wiiBackground5, wiiBackground6, wiiBackground7]


    mainMenuBG = pygame.image.load("assets/main_menu_bg.png")

    guesser_sign = pygame.image.load("assets/guessing.png").convert_alpha()
    guesser_sign = pygame.transform.scale_by(guesser_sign, 2.5)

    player_1_drinks = pygame.image.load("assets/Player_1_Drinks.png").convert_alpha()
    player_2_drinks = pygame.image.load("assets/Player_2_Drinks.png").convert_alpha()

    crown = pygame.image.load("assets/crown.png").convert_alpha()
    crown = pygame.transform.scale_by(crown, 0.5)

    player_1_drinks = pygame.transform.smoothscale_by(player_1_drinks, 1.35)
    player_2_drinks = pygame.transform.smoothscale_by(player_2_drinks, 1.35)

    font = pygame.font.Font('assets/wiiMenuFont.ttf', 40)
    guesserFont = pygame.font.Font('assets/wiiMenuFontBold.ttf', 48)
    guesserFont.set_italic(True)

    marioFont = pygame.font.Font('assets/mario_font.ttf', 200)

    backgroundIndex = random.randint(1,7)

    backgroundPicker(backgroundIndex, backgroundArray)
    screen.blit(mainMenuBG, (0, 0))
    screen.blit(guesser_sign , (390, 35))

    rounds = []
    
    for i in range(1, ROUND_COUNT + 1):
        player1 = Player(1, 300 * i, p1UpButton, p1DownButton, p1RightButton, p1LeftButton) # UP, DOWN, RIGHT,LEFT
        player2 = Player(2, 300 * i, p2UpButton, p2DownButton, p2RightButton, p2LeftButton)
        rounds.append(Round(i, player1, player2, screen))

    match_count = 0
    rounds[match_count].set_current_round(True)

    is_running = True

    pygame.event.clear()
    #
    while is_running:
        screen.fill((255, 255, 255))

        backgroundPicker(backgroundIndex, backgroundArray)
        screen.blit(mainMenuBG, (0, 0))
        screen.blit(guesser_sign, (390, 35))

        guesser_text_1 = guesserFont.render(f'PLAYER {currentGuesser}', True, (26,183,234))
        guesser_text_2 = guesserFont.render(f'IS GUESSING', True, (26, 183, 234))
        screen.blit(guesser_text_1, (580, 70))
        screen.blit(guesser_text_2, (580, 115))

        score1_text = font.render(f'Player 1: {player1Score.get_score()}', True, 'white')
        score2_text = font.render(f'Player 2: {player2Score.get_score()}', True, 'white')
        screen.blit(score1_text, (70, 40))
        screen.blit(score2_text, (1014, 40))

        if player1Score.get_score() > player2Score.get_score():
            screen.blit(crown, (135, 0))
        elif player1Score.get_score() < player2Score.get_score():
            screen.blit(crown, (1080, 0))

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

                    HIDE_WINNING_MESSAGE = pygame.USEREVENT + 1

                    pygame.time.set_timer(HIDE_WINNING_MESSAGE, 750, 1)

                    show_winning_message = True

                    while show_winning_message:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                exit()

                            if event.type == HIDE_WINNING_MESSAGE:
                                show_winning_message = False
                        if currentGuesser == 1:
                            pygame.draw.rect(screen, (26,183,234), pygame.Rect(0, 195, 1280, 500))
                            win_text_1 = marioFont.render(f'PLAYER 2', True, 'white')
                            win_text_2 = marioFont.render(f'DRINKS!', True, 'white')
                            drinkingP1Thread.start()
                            screen.blit(win_text_1, (130, 255))
                            screen.blit(win_text_2, (230, 455))
                        else:
                            pygame.draw.rect(screen, (26,183,234), pygame.Rect(0, 195, 1280, 500))
                            win_text_1 = marioFont.render(f'PLAYER 1', True, 'white')
                            win_text_2 = marioFont.render(f'DRINKS!', True, 'white')
                            drinkingP2Thread.start()
                            screen.blit(win_text_1, (130, 255))
                            screen.blit(win_text_2, (230, 455))

                        pygame.display.update()
                        clock.tick(60)

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
        
def backgroundPicker(backgroundIndex, array):
    if backgroundIndex == 1:
        screen.blit(array[0], (0, 0))

    elif backgroundIndex == 2:
        screen.blit(array[1], (0, -200))

    elif backgroundIndex == 3:
        screen.blit(array[2], (0, -60))

    elif backgroundIndex == 4:
        screen.blit(array[3], (0, 0))

    elif backgroundIndex == 5:
        screen.blit(array[4], (0, -50))

    elif backgroundIndex == 6:
        screen.blit(array[5], (0, 0))

    elif backgroundIndex == 7:
        screen.blit(array[6], (0, -350))


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
