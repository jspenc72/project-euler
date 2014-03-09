#!/usr/bin/env python

# lazy top-down dp
# don't need to worry about actual positions of digits,
# just how many of each have already been used.

mem={}
def ways(i,used):
    if i==18: return 1
    h = (i, tuple(used))
    if h in mem: return mem[h]
    total = 0
    for j in xrange(10):
        if used[j]==3: continue
        used[j]+=1
        total += ways(i+1, used)
        used[j]-=1
    mem[h] = total
    return total

print sum(ways(1, [0]*i+[1]+[0]*(9-i)) for i in xrange(1,10))
