import RPi.GPIO as GPIO
import time
import board
from adafruit_motorkit import MotorKit

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 23
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    return distance

if __name__== '__main__':
    
    kit = MotorKit(i2c=board.I2C())
    kit.motor1.throttle = -0.25
    kit.motor2.throttle = 0.25
    kit.motor3.throttle = 0.25
    kit.motor4.throttle = -0.25
    
    try:
        while True:
            dist = distance()
            #print("Measured Distance = %.1f cm" % dist)
            if (dist < 10.0):
                kit.motor1.throttle = 0
                kit.motor2.throttle = 0
                kit.motor3.throttle = 0
                kit.motor4.throttle = 0
            time.sleep(0.2)

    except KeyboardInterrupt:
        print("Measurement stopped")
        GPIO.cleanup()
