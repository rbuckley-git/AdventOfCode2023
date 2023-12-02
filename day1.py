#!/usr/bin/python3
#
# https://adventofcode.com/
# 01/12/2023
#
# Tricky part 2. Needed to scan for numbers in words from the end of the string toward the start as the search and replace
# approach did not work.

numbers = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def part1( line1 ):
    first_digit = None
    last_digit = None
    for ch in line1:
        if ch in "0123456789":
            if first_digit == None:
                first_digit = ch
            else:
                last_digit = ch
    if last_digit == None:
        last_digit = first_digit

    return int("".join([first_digit,last_digit]))

def part2( line1 ):

    first_number = None
    last_number = None

    # scan for digit or number as word from the start
    i = 0
    while not first_number and i < len(line1):
        if line1[i] in "0123456789":
            first_number = line1[i]
        else:
            for n in range(len(numbers)):
                if numbers[n] == line1[i:i+len(numbers[n])]:
                    first_number = str(n)
                    break
        i+=1

    # scan for digit or number as word from the end back
    i = len(line1)-1
    while not last_number and i >= 0:
        if line1[i] in "0123456789":
            last_number = line1[i]
        else:
            for n in range(len(numbers)):
                if numbers[n] == line1[i:i+len(numbers[n])]:
                    last_number = str(n)
                    break
        i-=1

    return int("".join([first_number,last_number]))

if __name__ == '__main__':
    with open( '1.input.txt' ) as fp:
        s1 = 0
        s2 = 0
        for line in fp:
            s1 += part1(line[:-1])
            s2 += part2(line[:-1])
        print(s1,s2)
