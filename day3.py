#!/usr/bin/python3
#
# https://adventofcode.com/
# 03/12/2023
#
# Nice puzzle with a very straightforward part 1 followed typically by a part 2 that makes you think. Trick for me was pairing up the numbers 
# around a common "*" symbol iddentified by its coordinates.

from functools import reduce

# These are the positions around the cell that we need to check.
pos = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]

def part1( lines ):
    part_numbers = []
    n = ""
    found_symbol = False
    for y,line in enumerate( lines ):
        for x,ch in enumerate( line ):
            # if we have a digit, append it to our digit store
            if ch.isdigit():
                n += ch
                # check cells around for a symbol (non-digit and non-fullstop)
                for xx,yy in pos:
                    # quick bounds check
                    if y+yy >=0 and y+yy < len(lines) and x+xx >= 0 and x+xx < len(line):
                        neighbour = lines[y+yy][x+xx]
                        if neighbour != "." and not neighbour.isdigit():
                            # indicate we have found a symbol validating this sequence of digits
                            found_symbol = True
            elif n != "":
                # add number to our list if we found a corresponding symbol, reset and repeat
                if found_symbol:
                    part_numbers.append(int(n))
                n = ""
                found_symbol = False

    return sum(part_numbers)

def part2( lines ):
    gears = {}
    n = ""
    found_gear = False
    for y,line in enumerate( lines ):
        for x,ch in enumerate( line ):
            # if we have a digit, append it to our digit store
            if ch.isdigit():
                n += ch
                for xx,yy in pos:
                    # quick bounds check
                    if y+yy >=0 and y+yy < len(lines) and x+xx >= 0 and x+xx < len(line):
                        ch_neighbour = lines[y+yy][x+xx]
                        if ch_neighbour == "*":
                            # indicate we have found a gear validating this sequence of digits. Create a map key using the coordinates of the gear.
                            found_gear = True
                            gear = str(x+xx) + "-" + str(y+yy)

            elif n != "":
                if found_gear:
                    # create a hash keyed by the gear coordinates which is a list of our numbers
                    if gear in gears:
                        gears[gear].append( int(n) )
                    else:
                        gears[gear] = [ int(n) ]

                    None
                n = ""
                found_gear = False

    # final bit is to find the gears with more than one number attached and multiple them all together
    s = 0
    for gear in gears:
        if len(gears[gear]) > 1:
            s += reduce((lambda x,y: x * y), gears[gear] )
    return s


if __name__ == '__main__':
    # Simple parse of file into an array of lines
    lines = []
    with open( '3.input.txt' ) as fp:
        for line in fp:
            lines.append( line[:-1] )
            
    print(part1(lines))
    print(part2(lines))