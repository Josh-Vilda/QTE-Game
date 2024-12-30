import pygame


class Round:
    def __init__(self, round_id, player_1, player_2, screen):
        self.round_id = round_id
        self.player_1 = player_1
        self.player_2 = player_2
        self.screen = screen
        self.players = pygame.sprite.Group(player_1, player_2)
        self.player_1_direction = None
        self.player_2_direction = None
        self.is_match = False
        self.is_current_round = False
        self.prev_guess = []


    def update(self):
        self.players.draw(self.screen)
        if self.is_current_round:

            self.player_1.update(self.prev_guess)
            self.player_2.update(self.prev_guess)
        else:
            self.player_1.update_end(self.player_1_direction)
            self.player_2.update_end(self.player_2_direction)

    def check_match(self):
        if not self.is_match:
            if self.player_1.get_input() is not None and self.player_1.get_input() not in self.prev_guess:
                self.player_1_direction = self.player_1.get_input()
            else:
                self.player_1_direction = self.player_1_direction

            if self.player_2.get_input() is not None and self.player_2.get_input() not in self.prev_guess:
                self.player_2_direction = self.player_2.get_input()
            else:
                self.player_2_direction = self.player_2_direction
            if self.player_1_direction  is not None and self.player_2_direction is not None:
                if self.player_1_direction == self.player_2_direction:
                    self.is_match = True
                self.is_current_round = False




    def set_current_round(self, val):
        self.is_current_round = val

    def get_is_match(self):
        return self.is_match

    def get_is_current_round(self):
        return self.is_current_round