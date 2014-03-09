#!/usr/bin/env python

mp={}
def p(n):
    if n==3: return 0
    if n in mp: return mp[n]
    ret = r(n-1)
    mp[n]=ret
    return ret

mq={}
def q(n):
    if n==3: return 1
    if n in mq: return mq[n]
    ret = q(n-1)+s(n-1)
    mq[n]=ret
    return ret

mr={}
def r(n):
    if n==3: return 2
    if n in mr: return mr[n]
    ret = 2*p(n-1)+2*s(n-1)
    mr[n]=ret
    return ret

ms={}
def s(n):
    if n==3: return 0
    if n in ms: return ms[n]
    ret = q(n-1)+s(n-1)
    ms[n]=ret
    return ret

print p(10)+q(10)+r(10)+s(10)
