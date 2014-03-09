#!/usr/bin/env python

pipe = 50
prev = 0
h = 50

radii = range(50, 29, -2) + range(31, 50, 2)

for r in radii:
    h += float(2*pipe*(2*prev+2*r-2*pipe))**.5 + r - prev
    prev = r

print int(round(h*1000))
