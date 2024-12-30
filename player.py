import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, playerNum, x_pos, up_key, right_key, down_key, left_key):
        super().__init__()
        self.x_pos = x_pos
        self.playerNum = playerNum
        self.up_key = up_key
        self.right_key = right_key
        self.down_key = down_key
        self.left_key = left_key
        self.limits = set()

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
        keys = pygame.key.get_pressed()
        # switch match case
        angle = None
        if keys[self.up_key]:
            angle = 0
        elif keys[self.right_key]:
            angle = -90
        elif keys[self.down_key]:
            angle = 180
        elif keys[self.left_key]:
            angle = 90
        return angle

    def update(self, guesses):
        # Continuous rotation
        self.image = pygame.transform.rotate(self.originalPointer, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.angle += self.rotationSpeed
        self.angle %= 360
        print(self.angle)

        for x in guesses:
            self.limits.add(x + 90)
            self.limits.add(x - 90)

        if self.limits:
            sorted(self.limits)
            if self.angle > min(self.limits) and self.angle < max(self.limits):
                self.angle = max(self.limits)

    def update_end(self, angle):
        self.image = pygame.transform.rotate(self.originalPointer, angle)
        self.rect = self.image.get_rect(center=self.rect.center)