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

- even_odd expects that the number of fence-symbols is uneven on both axes. This doesn't work because of the following case. The mole should be inside the garden.

    +--+ o |

- need to use bracket matching: open fence | count moles, close fence |. Update: matching alone isn't enough because of nested gardens. Counting the number of fence symbols on an axis doesn't solve this because an o may lie on one axis with a fence piece.