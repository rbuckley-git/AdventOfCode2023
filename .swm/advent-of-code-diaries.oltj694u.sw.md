---
title: Advent of Code diaries
---
These are a summary of my notes from 2023 AoC challenge. Nice to get some quick wins in. Eventually ran out of time and energy for the late nights these challenges involve for me. I might try to catch up with a few puzzles&nbsp;

## Day 1

Tricky part 2. Needed to scan for numbers in words from the end of the string toward the start as the search and replace approach did not work.

<SwmSnippet path="/day1.py" line="15">

---

This was the bit I learned fro this exercise, the quick way to check if a character is a digit.

```python
        if ch.isdigit():
```

---

</SwmSnippet>

<SwmSnippet path="/day1.py" line="36">

---

This bit looks for each number as a word at <SwmToken path="/day1.py" pos="31:1:1" line-data="    i = 0">`i`</SwmToken>. I think this can be improved and use startswith instead.

```python
            for n in range(len(numbers)):
                if numbers[n] == line1[i:i+len(numbers[n])]:
                    first_number = str(n)
```

---

</SwmSnippet>

## Day 2

Nice easy one for after Day 1 little catch in part 2. Simple parsing to get data in right form to then apply the game logic.

## Day 3

Nice puzzle with a very straightforward part 1 followed typically by a part 2 that makes you think. Trick for me was pairing up the numbers around a common "\*" symbol identified by its coordinates.

### Day 4

Simple part 1 but a frustrating (for me) part 2. I went down a recursive route when a more simple solution was required. I remembered to calculate the result of the set intersection to speed things up. So as normal, a bit of parsing into the right data structures then the logic is easy.

<SwmSnippet path="/day4.py" line="9">

---

This code snippet converts a list of integer strings `a` into a list of integers `b`. It accomplishes this by splitting the input string `a` on spaces, converting each element to an integer using the `int()` function, and appending the integer to the list `b`.

```python
def list_of_int_strings_to_list_of_ints( a ):
    b = list()
    for w in a.split(" "):
        if w:
            b.append(int(w))
    return b
```

---

</SwmSnippet>

<SwmSnippet path="/day4.py" line="31">

---

This code snippet takes a list of strings as input and performs calculations to determine the total number of cards held. It does this by parsing each string and extracting relevant information, such as card numbers and a pair of numbers separated by a vertical bar. It then uses this information to update two dictionaries: `map` and `cards_held`. Finally, it calculates the sum of the values in `cards_held` and returns it.

```python
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
```

---

</SwmSnippet>

## Day 5

Part 1 was nice. Part 2 was something to do with optimising the ranges but too tired to work it out.

## Day 6

Nice and simple today given the nightmare of last night! No need for a parser as the data was simple. There is probably a nice optimisation to run it quicker but bute force was quick enough to get the answer. Perfection being the enemy of done, I left it with the gold star achieved.

## Day 7

Part 1 was ok but felt like I was knife and forking it. Part 2 was a bugger and I am not happy with my solution. Too much copy and paste and only deals with up to 5 Js rather than the generic case of N Js. Need sleep.&nbsp;

One thing I did was to keep the bid value close to the answer so the final calculation was easy.

## Day 8

I remembered the LCM trick from 2019 so reused that and amazingly got the right answer - boom!

## Day 9

I had a silly bug in my first implementation. I was incorrectly finding the all zeros state by summing elements and checking for zero. Of course this does not work in all cases as a -5 and a +5 would give a zero too. Changed to check each cell is a value of zero and the answer popped out.

## Day 10

Nice pretty pipe maze printed out. No idea how to solve part 2. Need sleep.

## Day 15

Only part 1 working. Gave up on the challenge after this as I had other commitments to deal with.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBQWR2ZW50T2ZDb2RlMjAyMyUzQSUzQXJidWNrbGV5LWdpdA==" repo-name="AdventOfCode2023"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
