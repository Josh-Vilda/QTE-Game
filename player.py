import pygame

class Player(pygame.sprite.Sprite):
    all_players = []
    bothPlayersHaveSelected = False

    def __init__(self, playerNum):
        super().__init__()
        self.playerNum = playerNum
        self.directionSelected = False
        self.selectedRotation = None
        self.hasRotated = False

        Player.all_players.append(self)

        if self.playerNum == 1:
            self.originalPointer = pygame.image.load('assets/p1PointerUp.png').convert_alpha()
            y_pos = 300
        else:
            self.originalPointer = pygame.image.load('assets/p2PointerUp.png').convert_alpha()
            y_pos = 600

        self.image = self.originalPointer
        self.rect = self.image.get_rect(center=(300, y_pos))

        self.angle = 0
        self.rotationSpeed = 5

    def player_input(self):
        if not Player.bothPlayersHaveSelected and not self.hasRotated:
            keys = pygame.key.get_pressed()

            # Player 1 controls
            if self.playerNum == 1:
                if keys[pygame.K_w]:
                    self.selectedRotation = 0
                    self.directionSelected = True
                elif keys[pygame.K_d]:
                    self.selectedRotation = 270
                    self.directionSelected = True
                elif keys[pygame.K_s]:
                    self.selectedRotation = 180
                    self.directionSelected = True
                elif keys[pygame.K_a]:
                    self.selectedRotation = 90
                    self.directionSelected = True

            # Player 2 controls
            if self.playerNum == 2:
                if keys[pygame.K_UP]:
                    self.selectedRotation = 0
                    self.directionSelected = True
                elif keys[pygame.K_RIGHT]:
                    self.selectedRotation = 270
                    self.directionSelected = True
                elif keys[pygame.K_DOWN]:
                    self.selectedRotation = 180
                    self.directionSelected = True
                elif keys[pygame.K_LEFT]:
                    self.selectedRotation = 90
                    self.directionSelected = True

            # Check if both players have selected
            Player.bothPlayersHaveSelected = all(
                player.directionSelected for player in Player.all_players
            )

    def update(self):
        # Continuous rotation
        if not Player.bothPlayersHaveSelected:
            rotatedPointer = pygame.transform.rotate(self.originalPointer, self.angle)
            self.image = rotatedPointer
            self.rect = self.image.get_rect(center=self.rect.center)
            self.angle += self.rotationSpeed

        # Reveal
        elif not self.hasRotated:
            if self.selectedRotation is not None:
                rotatedPointer = pygame.transform.rotate(self.originalPointer, self.selectedRotation)
                self.image = rotatedPointer
                self.rect = self.image.get_rect(center=self.rect.center)
                self.hasRotated = True

        self.player_input()
