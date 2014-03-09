#!/usr/bin/env python

N=20
number = [0,0,1]+[0]*(N+1)
d={}

def good(number,i):
    if number[i-2]+number[i-1]+number[i] > 9: return False
    if number[i-1]+number[i]+number[i+1] > 9: return False
    if number[i]+number[i+1]+number[i+2] > 9: return False
    return True

def count(number,place):
    if place == N+2: return 1
    t = (number[place-2],number[place-1],place)
    if t in d: return d[t]
    total=0
    old = number[place]
    for i in xrange(10):
        if not good(number,place): break
        total += count(number,place+1)
        number[place] += 1
    number[place] = old
    d[t] = total
    return total

print count(number,2)
