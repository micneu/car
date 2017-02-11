# This is the main manager module for the car
# Simple car console
# Author: Michael Neu
# License: Public Domain
from __future__ import division
import time
from threading import Thread
from random import randint
from driveman import brake
from driveman import speedset
from driveman import steer
from sensorman import detectcollision

global max_forw
global slow_forw
global slow_backw
global max_backw
global xneutral
global steer_left
global steer_right
global steer_straight
max_forw=200
slow_forw=370
slow_backw=435
max_backw=580
xneutral=400
steer_left=500
steer_right=250
steer_straight=400


class car:
    def __init__(self, steer, speed):
        self.steer = steer
        self.speed = speed
        self.distance = 0

    def setspeed(self, speed):
        self.speed=speed

    def setsteer(self, steer):
        self.steer=steer

    def setdistance(self, dist):
        self.distance=dist

mycar=car(steer_straight, xneutral)

      
# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)


drivelist=[max_forw, slow_forw, slow_backw, max_backw, xneutral]
steerlist=[steer_left, steer_right, steer_straight]
 
def rand_steer():
    direction=steerlist[randint(1, 3)-1]
    print('direction change', direction)
    return direction


if __name__ == "__main__":
    print('Start thread...')
    thread = Thread(target=detectcollision, args=(mycar,))
    print('Start thread...')
    thread.start()
    print('go on...')

    print('Drive forward until barricade is detected')
    speedset(mycar, slow_forw)
    
    while True:
        print('steer randomly')
        steer(mycar, rand_steer())
        print(mycar.speed, mycar.steer, mycar.distance)
        time.sleep(1)
        if mycar.distance < 70:
            print('Drive back')
            steer(mycar, rand_steer())
            time.sleep(1)
            speedset(mycar, slow_backw)
            time.sleep(0.2)
            speedset(mycar, slow_backw)
            time.sleep(0.2)
            speedset(mycar, xneutral)
        else:
            print('Drive forward until barricade is detected')
            speedset(mycar, slow_forw)
            time.sleep(0.6)
            speedset(mycar, xneutral)
            time.sleep(0.1)
