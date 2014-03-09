#!/usr/bin/env python

N=70
M=N/5

mem={}

def gao(larr, rarr, pos, n):
    if max(larr)+max(rarr)>M: return 0
    if n==N and max(larr)==min(larr) and max(rarr)==min(rarr):
        return 1
    h = (tuple(larr),tuple(rarr))
    if h in mem: return mem[h]
    total=0
    larr[pos]+=1
    total += gao(larr,rarr,(pos+1)%5,n+1)
    larr[pos]-=1
    rarr[pos]+=1
    total += gao(larr,rarr,(pos-1)%5,n+1)
    rarr[pos]-=1
    mem[h]=total
    return total

larr=[0]*5
rarr=[0]*5
print gao(larr,rarr,0,0)
