import pygame
from sys import exit
from player import Player
from round import Round


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 1024))
    pygame.display.set_caption('Your Mom')
    clock = pygame.time.Clock()
    game_active = True

    mainMenuBG = pygame.image.load("assets/main_menu_bg.png")

    all_player_groups = []

    playerGroup = pygame.sprite.Group()
    player1 = Player(1, 300, pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)
    playerGroup.add(player1)
    player2 = Player(2, 300, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT)
    playerGroup.add(player2)

    all_player_groups.append(playerGroup)

    match_count = 0

    pygame.event.clear()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if not game_active:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    all_player_groups = []
                    match_count = 0
                    all_player_groups.clear()

                    playerGroup = pygame.sprite.Group()
                    player1 = Player(1, 300, pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)
                    playerGroup.add(player1)
                    player2 = Player(2, 300, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT)
                    playerGroup.add(player2)

                    all_player_groups.append(playerGroup)

        if game_active:
            screen.fill((255, 255, 255))
            screen.blit(mainMenuBG, (0, 0))

            for group in all_player_groups:
                for player in group:
                    player.player_input(group)
                    player.update(group)
                group.draw(screen)

            current_round = Round(all_player_groups[-1])
            match_result = current_round.check_match()

            if match_result == True:
                match_count += 1

                if match_count < 3:

                    new_playerGroup = pygame.sprite.Group()

                    player1 = Player(1, 300 + (match_count * 300), pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a)
                    new_playerGroup.add(player1)

                    player2 = Player(2, 300 + (match_count * 300), pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN,
                                     pygame.K_LEFT)

                    new_playerGroup.add(player2)


                    all_player_groups.append(new_playerGroup)

                else:
                    print("We drink!")
                    game_active = False

            elif match_result == False:
                game_active = False

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__': main()
