import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, playerNum):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.playerNum = playerNum

    def assignIcon(self):
            self.pointer = pygame.image.load('assets/p1PointerUp.png').convert_alpha() if self.playerNum==1 else pygame.image.load('assets/p2PointerUp.png').convert_alpha()         
  
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