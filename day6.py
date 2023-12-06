#!/usr/bin/python3
#
# https://adventofcode.com/
# 06/12/2023
#
# Nice and simple today given the nightmare of last night! No need for a parser as the data was simple.
# There is probably a nice optimisation to run it quicker but bute force was quick enough to get the answer.
# Perfection being the enemy of done, I left it with the gold star achieved.

# Time:      7  15   30
# Distance:  9  40  200
games1test = [
    { "t":  7, "d": 9},
    { "t": 15, "d": 40},
    { "t": 30, "d": 200},
]

games1 = [
    { "t":  71530, "d": 940200}
]

# Time:        53     71     78     80
# Distance:   275   1181   1215   1524
games2test = [
    { "t": 53, "d": 275},
    { "t": 71, "d": 1181},
    { "t": 78, "d": 1215},
    { "t": 80, "d": 1524}
]

games2 = [
    { "t": 53717880, "d": 275118112151524}
]

def solve( games ):
    ans = 1
    for game in games:
        tt = game["t"]

        speed = 0
        ways = 0
        for t in range( 1, tt ):
            speed += 1
            if ( (tt-t)*speed > game["d"] ):
                ways += 1
        ans *= ways
    return ans

if __name__ == '__main__':
    print("part 1 tes:",solve(games1test))
    print("part 1:",solve(games1))
    print("part 2 test:",solve(games2test))
    print("part 2:",solve(games2))
        