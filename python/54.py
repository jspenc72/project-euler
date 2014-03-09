#!/usr/bin/env python

def flush(hand):
    suit = hand[0][1]
    for i in xrange(1,len(hand)):
        if hand[i][1] != suit: return False
    return True

def straight(hand):
    ordered = set(sorted([card[0] for card in hand]))
    for i in xrange(2,15):
        if not i in ordered: continue
        for j in xrange(i+1,i+5):
            if not j in ordered: return False
        return True

def numinkind(hand):
    freq = [0]*15
    for card in hand:
        freq[card[0]] += 1
    return max(freq)

def fhouse(hand):
    freq = [0]*15
    for card in hand:
        freq[card[0]] += 1
    return (2 in freq and 3 in freq)

def twop(hand):
    freq = [0]*15
    for card in hand:
        freq[card[0]] += 1
    if 2 in freq:
        freq.remove(2)
        if 2 in freq: return True
    return False

def high(hand):
    vals = (card[0] for card in hand)
    return max(vals)

def htype(hand):
    st = straight(hand)
    fl = flush(hand)
    if st or fl:
        vals = [card[0] for card in hand]
        vals.sort()
        vals.reverse()
    if st and fl: return (8,vals)
    if fl: return (5,vals)
    if st: return (4,vals)
    freq = [0]*15
    for card in hand: freq[card[0]] += 1
    dups = max(freq)
    if dups == 4: return (7, [freq.index(4)]*4 + [freq.index(1)])
    if fhouse(hand): return (6, [freq.index(3)]*3 +[freq.index(2)]*2)
    smallest = 0
    if dups == 3:
        for i in xrange(len(freq)):
            if freq[i] == 1:
                smallest = i
                freq[i] = 0
                break
        return (3, [freq.index(3)]*3 + [freq.index(1)] + [smallest])
    if dups == 2:
        small2 = freq.index(2)
        freq[small2] = 0
        try:
            large2 = freq.index(2)
            return (2, [large2]*2 + [small2]*2 + [freq.index(1)])
        except ValueError:
            order = []
            for i in xrange(len(freq)-1,-1,-1):
                if freq[i] == 1: order.append(i)
            return (1, [small2]*2 + order)
    else:
        vals = [card[0] for card in hand]
        vals.sort()
        vals.reverse()
        return (0,vals)

f = open('input/poker.txt')
total = 0
for line in f:
    if len(line) < 5: continue
    arr = line.split()
    for i in xrange(len(arr)):
        card = arr[i]
        t = [0,0]
        val = card[0]
        if val == 'T': t[0] = 10
        elif val == 'J': t[0] = 11
        elif val == 'Q': t[0] = 12
        elif val == 'K': t[0] = 13
        elif val == 'A': t[0] = 14
        else: t[0] = int(val)
        suit = card[1]
        if suit == 'C': t[1] = 0
        elif suit == 'D': t[1] = 1
        elif suit == 'H': t[1] = 2
        elif suit == 'S': t[1] = 3
        t = tuple(t)
        arr[i] = t
    p1 = arr[:5]
    p2 = arr[5:]
    h1 = htype(p1)
    h2 = htype(p2)
    if h1[0] > h2[0]: total += 1
    elif h1[0] == h2[0]:
        for i in xrange(5):
            if h1[1][i] > h2[1][i]:
                total += 1
                break
            elif h1[1][i] == h2[1][i]: continue
            else: break
print total
