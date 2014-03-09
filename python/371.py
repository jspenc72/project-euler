#!/usr/bin/env python

mem={}
def p(m,n,f):
    if (m,n,f) in mem: return mem[m,n,f]
    if m==1:
        ret = float(n)/1000
        mem[m,n,f] = ret
        return ret
    # probably of hitting 000 or duplicating a non-500 plate
    ret = float(n)/1000*p(m-1,n,f) + (1-f)*float(1)/1000*p(m-1,n,f)
    # probability of getting a new plate which is not an additive inverse
    ret += f*max(0,float(999-2*n+1))/1000*p(m-1,n+1,f) \
        + (1-f)*max(0,float(999-2*n-1))/1000*p(m-1,n+1,f)
    # probability of hitting a 500 when it wasn't there before
    ret += (1-f)*float(1)/1000*p(m-1,n+1,True)
    mem[m,n,f] = ret
    return ret

total=0
for i in xrange(1,300):
    total += i*p(i,0,False)
print total
