import random
from enum import Enum


class ArrowDirection(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


def getRandomArrowDirection() -> ArrowDirection:
    index = random.randint(0, len(ArrowDirection)-1)# 4 is out of bounds
    return ArrowDirection(index)
