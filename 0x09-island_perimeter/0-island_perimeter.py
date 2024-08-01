#!/usr/bin/python3
"""island perimeter function module"""


def island_perimeter(grid):
    """
    Function name: island_perimeter
    Functionality : returns the perimeter after calculating it
    utilizes an input grid
    0 represents water
    1 represents land
    loops through each cell in the grid
    returns the perimeter of the island described
    removes 2 from the square lands if the neighbor is also land
    checks whether cell is land or water.
    """
    width = len(grid[0])
    height = len(grid)
    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
