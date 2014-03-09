#!/usr/bin/env python

def gcd(x,y):
    while y!=0:
        x,y = y,x%y
    return x

num = 987654321
den = 123456789
div = gcd(num,den)
num /= div
den /= div
rat = num/den

a=1
b=0
c=0
d=1
arr = []

run = 0
prev = 1

while True:
    test = gcd(a+b,c+d)
    if (a+b)/test==den and (c+d)/test==num:
        arr.append(run)
        if prev==0: arr.append(1)
        break
    ta = a
    tb = a+b
    tc = c
    td = c+d
    if ta>0 and tb>0:
        lower = min(tc/ta, td/tb)
        upper = max(tc/ta, td/tb)
        if upper==tc/ta and tc%ta>0: upper += 1
        elif upper==td/tb and td%tb>0: upper += 1
    elif ta==0:
        lower = td/tb
        upper = float('inf')
    else:
        lower = tc/ta
        upper = float('inf')
    if lower > rat or upper <= rat:
        a += b
        c += d
        if prev==1: run+=1
        else:
            prev=1
            arr.append(run)
            run=1
    else:
        b += a
        d += c
        if prev==0: run+=1
        else:
            prev=0
            arr.append(run)
            run=1
arr.reverse()
print arr
