#!/usr/bin/python3
#
# https://adventofcode.com/
# 10/12/2023
#
# Nice pretty pipe maze printed out. No idea how to solve part 2. Need sleep.

import sys

# These are the input and output of each pipe part
connects = {
    "-": [(0,-1), (0,1)],
    "|": [(-1,0), (1,0)],
    "7": [(0,-1),  (1,0)],   # left and below
    "J": [(0,-1),  (-1,0)],  # left and above
    "L": [(-1,0),  (0,1)],   # above and right
    "F": [(1,0), (0,1)]      # below and right
}

# All the moves to consider at start
pos = [(-1,0),(1,0),(0,-1),(0,1)]

# Allow us to print a nice picture later
grid = {}

def find_start( rows ):
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            if rows[r][c] == "S":
                return (r,c)
    return (None,None)

def move( s, prev = None, i=1 ):
    ans = 0
    cell = rows[s[0]][s[1]]
    grid[s] = cell

    # Just follow the pipe one way
    followed = False

    # establish the moves that this pipe can have. Consider all moves for the start location
    moves = pos
    if cell != "S":
        moves = connects[cell]

    for p in moves:
        # calculate next cell position
        q = (s[0] + p[0],s[1] + p[1] )
        # check we are looking at pipe
        if rows[q[0]][q[1]] != ".":
            if not prev or q != prev:
                if q == start:
                    return i
                # reverse the move p
                r = (p[0]*-1,p[1]*-1)
                connector = connects[rows[q[0]][q[1]]]
                if r in connector:
                    ans += move( (q[0], q[1]), s, i+1 )
                    followed = True

        if followed:
            break

    return ans

if __name__ == '__main__':
    # going deep
    sys.setrecursionlimit(10**6)

    rows = []
    with open( '10.test3.input.txt' ) as fp:
        for line in fp:
            line = line[:-1]
            rows.append( [ch for ch in line] )

    row_count = len(rows)
    col_count = len(rows[0])

    start = find_start(rows)

    print("Part 1",int(move(start)/2))
#  S-------7I
#  |F-----7|I
#  ||     || 
#  ||     || 
#  |L-7 F-J| 
#  |II| |II| 
#  L--J L--J 

# F7FSF7F7F7F7F7F---7
#  |LJ||||||||||||F--J
#  L-7LJLJ||||||LJL-7 
# F--JF--7||LJLJ F7FJ 
# L---JF-JLJ    FJLJ  
#    F-JF---7   L7    
#   FJF7L7F-JF7IIL---7
#   L-JL7||F7|L7F-7F7|
#      FJ|||||FJL7||LJ
#      L-JLJLJL--JLJI 

    cells_inside = 0
    for r in range(row_count):
        line = ""
        inside = False
        for c in range(col_count):
            if (r,c) in grid:
                line += grid[(r,c)]
                inside = not inside
            else:
                if inside and c != col_count-1:
                    cells_inside += 1
                    line += "I"
                else:
                    line += " "

        print(line)
    print("Part 2",cells_inside)