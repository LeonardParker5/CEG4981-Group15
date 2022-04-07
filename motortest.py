import time
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())

#run all 4 motors at half throttle for 5 seconds
#set values to 1.0 for full throttle
kit.motor1.throttle = 0.5
kit.motor2.throttle = 0.5
kit.motor3.throttle = 0.5
kit.motor4.throttle = 0.5
time.sleep(5.0)
kit.motor1.throttle = 0
kit.motor2.throttle = 0
kit.motor3.throttle = 0
kit.motor4.throttle = 0
