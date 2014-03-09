#!/usr/bin/env python

def count(vals, left, index, call):
    if left == 0: return 1
    if left < 0: return 0
    if call < 2:
        total = 0
        for i in xrange(index, len(vals)):
            total += count(vals, left-vals[i], i, call+1)
        return total
    else: return 0

if __name__=="__main__":
    doubles = range(2, 41, 2) + [50]
    values = range(1, 21) + [25] + doubles + range(3, 61, 3)
    values.sort(reverse=True)
    total = 0
    for i in xrange(1, 100):
        for d in doubles:
            total += count(values, i-d, 0, 0)
    print total
