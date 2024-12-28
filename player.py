import pygame
from gpiozero import Button

class Player(pygame.sprite.Sprite):

    def __init__(self, playerNum, x_pos, upPin, downPin, rightPin, leftPin):
        super().__init__()
        self.x_pos = x_pos
        self.playerNum = playerNum
        self.upButton = Button(upPin)
        self.downButton = Button(downPin)
        self.rightButton = Button(rightPin)
        self.leftButton = Button(leftPin)       
        '''
        when we impliment GPIO replace key with
        self.up_button = Button(upPin)
        ...
        '''

        if self.playerNum == 1:
            self.originalPointer = pygame.image.load('assets/p1PointerUp.png').convert_alpha()
            y_pos = 300
        else:
            self.originalPointer = pygame.image.load('assets/p2PointerUp.png').convert_alpha()
            y_pos = 600

        self.image = self.originalPointer
        self.rect = self.image.get_rect(center=(self.x_pos, y_pos))

        self.angle = 0
        self.rotationSpeed = 5


    def get_input(self):
        # switch match case
        #replace line 35 and each if statement with if self.upButton.is_pressed 
        angle = None
        if self.upButton.is_pressed:
            angle = 0
        elif self.rightButton.is_pressed:
            angle = 270
        elif self.downButton.is_pressed:
            angle = 180
        elif self.leftButton.is_pressed:
            angle = 90
        return angle

    def update(self):
        # Continuous rotation
        self.image = pygame.transform.rotate(self.originalPointer, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.angle += self.rotationSpeed

        # Reveal
        # elif all(player.directionSelected for player in players):
        #     if self.selectedRotation is not None:

    def update_end(self, angle):
        self.image = pygame.transform.rotate(self.originalPointer, angle)
        self.rect = self.image.get_rect(center=self.rect.center)