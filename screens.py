#different screns are different game loops
import pygame
from player import Player

mainMenuBG = pygame.image.load("assets/main_menu_bg.png")

def main_menu(screen):
    print("huh")
    playerGroup = pygame.sprite.Group()
    font = pygame.font.Font('assets/wiiMenuFont.ttf', 100)    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    print("p1")
                    player1 = Player(1)
                    playerGroup.add(player1)
                if event.key == pygame.K_2:
                    print("p2")
                    player2 = Player(2)
                    playerGroup.add(player2)
                                        
        # Fill the background with white
        screen.fill((255, 255, 255))
        screen.blit(mainMenuBG,(0,0))
        playerPrompt = font.render('Please choose players', True, (0, 0, 0))
        playerPrompt_rect = playerPrompt.get_rect(center=(640,512))
        screen.blit(playerPrompt, playerPrompt_rect)

        # Flip the display
        pygame.display.flip()

    