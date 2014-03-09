#!/usr/bin/env python
from itertools import count

def blocks(a, b, s):
    if b==0:
        if len(s)==10: yield []
    else:
        m = 1
        for i in count(1):
            if b//m == 0: break
            m *= 10
            trail = b%m
            lead = b//m
            if trail!=0 and trail//(m//10)==0: continue
            test = a*trail
            digits = set()
            expected = 0
            if test==0:
                digits.add(0)
                expected += 1
            while test>0:
                digits.add(test%10)
                expected += 1
                if len(digits) != expected: break
                test //= 10
            if len(digits) != expected: continue
            if len(s&digits) > 0: continue
            s |= digits
            for blk in blocks(a, lead, s):
                yield blk + [str(a*trail)]
            s -= digits

def perms(i, arr):
    if i==len(arr): yield arr
    else:
        for j in xrange(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            if arr[0]!=0:
                for p in perms(i+1, arr): yield p
            arr[i], arr[j] = arr[j], arr[i]

def maxint(block):
    block.sort(reverse=True)
    return int(reduce(lambda x,y:x+y, block))

idx=0
ans = -1
for p in perms(0, range(10)):
    idx += 1
    #if idx%1000==0: print idx
    pan = int(reduce(lambda x,y: x+y, map(str, p)))
    for t in xrange(9,4,-1):
        if (pan//10**(t-1)) % 10 == 0: continue
        x = pan//10**t
        for b in blocks(x, pan%10**t, set()):
            if len(b) <= 1: continue
            y = maxint(b)
            if y > ans:
                ans = y
                print x,
                for blk in b:
                    print int(blk)//x,
                print
print ans
