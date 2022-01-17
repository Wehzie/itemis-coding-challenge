import sys
import math

GRID_MIN = 0
GRID_MAX = 16

def get_dev_input2() -> list:
    """Build a maze for development purposes."""
    form1 = (
"""................
................
+------------+..
|            |..
+-+   o      |..
oo|      o   |..
+-+  +-------+..
|    |..........
+----+..........
............o...
.....o..........
................
.........o......
................
................
................""")

    form2 = form1.splitlines()
    grid = []
    for line in form2:
        grid.append(list(line))
    return grid

# read input
def get_input() -> list:
    """Build maze as list of lists."""
    grid = []
    for _ in range(16):
        line = input()
        grid.append(list(line))
    return grid

def check_bounds(i, j):
    """Assert that indices are within bounds of the grid."""
    cond1 = i >= GRID_MIN
    cond2 = i < GRID_MAX
    cond3 = j >= GRID_MIN
    cond4 = j < GRID_MAX
    return (cond1 and cond2 and cond3 and cond4)

def get_neighbors(grid: list, i_center, j_center) -> list:
    """Return a list of neighbors of the given patch."""
    neighbors = []
    for i_diff in range(-1, 2):
        for j_diff in range(-1, 2):
            i, j = i_center+i_diff, j_center+j_diff
            if check_bounds(i, j):
                neighbors.append(grid[i][j])

    return neighbors

def is_mole(c: str) -> bool:
    """Evaluate whether this character a mole."""
    return c == "o"

def is_in_garden(neighbors) -> bool:
    """Evaluate whether mole is in the garden."""
    cond1 = "." not in neighbors
    return cond1

def is_not_in_garden(neighbors) -> bool:
    """Evaluate whether mole is not in garden."""
    cond11 = set(neighbors) == {"-", "+", "|"}
    cond12 = len(neighbors) == 5 or len(neighbors) == 3
    cond21 = set(neighbors) == {"-", "+", "|", "o"}
    cond22 = len(neighbors) == 8
    print("1", cond21)
    print("2", cond22)

    return ((cond11 and cond12) or (cond21 and cond22))

def count_moles(grid: list) -> int:
    """Count number of moles in the grid"""
    mole_counter = 0
    for i in range(len(grid)): # row
        for j in range(len(grid[i])): # col
            if is_mole(grid[i][j]):
                neighbors = get_neighbors(grid, i, j)
                if is_in_garden(neighbors) and not is_not_in_garden(neighbors):
                    mole_counter += 1
    
    return mole_counter


def main():
    grid = get_dev_input2()
    print(count_moles(grid))
    
    # accessing the grid works in the form
    # grid[row_i][col_j]

main()