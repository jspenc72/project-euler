#!/usr/bin/env python
from gmpy import mpf

off = [(0,1), (1,0), (0,-1), (-1,0)]
paths = [ [[0]*900 for j in xrange(900)] for i in xrange(2) ]

for i in xrange(900):
    paths[0][i][i] = 1
for r in xrange(50):
    print r
    c = (r+1)%2
    p = r%2
    for i in xrange(900):
        y, x = i//30, i%30
        adj = []
        for o in off:
            xo, yo = x+o[0], y+o[1]
            if xo<0 or xo>=30 or yo<0 or yo>=30: continue
            k = yo*30 + xo
            adj.append(k)
        for j in xrange(i+1):
            paths[c][j][i] = 0
            for a in adj: paths[c][i][j] += paths[p][max(j,a)][min(j,a)]

total_paths = [0]*900 # total paths of length 50 starting from pos i
for i in xrange(900):
    total_paths[i] = sum(paths[0][max(i,j)][min(i,j)] for j in xrange(900))
ans = 0.0
for i in xrange(900):
    e = 1.0
    for j in xrange(900):
        p = float(total_paths[j] - paths[0][max(i,j)][min(i,j)])/total_paths[j]
        e *= p
    ans += e
print ans
