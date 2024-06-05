from gameLogic import GameState
import turtle
from typing import Callable, Optional

PLAYER_1_KEYS = ["Up", "Left", "Down", "Right"]  # DO NOT UNCAPITALIZE
PLAYER_2_KEYS = ["w", "a", "s", "d"]


def nothing():
    pass


def setUpKeyHandlers(
    window: turtle._Screen,
    gameState: GameState,
    callback: Optional[Callable[[], None]] = None,
):
    for key in PLAYER_1_KEYS:

        def c():
            gameState.player1GotPoint()
            if callback is not None:
                callback()

        window.onkeypress(c, key)

    for key in PLAYER_2_KEYS:

        def c():
            gameState.player2GotPoint()
            if callback is not None:
                callback()

        window.onkeypress(c, key)
