#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time
from threading import Thread
from driveman import brake

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#GPIO Pins zuweisen
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

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

def distanz():
    # setze Trigger auf HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # setze Trigger nach 0.01ms aus LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartZeit = time.time()
    StopZeit = time.time()
 
    # speichere Startzeit
    while GPIO.input(GPIO_ECHO) == 0:
        StartZeit = time.time()
 
    # speichere Ankunftszeit
    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()
 
    # Zeit Differenz zwischen Start und Ankunft
    TimeElapsed = StopZeit - StartZeit
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    distanz = (TimeElapsed * 34300) / 2
 
    return distanz

#detect_collision
def detectcollision(mycar):
    while True:
        try:
            mycar.setdistance(distanz())
            print ("Gemessene Entfernung = %.1f cm" % mycar.distance)
            if mycar.distance < 70 and mycar.speed < 400:
                brake(mycar)
                print ("Brake")
        # Beim Abbruch durch STRG+C resetten
        except KeyboardInterrupt:
            print("Messung vom User gestoppt")
            GPIO.cleanup()
        time.sleep(0.5)            


