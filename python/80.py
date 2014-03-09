#!/usr/bin/env python

if __name__=="__main__":
    from decimal import *
    getcontext().prec = 105
    total = 0
    num = 2
    while num < 100:
        root = Decimal(num).sqrt()
        while root.as_tuple()[2] >= 0:
            num += 1
            root = Decimal(num).sqrt()
        num += 1
        index = 0
        s = str(root)
        for j in xrange(100):
            while s[index] == '.':
                index += 1
            total += int(s[index])
            index += 1
    print total
