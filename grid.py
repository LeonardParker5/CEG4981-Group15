import gridvis

grid = []
for i in range (100):
    grid.append([])
    for j in range(1, 101):
        grid[i].append(j)
        
print("100 X 100 grid with numbers:")
print(grid)

gridvis.grid_visualize(grid)