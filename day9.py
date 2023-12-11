#!/usr/bin/python3
#
# https://adventofcode.com/
# 09/12/2023
#
# I had a silly bug in my first implementation. I was incorrectly finding the all zeros state by summing elements and checking for zero. 
# Of course this does not work in all cases as a -5 and a +5 would give a zero too. Changed to check each cell is a value of zero and 
# the answer popped out.


def part1( line ):
    next_line = []
    for i in range(len(line)-1):
        next_line.append( line[i+1] - line[i] )

    if all(y==0 for y in next_line):
        return line[-1]
    else:
        return line[-1] + part1(next_line)

def part2( line ):
    next_line = []
    for i in range(len(line)-1):
        next_line.append( line[i+1] - line[i] )

    if all(y==0 for y in next_line):
        return line[0]
    else:
        return line[0] - part2(next_line)

if __name__ == '__main__':

    lines = []
    with open( '9.input.txt' ) as fp:
        for line in fp:
            line = line[:-1]
            lines.append( [ int(x) for x in line.split(" ") ] )

    ans = 0
    for line in lines:
        ans += part1(line)

    print("Part 1",ans)

    ans = 0
    for line in lines:
        ans += part2(line)

    print("Part 2",ans)
