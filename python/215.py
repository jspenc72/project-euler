#!/usr/bin/env python

L=32
H=10
bricks = [2,3]

configs = []
adj = []
d = {}

def addconfigs(c,n):
    if n == L: configs.append(c-1)
    elif n < L:
        for b in bricks:
            addconfigs((c<<b)+1, n+b)

def numw(prev, y):
    if y == H: return 1
    if (prev,y) in d: return d[(prev,y)]
    total = 0
    for i in xrange(len(adj[prev])):
        if not adj[prev][i]: continue
        total += numw(i, y+1)
    d[(prev,y)] = total
    return total

addconfigs(0,0)

for i in xrange(len(configs)):
    adj.append([False]*len(configs))

for i in xrange(len(configs)):
    for j in xrange(i+1, len(configs)):
        if configs[i] & configs[j] == 0:
            adj[i][j] = True
            adj[j][i] = True

total=0
for i in xrange(len(adj)):
    total += numw(i,1)
print total
