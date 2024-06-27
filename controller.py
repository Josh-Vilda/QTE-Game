from gameLogic import GameState, scoreWriter
import turtle
from arrows import ArrowsP1, ArrowsP2
from typing import Callable, Optional
import RPi.GPIO as GPIO


PLAYER_1_KEYS = ["Up", "Left", "Down", "Right"]  # DO NOT UNCAPITALIZE
PLAYER_2_KEYS = ["w", "a", "s", "d"]


def nothing():
    pass


class PlayerController:
    def __init__(self,upPin,downPin,leftPin,rightPin,resetPin):
        
        self.upPin = upPin
        self.downPin = downPin
        self.leftPin = leftPin
        self.rightPin = rightPin
        self.resetPin = resetPin
        
        
        self.pinArray =[self.upPin,self.downPin,self.rightPin,self.leftPin]
        
        GPIO.setup(self.upPin,GPIO.IN)
        GPIO.setup(self.downPin,GPIO.IN)
        GPIO.setup(self.rightPin,GPIO.IN)
        GPIO.setup(self.leftPin,GPIO.IN) 
        GPIO.setup(self.resetPin, GPIO.IN)    
        print("Player Controller Activated")
    