#!/usr/bin/python3
#
# https://adventofcode.com/
# 08/12/2023
#
# I remembered the LCM trick from 2019 so reused that and amazingly got the right answer - boom!

import math

# obtain lowest common multiple from the series of integers passed in
def lcm( periods ):
    ans = 1
    for i in range(len(periods)):
        ans = ans * periods[i] // math.gcd(ans,periods[i])

    return ans

def part1( hash ):
    looping = True
    start = 'AAA'
    count = 0
    while looping:
        for i in instructions:
            h = hash[start]
            if i == "L":
                start = h[0]
            elif i == 'R':
                start = h[1]
            count += 1
            if start == 'ZZZ':
                looping = False
                break
    return count

def part2_find( hash, start ):
    looping = True
    count = 0
    while looping:
        for i in instructions:
            h = hash[start]
            if i == "L":
                start = h[0]
            elif i == 'R':
                start = h[1]
            count += 1
            if start[2] == 'Z':
                looping = False
                break
    return count

def part2( hash ):
    # find keys that end in "A"
    periods = []
    for k in hash.keys():
        if k[2] == "A":
            periods.append( part2_find(hash,k) )

    return lcm(periods)


if __name__ == '__main__':

    instructions = None
    hash = {}
    with open( '8.input.txt' ) as fp:
        for line in fp:
            line = line[:-1]
            if instructions == None:
                instructions = line
            elif line == "":
                continue
            else:
                # AAA = (BBB, BBB)
                a = line[0:3]
                b = line[7:10]
                c = line[12:15]
                hash[a] = (b,c)


    print("Part 1",part1(hash))
    print("Part 2",part2(hash))
