import sys
import math
import copy

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

def get_cross(grid: list, i_center, j_center) -> list:
    """Return lists of vertical and horizontal outgoing patches."""
    vertical = [li[j_center] for li in grid]
    #horizontal = copy.deepcopy(grid[i_center])
    #del horizontal[j_center]
    horizontal = grid[i_center]
    grid[i_center]
    
    return horizontal, vertical

def is_mole(c: str) -> bool:
    """Evaluate whether this character a mole."""
    return c == "o"

def is_in_garden(i_center, j_center, horizontal, vertical) -> bool:
    """Evaluate whether mole is in the garden."""
    # remove other space "." and white space " "
    #hori = [x for x in horizontal if x not in [".", " "]]
    #vert = [x for x in vertical if x not in [".", " "]]
    
    # count of e must be odd on both sides
    count_hori_right = 0
    for x in horizontal[j_center+1:-1]:
        if x in ["|", "+"]:
            count_hori_right += 1
    count_hori_left = 0
    for x in horizontal[0:j_center]:
        if x in ["|", "+"]:
            count_hori_left += 1   

    count_vert_bot = 0
    for x in vertical[i_center+1:-1]:
        if x in ["-", "+"]:
            count_vert_bot += 1
    count_vert_top = 0
    for x in vertical[0:i_center]:
        if x in ["-", "+"]:
            count_vert_top += 1        

    hori_ok = count_hori_right % 2 == 1 and count_hori_left % 2 == 1
    vert_ok = count_vert_top % 2 == 1 and count_vert_bot % 2 == 1
    print(i_center, j_center, "hori", hori_ok, "vert", vert_ok)
    print(count_hori_left, count_hori_right)

    return True if hori_ok and vert_ok else False

def count_moles(grid: list) -> int:
    """Count number of moles in the grid"""
    mole_counter = 0
    for i in range(len(grid)): # row
        for j in range(len(grid[i])): # col
            if is_mole(grid[i][j]):
                horizontal, vertical = get_cross(grid, i, j)
                if is_in_garden(i, j, horizontal, vertical):
                    print(i, j, "is in garden.")
                    mole_counter += 1

    return mole_counter


def main():
    grid = get_dev_input2()
    print(count_moles(grid))
    
    # accessing the grid works in the form
    #grid[row_i][col_j]

main()