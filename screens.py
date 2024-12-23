#different screns are different game loops
import pygame

mainMenuBG = pygame.image.load("assets/main_menu_bg.png")    
def main_menu(screen):
    print("huh")
    
    while True:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                   pygame.quit()

        screen.fill("white")
        screen.blit(mainMenuBG,(0,0))
        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        # Flip the display
        pygame.display.flip()

    