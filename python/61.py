#!/usr/bin/python

from math import *

def digits(n):
    return int(log10(n+.001)) + 1
def left(n):
    return n/100
def right(n):
    return n%100
def triangle(n):
    return n*(n+1)/2
def square(n):
    return n*n
def pentagonal(n):
    return n*(3*n-1)/2
def hexagonal(n):
    return n*(2*n-1)
def heptagonal(n):
    return n*(5*n-3)/2
def octagonal(n):
    return n*(3*n-2)

def cycle(rhalf, first, used, nums, figs):
    if len(nums) == 6: print sum(nums)
    else:
        for i in xrange(len(figs)):
            if i not in used and i != 0:
                for j in figs[i]:
                    if rhalf == left(j):
                        u = set(used)
                        u.add(i)
                        n = set(nums)
                        n.add(j)
                        if len(nums) < 5 or right(j) == left(first):
                            cycle(right(j), first, u, n, figs)

if __name__ == '__main__':
    figurate = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]
    fig = []
    toRemove = []
    for i in xrange(len(figurate)):
        fig.append(set([]))
        toRemove.append(set([]))
        num = 1
        func = figurate[i]
        poly = func(num)
        while digits(poly) < 4:
            num += 1
            poly = func(num)
        while digits(poly) == 4:
            fig[i].add(poly)
            num += 1
            poly = func(num)
    for i in xrange(len(fig)):
        for j in fig[i]:
            l = left(j)
            r = right(j)
            lfound = False
            rfound = False
            for k in xrange(len(fig)):
                if k != i:
                    for p in fig[k]:
                        lfound = lfound or (l == right(p))
                        rfound = rfound or (r == left(p))
                        if lfound and rfound:
                            break
                    if lfound and rfound:
                        break
            if not (lfound and rfound):
                toRemove[i].add(j)
    for i in xrange(len(toRemove)):
        for j in toRemove[i]:
            fig[i].remove(j)
    for i in fig[0]:
        cycle(right(i), i, set([]), set([i]), fig)
