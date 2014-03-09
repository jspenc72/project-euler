#!/usr/bin/python

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

if __name__=='__main__':
    count = 0
    for q in range(5, 12001):
        p = (q+1)/3 + int(not not (q+1)%3)
        while 2*p < q:
            if gcd(q, p) == 1:
                count += 1
            p += 1
    print count
