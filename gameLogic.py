import arrows2


class GameState:

    def __init__(self) -> None:
        self.player1Points = 0
        self.player2Points = 0
        self.roundNumber = 0
        self.currentDirection = arrows2.getRandomArrowDirection()

    def player1GotPoint(self):
        print("Player 1 got point")
        self.player1Points += 1
        self.roundNumber += 1

    def player2GotPoint(self):
        print("player 2 got point")
        self.player2Points += 1
        self.roundNumber += 1
