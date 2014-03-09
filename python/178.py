#!/usr/bin/env python

complete=(1<<10)-1
D=40

mem={}
def pstep(d,n,s):
    if n==D: return 1 if s==complete else 0
    if (d,n,s) in mem: return mem[d,n,s]
    ret=0
    if d>0: ret += pstep(d-1,n+1,s|(1<<(d-1)))
    if d<9: ret += pstep(d+1,n+1,s|(1<<(d+1)))
    mem[d,n,s]=ret
    return ret

print sum(pstep(i,j,1<<i) for i in xrange(1,10) for j in xrange(1,D))
