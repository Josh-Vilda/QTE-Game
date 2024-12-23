import RPi.GPIO as GPIO
import pygame
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(PIN, GPIO.RISING)  #This means you are catching a rising detection - so your button press
for event in pygame.event.get():
     if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE) or GPIO.event_detected(PIN):
          pygame.quit()
          sys.exit()