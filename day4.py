#!/usr/bin/python3
#
# https://adventofcode.com/
# 04/12/2023
#
# Simple part 1 but a frustrating (for me) part 2. I went down a recursive route when a more simple solution was required. I remembered to calculate the 
# result of the set intersection to speed things up. So as normal, a bit of parsing into the right data structures then the logic is easy.

def list_of_int_strings_to_list_of_ints( a ):
    b = list()
    for w in a.split(" "):
        if w:
            b.append(int(w))
    return b

def part1( lines ):
    s = 0
    for line in lines:
        line = line.split(": ")[1]
        (a,b) = line.split(" | ")

        common = list( set(list_of_int_strings_to_list_of_ints( a )) & set(list_of_int_strings_to_list_of_ints( b )) )
        score = 0
        if len(common) > 0:
            score = 1
            for x in range(1,len(common)):
                score *= 2
        s += score
    return s

def part2( lines ):
    map = dict()
    cards_held = dict()
    for line in lines:
        a = line.split(": ")[0]
        card = int(a.replace("Card ",""))
        line = line.split(": ")[1]
        (a,b) = line.split(" | ")

        # cache of winning number for each card - guessing this would be the expensive operation in the solution
        map[card] = len( list( set(list_of_int_strings_to_list_of_ints( a )) & set(list_of_int_strings_to_list_of_ints( b )) ))

        # record of how many cards we have
        cards_held[card] = 1

    # for each card
    for card in cards_held:
        # for each copy of a card held
        for y in range(0,cards_held[card]):
            # increment the number of cards according to the game algorithm
            for x in range(card+1,card+1+map[card]):
                cards_held[x] += 1

    return sum( n for n in cards_held.values())

if __name__ == '__main__':
    lines = []
    with open( '4.input.txt' ) as fp:
        for line in fp:
            lines.append( line[:-1] )

    print("part 1",part1( lines ))
    print("part 1",part2( lines ))
