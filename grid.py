import numpy as matrix

grid = matrix.ones((100,100))
grid[1:-1, 1:-1]=0

print("100 X 100 grid with numbers:")
print(grid)