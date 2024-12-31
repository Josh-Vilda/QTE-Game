import RPi.GPIO as GPIO
import pygame
import sys
import time

def drink(seconds,relay):
     GPIO.setmode(GPIO.BCM)
     GPIO.output(relay,1)
     time.sleep(seconds)
     GPIO.output(relay,0)