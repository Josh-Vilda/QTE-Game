import pygame

class Banner(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('assets/banner.png')
        self.rect = self.image.get_rect(center=(640, 512))

        self.factor = 1
        self.factorSpeed = 5


    def update(self):
        self.image = pygame.transform.scale_by(self.image, self.fator)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.factor += self.factorSpeed