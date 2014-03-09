#!/usr/bin/env python

def f(x):
    return int(2**(30.403243784-x*x))*1E-9
seen = set()
x = -1
while x not in seen:
    seen.add(x)
    x = f(x)
print x+f(x)
