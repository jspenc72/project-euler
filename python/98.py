#!/usr/bin/env python

from itertools import count

def freqdict(word):
    d = {}
    d2 = {}
    for letter in word:
        if letter in d: d[letter] += 1
        else: d[letter] = 1
    for freq in d.values():
        if freq in d2: d2[freq] += 1
        else: d2[freq] = 1
    return d2

freq = {}
anagrams = {}
squares = []

with open('input/words.txt') as f:
    arr = f.readline().split('","')
    arr[0] = arr[0].lstrip('"')
    p = len(arr)-1
    arr[p] = arr[p].rstrip('"')

for j in count(1):
    t = str(j*j)
    if len(t) > 9: break
    squares.append(t)
squareset = set([int(sq) for sq in squares])

for word in arr:
    s = ''.join(sorted(word))
    if s in freq: freq[s].append(word)
    else: freq[s] = [word]

for grams in freq:
    if len(freq[grams]) > 1: anagrams[grams] = freq[grams]

maxsq = 0
for words in anagrams.values():
    for i in xrange(len(words)):
        w = words[i]
        fd = freqdict(w)
        for sq in squares:
            if len(sq) > len(w): break
            if freqdict(sq) != fd: continue
            lmap = {}
            for j in xrange(len(w)): lmap[w[j]] = sq[j]
            for j in xrange(i+1, len(words)):
                w2 = words[j]
                num = ''
                for c in w2: num += lmap[c]
                if num[0] == '0': continue
                n = int(num)
                if not n in squareset: continue
                maxsq = max(maxsq, n, int(sq))
print maxsq
