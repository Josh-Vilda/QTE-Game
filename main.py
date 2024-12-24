
import pygame
from screens import main_menu

pygame.init()


SCREEN_WIDTH = 1280
SCREEN_LENGTH = 1024 #Resolution of monitor we're using    
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_LENGTH])

main_menu(screen)
