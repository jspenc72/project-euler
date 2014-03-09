#!/usr/bin/env python

p,q,k,r,s,l=-9,-8,8,-10,-9,8
x,y=0,1

sols = set([])

for i in xrange(20):
    t=x
    x = p*x+q*y+k
    y = r*t+s*y+l
    if y>0: sols.add(y)

p=-9
q=-8
k=-8
r=-10
s=-9
l=-8
p,q,k,r,s,l=-9,-8,-8,-10,-9,-8
x,y=0,-1
for i in xrange(20):
    t=x
    x = p*x+q*y+k
    y = r*t+s*y+l
    if x>0 and y>0: sols.add(y)

arr = list(sols)
arr.sort()
print sum(arr[i] for i in xrange(12))
