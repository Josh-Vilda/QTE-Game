import turtle
import random
import time
from enum import Enum
import keyboard
from arrows import ArrowsP1, ArrowsP2
import gameLogic
import controller
from timer import countdown
import threading


window = turtle.Screen()
window.title("Quick Time event by AAAAAAAAAAA")
window.setup(width=1200, height=600)
# variables
player1Points = 0
player2Points = 0
currentState = ""


ArrowState = Enum("ArrowState", ["UP", "DOWN", "LEFT", "RIGHT"])


# add the shapes
# window.addshape("clear.gif")
window.addshape("assets/up.gif")
window.addshape("assets/down.gif")
window.addshape("assets/right.gif")
window.addshape("assets/left.gif")
#pen
pen = turtle.Turtle()
pen.shape("assets/up.gif")
pen.speed(0)
pen.up()
pen.goto(0, 260)
pen.speed(0)
pen.goto(0, 0)
pen.down()

#Timer Pen
timeManager = turtle.Turtle()
timeManager.hideturtle()
timeManager.goto(0,260)

#P1 Pen
player1PointsManager = turtle.Turtle()
player1PointsManager.up()
player1PointsManager.ht()
player1PointsManager.goto(-500,260)
player1PointsManager.write("P1: {}".format(player1Points), align="center", font=("Courier", 24, "normal"))

#P2 Pen
player2PointsManager = turtle.Turtle()
player2PointsManager.up()
player2PointsManager.ht()
player1PointsManager.goto(500,260)
player1PointsManager.write("P2: {}".format(player2Points), align="center", font=("Courier", 24, "normal"))
    
# functions
def up():
    pen.shape("assets/up.gif")
    global currentState
    currentState = "UP"
    print(">UP")


def down():
    pen.shape("assets/down.gif")
    global currentState
    currentState = "DOWN"
    print(">DOWN")


def right():
    pen.shape("assets/right.gif")
    global currentState
    currentState = "RIGHT"
    print(">RIGHT")


def left():
    pen.shape("assets/left.gif")
    global currentState
    currentState = "LEFT"
    print(">LEFT")


def randomizer():
    num = random.randint(0, 3)
    if num == 0:
        up()
    elif num == 1:
        down()
    elif num == 2:
        right()
    elif num == 3:
        left()


def pointsManager():
    global player1Points, player2Points
    pressedKey = keyboard.read_key()

    if pressedKey in ArrowsP2 and str(pen.shape()) == "clear.gif":
        print("FALSE FALSE FALSE FALSE FLASE")
        player2Points -= 1
    if pressedKey in ArrowsP1 and str(pen.shape()) == "clear.gif":
        print("FALSE FALSE FALSE FALSE FLASE")
        player1Points -= 1
    if pressedKey == ArrowsP1[currentState].value:
        pen.shape("clear.gif")
        player1Points += 1
        print("P1 " + str(player1Points))
        random_delay = random.uniform(0.2, 5)
        time.sleep(random_delay)
        randomizer()
    if pressedKey == ArrowsP2[currentState].value:
        pen.shape("clear.gif")
        player2Points += 1
        print("P2 " + str(player2Points))
        random_delay = random.uniform(0.2, 5)
        time.sleep(random_delay)
        randomizer()


# Game setup
game = gameLogic.GameState()
# handle keyboard
controller.setUpKeyHandlers(window, game, randomizer)
window.listen()
#threading the countdown function
try:
    t1 =threading.Thread(target=countdown,args=(90, timeManager))
    t1.start()
except KeyboardInterrupt:
    GPIO.cleanup()
window.mainloop()
