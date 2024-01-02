---
title: Advent of Code diaries
---
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

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBQWR2ZW50T2ZDb2RlMjAyMyUzQSUzQXJidWNrbGV5LWdpdA==" repo-name="AdventOfCode2023"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
