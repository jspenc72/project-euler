#!/usr/bin/env python

def u(n):
    return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10

def diff(depth, seq, arr):
    if depth == 0: return arr
    return diff(depth-1, [seq[i]-seq[i-1] for i in xrange(1,depth+1)], [seq[depth] - seq[depth-1]] + arr)

arr = [u(i) for i in xrange(1,11)]

print sum(sum(diff(i, arr, [arr[i]])) for i in xrange(10))
