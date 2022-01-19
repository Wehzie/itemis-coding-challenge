import sys
import math
import copy

DEBUG = False
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


def get_dev_input3() -> list:
    """Build a maze for development purposes."""
    form1 = (
"""+--------------+
|   o      oo  |
| +----------+o|
| |..........| |
| |.+------+o|o|
| |.|      |.| |
| |o| +--+o|.| |
| |.| |oo|o|.| |
| |.| +--+ |.| |
| |.|  oo  |.| |
| |.|oooooo|.| |
| |.+------+o|o|
|o|..........| |
|o+----------+ |
|      o   o   |
+--------------+""")

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

def collapse(li: list, axis: str) -> list:
    """Collapse a fence to a single element."""
    if axis == "hori":
        old_tokens = ["+", "-"]
        new_token = "|"
    elif axis == "vert":
        old_tokens = ["+", "|"]
        new_token = "-"
    else:
        raise ValueError("axis must be 'hori' or 'vert'")

    new_li = []
    plus_count = 0
    for x in li:

        if x == "+":
            plus_count += 1
            
            if plus_count % 2 == 1:
                new_li.append(new_token)

        if x in old_tokens:
            continue
        
        new_li.append(x)
    
    return new_li

def is_in_garden(i_center, j_center, horizontal, vertical) -> bool:
    """Evaluate whether mole is in the garden."""
    # denote current mole
    vertical[i_center] = "x"
    horizontal[j_center] = "x"

    if DEBUG:
        print("i_cent", i_center, "j_cent", j_center)
        print("vert")
        print(vertical)
        print("hori")
        print(horizontal)

    # remove other space ".", white space " " and other "o"s
    hori = [x for x in horizontal if x not in [".", " ", "o"]]
    vert = [x for x in vertical if x not in [".", " ", "o"]]
    # collapse fences along a single axis
    hori = collapse(hori, "hori")
    vert = collapse(vert, "vert")
    
    # get new indices
    j = hori.index("x")
    i = vert.index("x")

    if DEBUG:
        print("i", i, "j", j)
        print("vert_clean")
        print(vert)
        print("hori_clean")
        print(hori)


    
    hori_ok, vert_ok = False, False
    # perform bound checks
    
    if j >= 0 and j < len(hori) and i >= 0 and i < len(vert):
        hori_left = len(hori[0:j])
        hori_right = len(hori[j:-1])
        hori_ok = min(hori_left, hori_right) % 2 == 1
        
        vert_top = len(vert[0:i])
        vert_bot = len(vert[i:-1])
        vert_ok = min(vert_top, vert_bot) % 2 == 1
        
        if DEBUG:
            print("hori_left", hori_left, "hori_right", hori_right)
            print("vert_top", vert_top, "vert_bot", vert_bot)
        
    if DEBUG:
        print("#########")
        print("")

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
    #grid = get_dev_input2()
    #print(count_moles(grid))

    grid = get_dev_input3()
    print(count_moles(grid))
    
    # accessing the grid works in the form
    #grid[row_i][col_j]

main()