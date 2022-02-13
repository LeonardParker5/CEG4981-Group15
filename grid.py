import numpy as np
import sys, gridvis, random

grid = np.ones((100,100))
grid[1:-1, 1:-1]=0

np.set_printoptions(threshold=sys.maxsize)

im = gridvis.grid_visualize(grid)

#
# Characters used to represent valid/invalid grid coordinates the robot can move to
# as well as character to represent center of robots current position
#
inval_char = 1
val_char = 0 
robot_char = -1

#
# Assumption is that robot will be placed in a random spot on table
# First objective will be to find the tables top edge
#

grid[random.randint(1,98)][random.randint(1,98)] = robot_char

for i in range(0, len(grid)):
    try:
        x_index = grid[i].tolist().index(robot_char)
        y_index = i
    except:
        if (i == len(grid)):
            print("Robot location not found")

print("Robot location initialized at: ")
print(x_index, y_index)
print("Symbol identifying robot at index: ")
print(grid[y_index][x_index])

last_coord = [x_index, y_index]
im = gridvis.init_pos(im, x_index, y_index)

#
# Currently the "robot" finds the edge by simply decrementing its y-coordinate until
# it reaches the 0 index. Once we start working with hardware this should instead make
# calls to the proximity sensor library to determine whether it can keep moving or
# whether it has reached the edge as well as make calls to the motor driver to move
# the robot
#
# This loop decrements from the robot's current y position to move it up until it reaches the 1 y-position.
# It does not decrement to 0 since y=0 contains the out-of-bounds characters
#
for i in range(y_index, 0, -1):

    # Call to proximity sensor to see if table edge is in view. If so break loop, otherwise move

    grid[y_index][x_index] = val_char
    grid[i][x_index] = robot_char

    # Call to motor driver library to move robot to new coordinate position

    y_index = i

#
# Once it has reached an edge the robot will have to turn to begin moving across the table.
# This may involve a movement to back itself up so that it has room to make the turn.
# The robot should then begin cleaning and moving to the tables right edge
#
for i in range(x_index, (len(grid[y_index])-1)):

    # Call to proximity sensor to see if table edge is in view. If so break loop, otherwise move

    grid[y_index][x_index] = val_char
    grid[y_index][i] = robot_char

    # Call to motor driver library to move robot to new coordinate position

    x_index = i

#
# From here the robot will commence a simple movement pattern. It will move down a y-coord index
# and clean the table from right to left. After reaching the edge it will go down a y-coord index
# again and clean left to right. It will repeat this pattern until reaching the bottom edge of the
# table
#

clean_right = False

for i in range(y_index, (len(grid) - 1)):
    # Robot is at the "left" table edge and needs to clean left to right
    if(clean_right):
        for j in range(x_index, (len(grid[y_index])-1)):
            # Call to proximity sensor to see if table edge is in view. If so break loop, otherwise move
            grid[y_index][x_index] = val_char
            grid[y_index][j] = robot_char
            # Call to motor driver library to move robot to new coordinate position
            x_index = j
    # Robot is at the "right" table edge and needs to clean right to left
    else:
        for j in range(x_index, 0, -1):
            # Call to proximity sensor to see if table edge is in view. If so break loop, otherwise move
            grid[y_index][x_index] = val_char
            grid[y_index][j] = robot_char
            # Call to motor driver library to move robot to new coordinate position
            x_index = j
    # Robot reaches an edge and needs to move down another y-coordinate
    # Call to proximity sensor to see if table edge is in view. If so break loop, otherwise move
    clean_right = not clean_right
    grid[y_index][x_index] = val_char
    grid[i][x_index] = robot_char
    # Call to motor driver library to move robot to new coordinate position
    y_index = i
    
print("100 X 100 grid with numbers:")
print(grid)

print("Current robot location:")
print(x_index, y_index)

gridvis.render_grid(im)
