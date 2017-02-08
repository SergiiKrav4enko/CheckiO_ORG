def kor_len(grid=()):
    grid_len_x=len(grid)
    a_grid_len_y=grid[1]
    grid_len_y=len(a_grid_len_y)
    return grid_len_x, grid_len_y
print(kor_len(((1, 0, 0, 1),
               (0, 1, 0, 0),
               (0, 0, 1, 0),
               (1, 0, 0, 0),
               (0, 0, 1, 0),)))