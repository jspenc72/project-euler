#!/usr/bin/env python

N=4
cut=[[-1,1,1,1],[0,-1,1,1],[0,0,-1,1],[0,0,0,-1]]

mem={}
def f(arr):
    h=tuple(arr)
    if h in mem: return mem[h]
    t=sum(arr)
    if t==1:
        if arr[N-1]==1: return 0.0
        for i in xrange(N):
            if arr[i]: return 1.0 + f([arr[j]+cut[i][j] for j in xrange(N)])
    t=float(t)
    ret=0.0
    for i in xrange(N):
        if arr[i]<=0: continue
        ret += arr[i]/t*f([arr[j]+cut[i][j] for j in xrange(N)])
    mem[h]=ret
    return ret

print round(f([1,1,1,1]),6)
