#!/usr/bin/env python

mem={}
#lucas?
def no_adjacent_cyclic(n):
#    if n==1: return 2
    if n==1: return 1
    if n==2: return 3
    if n in mem: return mem[n]
    ret = mem[n] = no_adjacent_cyclic(n-1)+no_adjacent_cyclic(n-2)
    return ret

arr = [0]*64
for i in xrange(64):
    a = not not (i&(1<<5))
    b = not not (i&(1<<4))
    c = not not (i&(1<<3))
    j = ((i<<1)-(1<<6)*a)&((1<<6)-2)
    j ^= (a^(b&c))
    arr[i]=j

s = set([])
ans = 1
for n in xrange(64):
    if n in s: continue
    total=0
    arrn=[]
    while n not in arrn:
        s.add(n)
        arrn.append(n)
        n = arr[n]
#    l = len(arrn)
#    if l<=1: continue
#    total += no_adjacent(l)
#    if l in (3,4): total -= 1
#    elif l>4: total -= no_adjacent(l-4)
#    ans *= total
    ans *= no_adjacent_cyclic(len(arrn))
print ans
