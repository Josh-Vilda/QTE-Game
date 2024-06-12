import arrows2
import turtle


class GameState:

    def __init__(self) -> None:
        self.player1Points = 0
        self.player2Points = 0
        self.currentDirection = arrows2.getRandomArrowDirection()

    def player1GotPoint(self,p1pm):
        print("Player 1 got point")
        #writing the score 
        p1pm.ht()
        p1pm.goto(-500,260)
        p1pm.clear()
        p1pm.write("P1: {}".format(self.player1Points ), align="center", font=("Courier", 24, "normal"))

    def player2GotPoint(self,p2pm):
        print("player 2 got point")
        self.player2Points += 1
        p2pm.ht()
        p2pm.goto(500,260)
        p2pm.clear()
        p2pm.write("P2: {}".format(self.player2Points), align="center", font=("Courier", 24, "normal"))
        
class scoreTracker: #Responsible for writing score to screen
    def __init__(self,scoreP1,scoreP2) -> None:
        self.scoreP1 = scoreP1
        self.scoreP2 =scoreP2
        