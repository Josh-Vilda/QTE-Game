import turtle
import random
import time
from enum import Enum
import keyboard
from arrows import ArrowsP1, ArrowsP2
import gameState
import controller
import glob

SCREEN_WIDTH_PERCENT = 0.75
SCREEN_HEIGHT_PERCENT = 0.75
SCREEN_TITLE = "QUICK TIME EVENT: THE EVENT"


def screenSetup(fullScreen=False) -> turtle._Screen:

    # setup screen
    screen = turtle.Screen()
    if fullScreen:
        screen.setup(width=1.0, height=1.0)
    else:
        screen.setup(width=SCREEN_WIDTH_PERCENT, height=SCREEN_HEIGHT_PERCENT)
    screen.title(SCREEN_TITLE)

    # adding shapes
    arrows = glob.glob("assets/*.gif")
    for arrow in arrows:
        screen.addshape(arrow)
    return screen


window = screenSetup()

currentState = ""


ArrowState = Enum("ArrowState", ["UP", "DOWN", "LEFT", "RIGHT"])


# add the shapes
# window.addshape("clear.gif")
window.addshape("assets/up.gif")
window.addshape("assets/down.gif")
window.addshape("assets/right.gif")
window.addshape("assets/left.gif")
# Pen
pen = turtle.Turtle()
pen.shape("assets/up.gif")
pen.speed(0)
pen.up()
pen.goto(0, 260)
pen.speed(0)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
pen.goto(0, 0)
pen.down()


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


# def pointsManager():
#     global player1Points, player2Points
#     pressedKey = keyboard.read_key()

#     if pressedKey in ArrowsP2 and str(pen.shape()) == "clear.gif":
#         print("FALSE FALSE FALSE FALSE FLASE")
#         player2Points -= 1
#     if pressedKey in ArrowsP1 and str(pen.shape()) == "clear.gif":
#         print("FALSE FALSE FALSE FALSE FLASE")
#         player1Points -= 1
#     if pressedKey == ArrowsP1[currentState].value:
#         pen.shape("clear.gif")
#         player1Points += 1
#         print("P1 " + str(player1Points))
#         random_delay = random.uniform(0.2, 5)
#         time.sleep(random_delay)
#         randomizer()
#     if pressedKey == ArrowsP2[currentState].value:
#         pen.shape("clear.gif")
#         player2Points += 1
#         print("P2 " + str(player2Points))
#         random_delay = random.uniform(0.2, 5)
#         time.sleep(random_delay)
#         randomizer()


# Game setup
game = gameState.GameState()

# handle keyboard
controller.setUpKeyHandlers(window, game, randomizer)
window.listen()
window.mainloop()
