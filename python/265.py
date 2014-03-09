#!/usr/bin/env python

def s(cur,used,i,n):
    if i==32: return n>>5
    if cur in used: return 0
    used.add(cur)
    total = s((cur<<1)&31,used,i+1,n<<1)
    total += s(((cur<<1)+1)&31,used,i+1,(n<<1)+1)
    used.remove(cur)
    if i==31: return total>>1
    return total

print s(0,set([]),0,0)
