from gameLogic import GameState

PLAYER_1_KEYS = ["up", "left", "down", "right"]
PLAYER_2_KEYS = ["w", "a", "s", "d"]


def handleUserInput(key, gameState: GameState):
    if key in PLAYER_1_KEYS:
        gameState.player1GotPoint()
    elif key in PLAYER_2_KEYS:
        gameState.player2GotPoint()
