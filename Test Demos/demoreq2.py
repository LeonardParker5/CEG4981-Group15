import time
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())

#   DEMO FOR REQUIREMENT 2.0
#       Demonstration
#   Show that the robot can move around via the wheels that are actuated.
#   Objective: The robot travels in the desired direction at the desired speed,
#   without wheel slipping/sliding.

#Loop for 1 minute
counter = 0
while(counter < 60):
    #Drive half throttle for 10 seconds, making impact with object
    kit.motor1.throttle = 0.5
    kit.motor2.throttle = 0.5
    kit.motor3.throttle = 0.5
    kit.motor4.throttle = 0.5
    time.sleep(10.0)
    counter = counter+10
    time.sleep(1.0)
    kit.motor1.throttle = -0.5
    kit.motor2.throttle = -0.5
    kit.motor3.throttle = -0.5
    kit.motor4.throttle = -0.5
    time.sleep(10.0)
    counter = counter+10

