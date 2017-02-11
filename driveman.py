# This manages the drive functions of the car
# The list of drive functions is:
# - accellerate forward
# - accellerate backward
# - steer left
# - steer right
# - steer straight
# - brake

# Import the PCA9685 module.
import Adafruit_PCA9685
import time
# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()



# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Helper function to make setting a speed pulse width simpler.
def set_speed_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 1, pulse)

def speedset(mycar, speed):
    pwm.set_pwm(1, 0, speed)
    mycar.setspeed=speed
    
def brake(mycar):
    pwm.set_pwm(1, 0, max_backw)
    pwm.set_pwm(1, 0, xneutral)
    speedset(mycar, xneutral)

def steer(mycar, direction):
    pwm.set_pwm(0, 0, direction)
    mycar.setsteer(direction)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

#init speed controller
time.sleep(1)
pwm.set_pwm(1, 0, 375)
print('Speedcontrol init')
