#!/usr/bin/env python

p=-9
q=-4
k=-14
r=-20
s=-9
l=-28

start = [[0,-1],[0,1],[-3,-2],[-3,2],[-4,-5],[-4,5],[2,-7],[2,7]]


sols = set([])

for x,y in start:
    for i in xrange(20):
        t=x
        x = p*x+q*y+k
        y = r*t+s*y+l
        if x>0: sols.add(x)

arr = list(sols)
arr.sort()
print sum(arr[i] for i in xrange(30))
