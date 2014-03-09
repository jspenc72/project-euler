#!/usr/bin/env python

p=-9
q=-4
k=-2
r=-20
s=-9
l=-4

start = [[0,-1],[0,1],[-1,-2],[-1,2],[2,-5]]


sols = set([])

for x,y in start:
    for i in xrange(20):
        t=x
        x = p*x+q*y+k
        y = r*t+s*y+l
        if x>0: sols.add(x)

arr = list(sols)
arr.sort()
print arr[14]
