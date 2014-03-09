#!/usr/bin/env python

# ad hoc, just do what it says to do

names = sorted([name.strip('"') for name in raw_input().split(',')])
print sum((i+1)*sum(ord(c)-ord('A')+1 for c in names[i]) for i in xrange(len(names)))
