#!/usr/bin/env python
import sys

# This works as follows:
# For the next group, pick it so that it is lexicographically
# less than the previous group, where B > W

# For each valid group, we recursively add the number of ways
# to partition the remaining objects given the choice of the group.

# Runs in slightly over 1 minute on my machine. Good enough.

mem={}
def p(b,w,bprev,wprev):
    if b==0 and w==0: return 1
    if b>0 and bprev==0:
        sys.stdout.write(' FAILED')
        return 0
    test = (b,w,bprev,wprev)
    if test in mem: return mem[test]
    total = 0
    for i in xrange(min(b,bprev)+1):
        for j in xrange(w+1):
            if i==bprev and j>wprev: break
            if i==0 and (b > 0 or j==0): continue
            total += p(b-i,w-j,i,j)
    mem[test]=total
    return total

print p(60,40,60,40)
