#!/usr/bin/env python

mem={}
def desc(a,s):
    if s==0: return 1
    if a<s: return 0
    if s==1: return a
    if (a,s) in mem: return mem[a,s]
    total=0
    for i in xrange(1,a): total += desc(i,s-1)
    mem[a,s] = total
    return total

#def ways(a,s):
#    if s==1: return 0
#    total=0
#    for i in xrange(a):
#        for j in xrange(i+1,a):
#            total += desc(j-1,s-2)
#    for p in xrange(1,s-1):
#        for l in xrange(1,a):
#            for r in xrange(l):
#                mult = desc(l-r-1,p-1)
#                for i in xrange(r+1,a-p):
#                    total += mult*desc(i-1,s-p-2)
#    return total

def p(n):
    total = 0
    for k in xrange(1,n):
        total += desc(26,k)*desc(26-k,n-k)-desc(26,n)
    return total

print max(p(i) for i in xrange(1,27))
