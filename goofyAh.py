import pygame
from sys import exit

def main():

    def playerChoice():
        print("WE CHOOSING BOYS")
        playerPrompt = font.render('Please choose players', True, (0, 0, 0))
        playerPrompt_rect = playerPrompt.get_rect(center=(640,512))
        screen.blit(background, playerPrompt_rect)
        if event.type == pygame.KEYDOWN:
            print("we in boys")
            if event.key == pygame.K_1:
                player1 = playerGroup.add(Player(1))
                print("p1")
            if event.key == pygame.K_2:
                player2 = playerGroup.add(Player(2))
                print("p2")

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
    player1 = playerGroup.add(Player(1))
    player2 = playerGroup.add(Player(2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_active == False:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    print("game no longer false")
                    playerChoice()
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__': main()

class Player(pygame.sprite.Sprite):
    def __init__(self, playerNum):
        super().__init__()
        self.playerNum = playerNum
        if playerNum == 1:
            self.pointer = pygame.image.load('assets/p1PointerUp.png').convert_alpha()
            y_pos = 100
        else:
            self.pointer = pygame.image.load('assets/p2PointerUp.png').convert_alpha()
            self.pointerRect = self.pointer.get.rect()
            y_pos = 500

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pointer = self.pointer
        elif keys[pygame.K_d]:
            self.pointer = pygame.transform.rotate(self.pointer, 90)
        elif keys[pygame.K_s]:
            self.pointer = pygame.transform.rotate(self.pointer, 180)
        elif keys[pygame.K_a]:
            self.pointer = pygame.transform.rotate(self.pointer, 270)


    def update(self):
        self.player_input(self)