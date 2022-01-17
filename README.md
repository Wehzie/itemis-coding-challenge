# itemis-coding-challenge

- Author: Rafael Tappe Maestro
- Date: January 2022

## Mole Hill Problem

### Example

Input

-+
0|
-+

0|
-+

+-+
|o|
+-+

```
................
................
..+----------+..
..|          |..
..|   o      |..
..|      o   |..
..|          |..
..+----------+..
................
............o...
.....o..........
................
.........o......
................
................
................
```

Output

```
2
```

### Notes

    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

- we cannot assume that the garden has a rectangle shape
- a mole in the garden cannot have "." as a neighbor
- its not possible to distinguish the following cases using only 8 neighbors

        # outside
        +-+
        oo|
        +-+

        # inside
        +--+
        |oo|
        +--+

- need to use bracket matching: open fence | count moles, close fence |