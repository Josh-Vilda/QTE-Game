class Round:
    def __init__(self, players):
        self.players = players
        self.is_match = False

    def check_match(self):
        if all(player.directionSelected for player in self.players):
            rotations = [player.selectedRotation for player in self.players]
            print(f"Rotations: {rotations}")

            if len(set(rotations)) == 1:
                self.is_match = True
                return True

            return False

        return None