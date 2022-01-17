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
|o       o  o|..
+-+   oo     |..
oo|      o   |..
+-+ o+-------+..
|o   |..........
+----+..........
............o...
.....o..........
................
.........o......
................
................
o...............""")

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
    horizontal = grid[i_center]
    grid[i_center]
    
    return horizontal, vertical

def is_mole(c: str) -> bool:
    """Evaluate whether this character a mole."""
    return c == "o"

def is_in_garden(i_center, j_center, horizontal, vertical) -> bool:
    """Evaluate whether mole is in the garden."""
    # denote current mole
    vertical[i_center] = "x"
    horizontal[j_center] = "x"

    #print("i_cent", i_center, "j_cent", j_center)
    #print("vert")
    #print(vertical)
    #print("hori")
    #print(horizontal)

    i = int(i_center
        - vertical[0:i_center+1].count(".") 
        - vertical[0:i_center+1].count(" ")
        - vertical[0:i_center+1].count("o"))
    j = int(j_center
        - horizontal[0:j_center+1].count(".")
        - horizontal[0:j_center+1].count(" ")
        - horizontal[0:j_center+1].count("o"))
    #print("i", i, "j", j)

    # remove other space "." and white space " "
    hori = [x for x in horizontal if x not in [".", " ", "o"]]
    vert = [x for x in vertical if x not in [".", " ", "o"]]
    #print("vert_clean")
    #print(vert)
    #print("hori_clean")
    #print(hori)

    #print("#########")
    #print("")
    
    hori_ok, vert_ok = False, False
    if j-1 >= 0 and j+1 < len(hori) and i-1 >= 0 and i+1 < len(vert):
        hori_ok = hori[j-1] in ["|", "+"] and hori[j+1] in ["|", "+"]
        vert_ok = vert[i-1] in ["-", "+"] and vert[i+1] in ["-", "+"]

    # convert "x" back to "o" (was pass by reference)
    for x in range(len(vertical)):
        if vertical[x] == "x":
            vertical[x] = "o"
    for x in range(len(horizontal)):
        if horizontal[x] == "x":
            horizontal[x] = "o"

    return True if hori_ok and vert_ok else False

def count_moles(grid: list) -> int:
    """Count number of moles in the grid"""
    mole_counter = 0
    for i in range(len(grid)): # row
        for j in range(len(grid[i])): # col
            if is_mole(grid[i][j]):
                horizontal, vertical = get_cross(grid, i, j)
                if is_in_garden(i, j, horizontal, vertical):
                    #print(i, j, "is in garden.")
                    mole_counter += 1

    return mole_counter


def main():
    grid = get_dev_input2()
    print(count_moles(grid))
    
    # accessing the grid works in the form
    #grid[row_i][col_j]

main()