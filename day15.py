#!/usr/bin/python3
#
# https://adventofcode.com/
# 15/12/2023
#
# Only part 1 working

def display_pattern( lines ):
    for i,line in enumerate(lines):
        print(i,line)

def find_horizontal_reflection( lines ):
    start = len(lines)-2

    found = False
    while not found and start >= 0:
        matching = True
        i = start
        j = start + 1
        # print("matching",start,i,j)
        while matching and i >= 0 and j < len(lines):
            # print(start,i,lines[i],j,lines[j],matching)
            if lines[i] != lines[j]:
                matching = False
            i -= 1
            j += 1

        if matching:
            found = True
        else:
            start -= 1
    
    if found:
        # print("Horizontal found at",start)
        return start + 1
    
    return 0

def get_vertical(lines,i):
    return "".join(x[i] for x in lines)

def find_vertical_reflection( lines ):
    # print("check vertical")
    start = len(lines[0])-2

    found = False
    while not found and start >= 0:
        matching = True
        i = start
        j = start + 1
        # print("matching",start,i,j)
        while matching and i >= 0 and j < len(lines[0]):
            # print(start,i,get_vertical(lines,i),j,get_vertical(lines,j))
            if get_vertical(lines,i) != get_vertical(lines,j):
                matching = False
            i -= 1
            j += 1
        if matching:
            found = True
        else:
            start -= 1
    
    if found:
        # print("Vertical found at",start)
        return start + 1
    
    return 0


def process( lines ):
    # print("new pattern")
    # display_pattern(lines)
    ans = find_horizontal_reflection(lines) * 100
    ans += find_vertical_reflection(lines)

    return ans

if __name__ == '__main__':

    mirrors = []
    with open( '15.test.input.txt' ) as fp:
        lines = []
        for line in fp:
            line = line.strip()
            if line == "":
                mirrors.append( lines )
                lines = []
            else:
                lines.append(line)
        mirrors.append( lines )

    part1 = 0
    for mirror in mirrors:
        part1 += process(mirror)

    print("Part 1",part1)

    part2 = 0
    for i,mirror in enumerate(mirrors):
        print("Mirror",i)
        original_score = process(mirror)
        print("Original score",original_score)
        looping = True
        while looping:
            for x in range(len(mirror[0])):
                for y in range(len(mirror)):
                    smudge = mirror
                    print("original")
                    display_pattern(smudge)
                    cell = smudge[y][x]
                    if cell == ".":
                        cell = "#"
                    else:
                        cell = "."

                    line = [x for x in smudge[y]]
                    line[x] = cell
                    smudge[y] = "".join(line)
                    print("modified")
                    display_pattern(smudge)
                    
                    new_score = process(smudge)
                    if new_score > 0:
                        part2 += new_score
                        print("New",new_score,x,y)
                        looping = False
                        break
                if not looping:
                    break
            looping = False
    print("Part 2",part2)
