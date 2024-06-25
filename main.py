import turtle
import random
import time
from enum import Enum
import keyboard
from arrows import ArrowsP1, ArrowsP2
from gameLogic import GameState, scoreWriter
import controller
from timer import countdown
import threading
import os
import sys
#import RPi.GPIO as GPIO 

window = turtle.Screen()
window.title("Quick Time event by AAAAAAAAAAA")
window.setup(width=1200, height=600)

#controller set up
p1Controller = controller.Player1Controller(1,3,5,7) #RasPi pins
p2Controller = controller.Player2Controller(15,16,17,18) #RasPi pins


#ArrowState = Enum("ArrowState", ["UP", "DOWN", "LEFT", "RIGHT"]) currently not used

# add the shapes
window.addshape("assets/clear.gif")
window.addshape("assets/up.gif")
window.addshape("assets/down.gif")
window.addshape("assets/right.gif")
window.addshape("assets/left.gif")

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.goto(0, 0)
pen.up()


# Game setup
game = GameState(pen)
game.randomizer()


#Timer Pen
timeManager = turtle.Turtle()
timeManager.hideturtle()
timeManager.up()
timeManager.goto(0,260)

#Score Tracker
player1PointsManager = turtle.Turtle()#P1 pen
player2PointsManager = turtle.Turtle()#P2 pen

scoreWriter = scoreWriter(player1PointsManager,player2PointsManager)
scoreWriter.scoreP1.up()
scoreWriter.scoreP1.up()
scoreWriter.scoreP1.ht()
scoreWriter.scoreP1.goto(500,260)
scoreWriter.scoreP1.write("P1: {}".format(game.player1Points), align="center", font=("Courier", 24, "normal"))

scoreWriter.scoreP2.up()
scoreWriter.scoreP2.ht()
scoreWriter.scoreP2.goto(-500,260)
scoreWriter.scoreP2.write("P2: {}".format(game.player2Points), align="center", font=("Courier", 24, "normal"))


# handle keyboard
#controller.setUpKeyHandlers(window, game, scoreWriter,ArrowsP1,ArrowsP2,game.randomizer)
def restartGame():
    os.execl(sys.executable, sys.executable, *sys.argv)
window.listen()
window.onkeypress(restartGame,"r")


def checkPoints(p1pm,p2pm,pen,game):
        while(True):
            game.pointsManager(p1pm,p2pm,pen)
#threading the countdown function
try:
    t1 =threading.Thread(target=countdown,args=(90, timeManager,game))
    t2 =threading.Thread(target=checkPoints,args=(player1PointsManager,player2PointsManager,pen,game))
    t1.start()
    t2.start()
except KeyboardInterrupt:
    GPIO.cleanup()    
window.mainloop()
    
