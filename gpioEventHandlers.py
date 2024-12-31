import gpiozero 
import pygame
import sys
import time



def drink(seconds,relay):
     start_time = time.time()
     while(time.time()-start_time<= seconds):
          relay.on()
     relay.off()
     print("Turning off relay")
