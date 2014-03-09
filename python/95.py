#!/usr/bin/env python

N = 10**6

dsum = [0]*N
for i in xrange(1,N):
    for j in xrange(i<<1,N,i):
        dsum[j] += i

best = set([])
done = set([])
for i in xrange(1,N):
    if i in done: continue
    prev = i
    s = set([prev])
    arr = [prev]
    next = dsum[prev]
    while prev != next and next < N:
        if next in s:
            j = arr.index(next)
            subs = set(arr[j:])
            if len(subs)>len(best): best=subs
            break
        s.add(next)
        arr.append(next)
        prev = next
        next = dsum[prev]
    done |= s
print min(best)
