#!/usr/bin/python3
#
# https://adventofcode.com/
# 05/12/2023
#
# Part 1 was nice. Part 2 was something to do with optimising the ranges but too tired to work it out.

import json
import sys

almanac = {}

# static mapping for convenience
phases = {
    "seed-soil": "soil-fertilizer",
    "soil-fertilizer": "fertilizer-water",
    "fertilizer-water": "water-light",
    "water-light": "light-temperature",
    "light-temperature": "temperature-humidity",
    "temperature-humidity": "humidity-location",
    "humidity-location": None
}

def convert_source_to_dest( s, name ):
    for m in almanac[name]:
        if m[1] <= s <= m[1] + m[2]:
            return m[0] + s - m[1]
    return s

if __name__ == '__main__':
    lines = []
    with open( '5.input.txt' ) as fp:
        for line in fp:
            lines.append( line[:-1] )

    # extract the seeds
    seeds = list(map(int, lines[0].split(": ")[1].split(" ")) )
    (s,d) = (None,None)
    l = list()
    for line in lines[1:]:
        if line == "":
            if len(l):
                almanac[s + "-" + d] = l
                l = list()
        elif line.find("map:")>-1:
            (s,d) = line.split(" ")[0].split("-to-")
        else:
            (dest_start,source_start,range_len) = list(map(int, line.split(" ")) )
            l.append((dest_start,source_start,range_len))
    if len(l):
        almanac[s + "-" + d] = l

    ans1 = sys.maxsize
    for x in seeds:
        phase = "seed-soil"
        while phase:
            x = convert_source_to_dest(x,phase)
            phase = phases[phase]
        ans1 = min( ans1, x)

    print("part 1:",ans1)

