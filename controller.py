from gameLogic import GameState, scoreWriter
import turtle
from arrows import ArrowsP1, ArrowsP2

from typing import Callable, Optional
#import RPi.GPIO as GPIO


PLAYER_1_KEYS = ["Up", "Left", "Down", "Right"]  # DO NOT UNCAPITALIZE
PLAYER_2_KEYS = ["w", "a", "s", "d"]


def nothing():
    pass

'''
def setUpKeyHandlers(
    window: turtle._Screen,
    gameState: GameState,
    scoreWriter: scoreWriter,
    arrowsP1: ArrowsP1,
    arrowsP2: ArrowsP2,
    callback: Optional[Callable[[], None]] = None,
    
):
    for key in PLAYER_1_KEYS:

        def c():
            print(">>"+str(ArrowsP1[gameState.currentDirection].value))
            print(str(key))
            if(key==ArrowsP1[gameState.currentDirection].value.lower()):
                st1 = scoreWriter.scoreP1
                gameState.player1GotPoint(st1)
                if callback is not None:
                    callback()#wtf does this do 

        window.onkeypress(c, key)

    for key in PLAYER_2_KEYS:
        def c():
            print(">>"+str(ArrowsP2[gameState.currentDirection].value))
            print(str(key))
            st2 = scoreWriter.scoreP2
            gameState.player2GotPoint(st2)
            if callback is not None:
                callback()
                
        window.onkeypress(c, key)'''

class Player1Controller:
    def __init__(self,up,down,left,right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        print("Player 1 Controller Activated")              
            
class Player2Controller:
    def __init__(self,up,down,left,right):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        print("Player 2 Controller Activated")        
