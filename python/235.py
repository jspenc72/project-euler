#!/usr/bin/env python

from decimal import *

def f(x):
    return -14100*x**5001 + 14103*x**5000 + 600000000000*x**2 - 1200000000900*x + 600000000897
def fp(x):
    return -70514100*x**5000 + 70515000*x**4999 + 1200000000000*x + 1200000000900

prev = Decimal('0')
cur = Decimal('1.00232')
prec = Decimal('0.000000000000001')

while abs(cur-prev) > prec:
    slope = fp(cur)
    y = f(cur)
    prev = cur
    cur = cur+y/slope
print cur
