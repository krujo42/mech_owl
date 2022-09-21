import pygame
import time
import random
from adafruit_servokit import ServoKit
from time import sleep

#defined controller
kit = ServoKit(channels=16)

###
# servos

# eyes
kit.servo[0].angle = 5 #eyes opend
time.sleep(1.3)
kit.servo[0].angle = 90  #eyes closed
time.sleep(1)
kit.servo[0].angle = None

# beak
kit.servo[1].angle = 90 # beak open
time.sleep(0.3)
kit.servo[1].angle = 135 # beak closed
time.sleep(1)
kit.servo[1].angle = None

#head
kit.servo[2].angle = 90 # head middle
time.sleep(0.5)
kit.servo[2].angle = 150 # head right
time.sleep(1)
kit.servo[2].angle = 30 # head left
time.sleep(1)
kit.servo[2].angle = None

#chickenwings
kit.servo[3].angle = 65 # wings up
time.sleep(0.3)
kit.servo[3].angle = 120 # wings down
time.sleep(1)
kit.servo[3].angle = None


# play sound
pygame.mixer.init()
pygame.mixer.music.load("./sound.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
        continue           
