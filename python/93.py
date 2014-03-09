#!/usr/bin/env python

from itertools import count

groups = [[[0,1],[2,3]], [0,[[1,2],3]], [0,[1,[2,3]]], [[[0,1],2],3], [[0,[1,2]],3]]
opcombs = []
for i in xrange(4):
    for j in xrange(4):
        for k in xrange(4):
            opcombs.append([i,j,k])

def gencombs(arr):
    for a in arr:
        for b in arr:
            if b==a: continue
            for c in arr:
                if c==b or c==a: continue
                for d in arr:
                    if d==c or d==b or d==a: continue
                    yield [a,b,c,d]

def deeplen(arr):
    if type(arr) == type(0): return 1
    total = 0
    for item in arr:
        total += deeplen(item)
    return total

def reducegroup(arr, group, ops, index):
    if type(group) == type(0):
        return arr[group]
    length = deeplen(group[0])
    total = reducegroup(arr, group[0], ops, index)
    for i in xrange(1, len(group)):
        next = reducegroup(arr, group[i], ops, index+length)
        op = ops[index+length-1]
        if op == 0: total += next
        elif op == 1: total -= next
        elif op == 2: total *= next
        elif next != 0: total = float(total)/next
        else: total = float('nan')
        length = deeplen(group[i])
        index += length
    return total

best=0
bestvals = [-1,-1,-1,-1]
for a in xrange(0,10):
    for b in xrange(a+1,10):
        for c in xrange(b+1,10):
            for d in xrange(c+1,10):
                poss = set([])
                for comb in gencombs([a,b,c,d]):
                    for group in groups:
                        for ops in opcombs:
                            num = reducegroup(comb, group, ops, 0)
                            if num > 0 and abs(num - round(num)) < .01: poss.add(int(round(num)))
                for n in count(0):
                    if not n+1 in poss: break
                if n>best:
                    best=n
                    bestvals = [str(a),str(b),str(c),str(d)]
print reduce(lambda x,y: x+y, bestvals)
