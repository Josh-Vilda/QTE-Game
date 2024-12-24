import pygame
from sys import exit
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 1024))
    pygame.display.set_caption('Your Mom')
    clock = pygame.time.Clock()
    font = pygame.font.Font('assets/wiiMenuFont.ttf', 100)
    game_active = True
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    screen.blit(background, (0,0))

    mainMenuBG = pygame.image.load("assets/main_menu_bg.png")
    screen.blit(mainMenuBG, (0, 0))

    playerGroup = pygame.sprite.Group()

    player1 = Player(1)
    playerGroup.add(player1)
    player2 = Player(2)
    playerGroup.add(player2)

    pygame.event.clear()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if game_active:
            playerGroup.update()
            playerGroup.draw(screen)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__': main()
