#!/usr/bin/python3
#
# https://adventofcode.com/
# 02/12/2023
#
# Nice easy one for today after yesterdays little catch in part 2. Simple parsing to get data in right form to then apply the game logic.


def part1():
    solution =  {
                "red": 12,
                "green":  13,
                "blue": 14
                }

    with open( '2.input.txt' ) as fp:
        s = 0
        for line in fp:
            a,b = line[:-1].split(": ")
            game = int(a.replace("Game ",""))

            possible = True
            for attempt in b.split("; "):
                for cube in attempt.split(", "):
                    (n,colour) = cube.split(" ")
                    if int(n) > solution[colour]:
                        possible = False
            if possible:
                s += game

            print(game,"possible",possible)
    return s

def part2():
    with open( '2.input.txt' ) as fp:
        s = 0
        for line in fp:
            a,b = line[:-1].split(": ")

            maxs = {"red": 0, "blue": 0, "green": 0 }

            for attempt in b.split("; "):
                for cube in attempt.split(", "):
                    (n,colour) = cube.split(" ")
                    maxs[colour] = max(maxs[colour],int(n))
            # power is the product of all maximums
            power = 1
            for colour in maxs:
                power *= maxs[colour]

            print(maxs,power)
            # answer is sum of all powers
            s += power
    return s

if __name__ == '__main__':
    print(part1())
    print(part2())