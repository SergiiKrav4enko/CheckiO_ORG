def count_neighbours(grid=(), x=None, y=None):
    quantity = 0
    grid_len_x=len(grid)
    a_grid_len_y=grid[1]
    grid_len_y=len(a_grid_len_y)
    if y-1>=0:
        if grid[x][y - 1] == 1:
            quantity += 1
    if y+1<grid_len_y:
        if grid[x][y + 1] == 1:
            quantity += 1
    if x-1>=0 and y-1>=0:
        if grid[x - 1][y - 1] == 1:
            quantity += 1
    if x-1>=0:
        if grid[x - 1][y] == 1:
            quantity += 1
    if x-1>=0 and y+1<grid_len_y:
        if grid[x - 1][y + 1] == 1:
            quantity += 1
    if x+1<grid_len_x and y-1>=0:
        if grid[x + 1][y - 1] == 1:
            quantity += 1
    if x+1<grid_len_x:
        if grid[x + 1][y] == 1:
            quantity += 1
    if x+1<grid_len_x and y+1<grid_len_y:
        if grid[x + 1][y + 1] == 1:
            quantity += 1
    return quantity
print(count_neighbours(((1, 0, 0, 1, 0),
                        (0, 1, 0, 0, 0),
                        (0, 0, 1, 0, 1),
                        (1, 0, 0, 0, 0),
                        (0, 0, 1, 0, 0),), 0, 4))