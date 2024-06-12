from gameLogic import GameState, scoreTracker
import turtle
from typing import Callable, Optional


PLAYER_1_KEYS = ["Up", "Left", "Down", "Right"]  # DO NOT UNCAPITALIZE
PLAYER_2_KEYS = ["w", "a", "s", "d"]


def nothing():
    pass

def setUpKeyHandlers(
    window: turtle._Screen,
    gameState: GameState,
    scoreTracker: scoreTracker,
    callback: Optional[Callable[[], None]] = None,
):
    for key in PLAYER_1_KEYS:

        def c():
            gameState.player1GotPoint(scoreTracker)
            if callback is not None:
                callback()

        window.onkeypress(c, key)

    for key in PLAYER_2_KEYS:

        def c():
            st2 = scoreTracker.scoreP2
            gameState.player2GotPoint(st2)
            if callback is not None:
                callback()
                
        window.onkeypress(c, key)


'''

def pointsManager(p1pm,p2pm,pp1,pp2):
    pressedKey = keyboard.read_key()

    if pressedKey in ArrowsP2 and str(pen.shape()) == "clear.gif":
        print("FALSE FALSE FALSE FALSE FLASE")
        pp2 -= 1
    if pressedKey in ArrowsP1 and str(pen.shape()) == "clear.gif":
        print("FALSE FALSE FALSE FALSE FLASE")
        pp2 -= 1
    if pressedKey == ArrowsP1[currentState].value:
        pen.shape("clear.gif")
        player1Points += 1
        print("P1 " + str(pp1))
        p1pm.up()
        p1pm.ht()
        p1pm.goto(500,260)
        p1pm.write("P2: {}".format(pp1), align="center", font=("Courier", 24, "normal"))       
        random_delay = random.uniform(0.2, 5)
        time.sleep(random_delay)
        randomizer()
    if pressedKey == ArrowsP2[currentState].value:
        p2pm.up()
        p2pm.ht()
        p2pm.goto(500,260)
        p2pm.write("P2: {}".format(pp2), align="center", font=("Courier", 24, "normal")) 
        pen.shape("clear.gif")
        player2Points += 1
        print("P2 " + str(pp2))
        random_delay = random.uniform(0.2, 5)
        time.sleep(random_delay)
        randomizer()
        
        '''