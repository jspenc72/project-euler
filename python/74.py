#!/usr/bin/python

import time

fact_arr = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

class memoize:
    def __init__(self, function):
        self.function = function
        self.memoized = {}

    def __call__(self, *args):
        try:
            return self.memoized[args[0]]
        except KeyError:
            self.memoized[args[0]] = self.function(*args)
            return self.memoized[args[0]]

def fact(n):
    if n in (0, 1):
        return 1
    return reduce(lambda x,y: x*y, xrange(2, n+1))

def sumofact(n):
    total = 0
    while n > 0:
        total += fact_arr[n%10]
        n /= 10
    return total
    #total = 0
    #for d in str(n):
    #    total += fact(int(d))
    #return total
    #return reduce(lambda x,y: fact(int(x))+fact(int(y)), str(n))

@memoize
def lochelper(n, s):
    if n in s:
        return 0
    s.add(n)
    return 1 + lochelper(sumofact(n), s)

def lengthochain(n):
    return lochelper(n, set([]))

if __name__ == '__main__':
    #t = time.clock() 
    count = 0
    for i in xrange(1000000):
        if lengthochain(i) == 60:
            count += 1

    print count
    #print time.clock()-t
