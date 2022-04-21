import time
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())

#   DEMO FOR REQUIREMENT 1.0
#       Inspection
#   Show that the robot has housing components for all motors and electronics.
#   Objective: The housing components protect the robot’s parts from damage upon 
#   collision at maximum speed (<= 50cm/s).


#Drive full throttle for 5 seconds, making impact with object
kit.motor1.throttle = 1.0
kit.motor2.throttle = 1.0
kit.motor3.throttle = 1.0
kit.motor4.throttle = 1.0
time.sleep(5.0)
#Stop for 1 second
kit.motor1.throttle = 0
kit.motor2.throttle = 0
kit.motor3.throttle = 0
kit.motor4.throttle = 0
time.sleep(1.0)
#Reverse at half throttle for 5 seconds
kit.motor1.throttle = -0.5
kit.motor2.throttle = -0.5
kit.motor3.throttle = -0.5
kit.motor4.throttle = -0.5
time.sleep(5.0)
#Stop and end
kit.motor1.throttle = 0
kit.motor2.throttle = 0
kit.motor3.throttle = 0
kit.motor4.throttle = 0
