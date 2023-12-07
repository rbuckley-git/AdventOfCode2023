#!/usr/bin/python3
#
# https://adventofcode.com/
# 07/12/2023
#
# Part 1 was ok but felt like I was knife and forking it. Part 2 was a bugger and I am not happy with my solution. Too much copy and paste and only deals with up to 5 Js
# rather than the generic case of N Js. Need sleep.
# One thing I did was to keep the bid value close to the answer so the final calculation was easy.

def set_hand( hand ):
    s = {}
    for ch in hand:
        if ch in s:
            s[ch] += 1
        else:
            s[ch] = 1
    return s

# 7. Five of a kind, where all five cards have the same label: AAAAA
def is_five_of_a_kind( sh ):
    if len(sh) == 1:
        return True
    return False

# 6. Four of a kind, where four cards have the same label and one card has a different 
# label: AA8AA
def is_four_of_a_kind( sh ):
    for k,v in sh.items():
        if v == 4:
            return True
    return False

# 5. Full house, where three cards have the same label, and the remaining two cards share a 
# different label: 23332
def is_full_house( sh ):
    if len(sh) == 2:
        return True
    return False

# 4. Three of a kind, where three cards have the same label, and the remaining two cards 
# are each different from any other card in the hand: TTT98
def is_three_of_a_kind( sh ):
    s1 = [v for v in sh.values()]
    s1.sort()
    if s1 == [1,1,3]:
        return True
    return False

# 3. Two pair, where two cards share one label, two other cards share a second label, 
# and the remaining card has a third label: 23432
def is_two_pair( sh ):
    s1 = [v for v in sh.values()]
    s1.sort()
    if s1 == [1,2,2]:
        return True
    return False

# 2. One pair, where two cards share one label, and the other three cards have a different 
# label from the pair and each other: A23A4
def is_one_pair( sh ):
    s1 = [v for v in sh.values()]
    s1.sort()
    if s1 == [1,1,1,2]:
        return True
    return False

# 1. High card, where all cards' labels are distinct: 23456
def is_high_card( sh ):
    if len(sh) == 5:
        return True
    return False

def part1_sorted_hands( hands ):
    card_scoring = {'A': 'D', 'K': 'C', 'Q': 'B', 'J': 'A', 'T': '9', '9': '8', '8': '7', '7': '6', '6': '5', '5': '4', '4': '3', '3': '2', '2': '1'}
    return sorted_hands( hands, card_scoring )

# slightly differet sorting logic for 
def part2_sorted_hands( hands ):
    card_scoring = {'A': 'D', 'K': 'C', 'Q': 'B', 'T': 'A', '9': '9', '8': '8', '7': '7', '6': '6', '5': '5', '4': '4', '3': '3', '2': '2', 'J': '1'}
    return sorted_hands( hands, card_scoring )

def sorted_hands( hands, card_scoring ):
    hh = {}
    for (hand,bid) in hands:
        h = ""
        for ch in hand:
            h += card_scoring[ch]
        i = int(h,16)
        hh[(hand,bid)] = i

    values = list(hh.values())
    values.sort(reverse=True)

    ret = []
    for val in values:
        for k,v in hh.items():
            if v == val:
                ret.append(k)
                break

    return ret

def get_score(hand):
    score = 0
    sh = set_hand(hand)
    if is_five_of_a_kind(sh):
        score = 7
    elif is_four_of_a_kind(sh):
        score = 6
    elif is_full_house(sh):
        score = 5
    elif is_three_of_a_kind(sh):
        score = 4
    elif is_two_pair(sh):
        score = 3
    elif is_one_pair(sh):
        score = 2
    elif is_high_card(sh):
        score = 1
    return score

def part1( hands ):
    l = {}
    for (hand,bid) in hands:
        score = get_score(hand)
        if score not in l:
            l[score] = list()
        l[score].append((hand,bid))
    ll = []
    for x in range(7,0,-1):
        if x in l:
            h = l[x]
            if len(h) == 1:
                ll.append(h[0])
            else:
                ll.extend(part1_sorted_hands(h))
    ll.reverse()                

    s = 0
    for i,(hand,bid) in enumerate(ll,start=1):
        s += i * int(bid)

    return s

# need to deal with all 5 cards being J. Try every permutation of J and record maximum scoring values.
def maximise_hand( hand ):
    other_cards = "AKQT98765432"
    js = hand.count("J")
    hand = hand.replace("J","")
    m = 0
    keep = None
    for j1 in other_cards:
        if js == 1:
            replacement = j1
            score = get_score( hand + replacement )
            if score > m:
                m = score
                keep = hand + replacement
        else:
            for j2 in other_cards:
                if js == 2:
                    replacement = j1+j2
                    score = get_score( hand + replacement )
                    if score > m:
                        m = score
                        keep = hand + replacement
                else:
                    for j3 in other_cards:
                        if js == 3:
                            replacement = j1+j2+j3
                            score = get_score( hand + replacement )
                            if score > m:
                                m = score
                                keep = hand + replacement
                        else:
                            for j4 in other_cards:
                                if js == 4:
                                    replacement = j1+j2+j3+j4
                                    score = get_score( hand + replacement )
                                    if score > m:
                                        m = score
                                        keep = hand + replacement
                                else:
                                    for j5 in other_cards:
                                        replacement = j1+j2+j3+j4+j5
                                        score = get_score( hand + replacement )
                                        if score > m:
                                            m = score
                                            keep = hand + replacement

    return keep

def part2( hands ):
    l = {}
    for (hand,bid) in hands:
        original_hand = hand
        if 'J' in hand:
            hand = maximise_hand(hand)

        score = get_score(hand)
        if score not in l:
            l[score] = list()
        l[score].append((original_hand,bid))
    ll = []

    for x in range(7,0,-1):
        if x in l:
            h = l[x]
            if len(h) == 1:
                ll.append(h[0])
            else:
                ll.extend(part2_sorted_hands(h))
    ll.reverse()                

    s = 0
    for i,(hand,bid) in enumerate(ll,start=1):
        s += i * int(bid)

    return s

if __name__ == '__main__':

    hands = []
    with open( '7.input.txt' ) as fp:
        for line in fp:
            (hand,bid) = line[:-1].split(" ")
            hands.append( (hand,bid) )
    
    print("part 1",part1( hands ))
    print("part 2",part2( hands ))
