#!/usr/bin/env python

from itertools import count

mem = {}
def fib(n):
    if n<=0: return 0
    if n==1: return 1
    if n==2: return 1
    if n in mem: return mem[n]
    if n&1:
        m = (n-1)/2
        mem[n] = fib(m+1)**2 + fib(m)**2
        return mem[n]
    else:
        m = n>>1
        mem[n] = fib(m+1)**2 - fib(m-1)**2
        return mem[n]

def rpan(n):
    arr = [False]*10
    tot = 0
    while n != 0:
        p = n%10
        if p==0 or arr[p]: return False
        arr[p] = True
        n /= 10
        tot += 1
    if tot < 9: return False
    return True

def lpan(n):
    n = int(str(n)[:9])
    return rpan(n)

if __name__=="__main__":
    mod = 10**9
    prev = 0
    cur = 1
    for k in count(2):
        temp = cur
        cur += prev
        cur %= mod
        prev = temp
        if rpan(cur):
            f = fib(k)
            if lpan(f):
                print k
                break
