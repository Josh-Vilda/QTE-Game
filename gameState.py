import arrows2


class GameState:

    def __init__(self) -> None:
        self._player1Points = 0
        self._player2Points = 0
        self._roundNumber = 0
        self._currentDirection = arrows2.getRandomArrowDirection()

    def player1GotPoint(self):
        print("Player 1 got point")
        self._player1Points += 1
        self._roundNumber += 1

    def player2GotPoint(self):
        print("player 2 got point")
        self._player2Points += 1
        self._roundNumber += 1

    def currentRound(self) -> int:
        return self._roundNumber

    def player1Points(self) -> int:
        return self._player1Points

    def player2Points(self) -> int:
        return self._player2Points
