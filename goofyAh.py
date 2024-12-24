import pygame
from sys import exit
from player import Player

def main():

    def playerChoice(playerGroup):
        print("WE CHOOSING BOYS")
        playerPrompt = font.render('Please choose players', True, (0, 0, 0))
        playerPrompt_rect = playerPrompt.get_rect(center=(640,512))
        screen.blit(playerPrompt, playerPrompt_rect)
        while True:
            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                print("we in boys")
                if event.mod & pygame.K_1:
                    player1 = Player(1)
                    playerGroup.add(player1)
                    player1.assignIcon()
                    print("p1")
                    return 1
                if event.mod & pygame.K_2:
                    player2 = Player(1)
                    playerGroup.add(player2)
                    player2.assignIcon()
                    print("p2")
                    return 1

    pygame.init()
    screen = pygame.display.set_mode((1280, 1024))
    pygame.display.set_caption('Your Mom')
    clock = pygame.time.Clock()
    font = pygame.font.Font('assets/wiiMenuFont.ttf', 100)
    game_active = False
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    screen.blit(background, (0,0))

    playerGroup = pygame.sprite.Group()
    pygame.event.clear()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_active == False:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    print("game no longer false")
                    playerChoice(playerGroup)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__': main()
